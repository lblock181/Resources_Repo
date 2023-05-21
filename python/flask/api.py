from flask import render_template, Blueprint, abort
from jinja2 import TemplateNotFound

import controller

api = Blueprint("api", __name__, template_folder="templates")

@api.route('/')
def index() -> dict:
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@api.get('/healthCheck')
def health_check() -> dict:
    return create_response("Health Check","Ok")


def create_response(status:str, response_message:str) -> dict:
    return {status: response_message}