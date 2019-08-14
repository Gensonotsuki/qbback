from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True
                   )
    delete = db.Column(db.Integer,
                       default=1)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)

    def set_attrs(self, attrs):
        for k, v in attrs.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)


from apps.notebook.model import usermodel, ep7mod
