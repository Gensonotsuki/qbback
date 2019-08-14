from flask import Blueprint

main = Blueprint('index', __name__)

from apps.notebook.view.index import index