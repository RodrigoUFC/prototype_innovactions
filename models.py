from config import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UsersModel(db.Model):
    __table_args__ = {"schema": "qr_codes"}
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    pass_word = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)


class UsersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UsersModel
        include_relationships = True
        load_instance = True


class CodesModel(db.Model):
    __table_args__ = {"schema": "qr_codes"}
    __tablename__ = 'codes'
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(), nullable=False)
    qr_code = db.Column(db.String(), nullable=False)
    expires_on = db.Column(db.DateTime)


class CodesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CodesModel
        include_relationships = True
        load_instance = True


class Users:
    def __init__(self):
        self.last_name = ""
        self.first_name = ""
        self.password = ""
        self.email = ""


class Codes:
    def __init__(self):
        self.user_email = ""
        self.qr_code = ""
        self.expires_on = ""
