from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from apps.notebook import loginmanager
from apps.notebook.model import BaseModel, db


class UserModel(BaseModel, UserMixin):
    __bind_key__ = 'user'
    __tabalename__ = 'user'
    username = db.Column(db.String(36))
    _password = db.Column(db.String(256))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = generate_password_hash(val)

    def check_password(self, val):
        return check_password_hash(self._password, val)

    def __repr__(self):
        return f'{self.username}'


@loginmanager.user_loader
def get_user(userid):
    return UserModel.query.get(int(userid))
