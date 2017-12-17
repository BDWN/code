"""posts.py"""
from os import path, remove
from uuid import uuid4
from PIL import Image
from resizeimage import resizeimage
from endpoints import APP, RESPONSES
from endpoints.decorators import requires_auth
from flask import jsonify, request, _app_ctx_stack
from requests_futures.sessions import FuturesSession
from persistence import POST_REPO, USER_REPO, PAINTING_REPO
from services import STORAGE_CLIENT, PAINTING_CLASSIFIER

VALID_PHOTO_EXTENSIONS = ['.png', '.jpg', '.jpeg']

@APP.route('/api/posts', methods=['GET'])
def get_posts():
    """Returns all posts as JSON"""
    posts = POST_REPO.get_all()
    objects = [p.as_dict() for p in posts]
    objects.reverse()

    return jsonify(objects)

@APP.route('/api/user/<identifier>/posts', methods=['GET'])
def get_posts_byuser(identifier):
    """Returns all posts by a specific user as JSON"""
    posts = USER_REPO.get_byid(identifier).posts
    objects = [p.as_dict() for p in posts]
    objects.reverse()

    return jsonify(objects)

@APP.route('/api/post', methods=['POST'])
@requires_auth
def create_post():
    """Creates a new post."""
    if 'photo' not in request.files:
        return RESPONSES['bad_request']('No photo in payload.')

    description = request.form.get('description')
    photo = request.files['photo']
    if photo.filename == '' or '.' not in photo.filename:
        return RESPONSES['bad_request']('No photo in payload.')

    extension = path.splitext(photo.filename)[1].lower()
    if extension not in VALID_PHOTO_EXTENSIONS:
        return RESPONSES['bad_request']('Invalid photo in payload.')

    photo_filename = uuid4().hex + extension
    photo.save(photo_filename)

    # Resize photo (2MB size limit for painting classifier).
    resized_filename = 'resized_{0}'.format(photo_filename)
    with open(photo_filename, 'r+b') as file:
        with Image.open(file) as image:
            resized = resizeimage.resize_contain(image, [400, 300])
            resized = resized.convert('RGB')
            resized.save(resized_filename, resized.format)
            resized.close()

    remove(photo_filename)
    photo_filename = resized_filename

    # Upload photo to cloud object storage.
    STORAGE_CLIENT.store_object(photo_filename, 'photos-bucket')
    STORAGE_CLIENT.set_object_access('public-read', photo_filename, 'photos-bucket')
    remove(photo_filename)

    # Recognize painting in photo.
    photo_url = STORAGE_CLIENT.get_url('photos-bucket', photo_filename)
    wikidata_id = PAINTING_CLASSIFIER.classify(photo_url)
    painting = PAINTING_REPO.get_bywikidata(wikidata_id)

    if painting is None:
        return RESPONSES['not_implemented']('Photographed painting not supported.')

    user = USER_REPO.get_bysubject(_app_ctx_stack.top.current_user['sub'])
    description = ('' if description is None else description + ' ') + '#{0}'.format(painting.name)

    post = POST_REPO.create(user, painting, description, photo_filename)
    base_url = APP.config['base_url']
    FuturesSession().post('{0}/api/post/{1}/comments/generate'.format(base_url, post.get_id()))

    return RESPONSES['created']('Post created.', post.as_dict())
