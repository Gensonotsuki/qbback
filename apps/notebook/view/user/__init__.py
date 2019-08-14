from flask import Blueprint

usermsg = Blueprint('usermsg', __name__)

from apps.notebook.view.user import registe
