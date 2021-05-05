from flask import Blueprint

blog_ab = Blueprint('blog', __name__)

def test1():
    return 'This is test1'


@blog_ab.route('/blog1')
def blog():
    return "Test Success"


 