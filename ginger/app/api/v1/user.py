from flask import Blueprint

from app.libs.redprint import Redprint

# user = Blueprint("user", __name__)

api = Redprint("user")

@api.route("/get")
def get_user():
    return "I am Raj"


@api.route("/create")
def create_user():
    # name
    # password
    pass
