from flask import Blueprint

blue_ab = Blueprint('myblue', __name__)

@blue_ab.route('/blue1')
def blue_func():
    return 'blueblue'