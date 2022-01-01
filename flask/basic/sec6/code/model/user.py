from db import db

class UserModel(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password