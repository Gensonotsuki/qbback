from flask import Blueprint

test = Blueprint('test', __name__)

from apps.notebook.view.text import apitest