from flask import Blueprint
from flask import render_template, abort
from simpledu.models import Course, User

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/<username>')
def user_index(username):
    #user_item = Course.query.all()
    user_item = User.equey.filt.
    user_item = User.equey.filt.
    return render_template('user.html', user_item=user_item)


