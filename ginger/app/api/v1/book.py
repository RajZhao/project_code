from flask import Blueprint

from app.libs.redprint import Redprint

# book = Blueprint("book", __name__)
api = Redprint("book")


@api.route("", methods=["GET"])
def get_book():
    return "get book"


@api.route("", methods=["POST"])
def create_book():
    return "create book"
