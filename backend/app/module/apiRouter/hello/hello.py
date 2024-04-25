from flask import Blueprint

router = Blueprint('hello', __name__)

@router.route('/hello')
def hello():
    return 'Hello, World!'
