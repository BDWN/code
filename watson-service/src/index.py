"""index.py"""
from os import getenv
from endpoints import APP
from persistence import DATABASE, USER_REPO
from persistence.models import MODEL_LIST
from services.models import FACT_PREDICTION

def initialize_db():
    """Makes sure all tables are created."""
    DATABASE.connect()
    for model in MODEL_LIST:
        DATABASE.create_table(model, safe=True)

    # Make sure demo users are present
    user1 = USER_REPO.get_byid(1)
    if user1 is None:
        USER_REPO.create('auth0|5a33987e8d3cea7aad4094f1')

    user2 = USER_REPO.get_byid(2)
    if user2 is None:
        USER_REPO.create('auth0|5a33996d7b89183611badf81')

    DATABASE.close()

def initialize_models():
    """Makes sure the models are trained."""
    package = 'scikit-surprise'
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])

    FACT_PREDICTION.train()

def initialize_config():
    """Initialize config."""
    bluemix = bool(getenv('BLUEMIX', ''))

    if bluemix:
        APP.config['base_url'] = 'https://watson-service.eu-gb.mybluemix.net'
    else:
        APP.config['base_url'] = 'http://localhost:5000'

@APP.route('/')
def index():
    """Shows a landing page."""
    return APP.send_static_file('index.html')

PORT = getenv('PORT', '5000')

if __name__ == "__main__":
    initialize_db()
    initialize_models()
    initialize_config()

    APP.run(host='0.0.0.0', port=int(PORT))
