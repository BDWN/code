"""comments.py"""
from endpoints import APP, RESPONSES
from flask import jsonify
from persistence import COMMENT_REPO, POST_REPO
from services.models import FACT_PREDICTION

@APP.route('/api/comments')
def get_comments():
    """Returns all comments as JSON."""
    comments = COMMENT_REPO.get_all()
    return jsonify([c.as_dict() for c in comments])

@APP.route('/api/comment/<identifier>')
def get_comment_byid(identifier):
    """Returns a single comment (by identifier) as JSON."""
    comment = COMMENT_REPO.get_byid(identifier)
    if comment is None:
        return RESPONSES['not_found']('Comment {0} not found,'.format(identifier))

    return jsonify(comment.as_dict())

@APP.route('/api/post/<identifier>/comments')
def get_comments_bypost(identifier):
    """Returns the comments for a specific post as JSON."""
    post = POST_REPO.get_byid(identifier)

    comments = []
    for comment in post.comments:
        comments.append({
            'person': {
                'name': comment.person.name,
                'photo': comment.person.photo,
            },
            'description': comment.fact.description
        })

    return jsonify(comments)

@APP.route('/api/post/<identifier>/comments/generate', methods=['POST'])
def generate_comments(identifier):
    """Generates a set of comments for a specific post."""
    post = POST_REPO.get_byid(identifier)
    user_id = post.user.get_id()
    facts = post.painting.facts
    person = post.painting.person

    for fact in facts:
        fact_id = fact.get_id()
        fact.score = FACT_PREDICTION.predict(user_id, fact_id).est

    facts = sorted(facts, key=lambda f: f.score, reverse=True)
    comment = COMMENT_REPO.create(post, facts[0], person)

    return RESPONSES['created']('Comment created.', comment.as_dict())
