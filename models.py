import flask_sqlalchemy import sqlalchemy

db= sqlalchemy()

class Favorite(db.Model):
    id = db.Column(db.interger, primary_key=True)
    api_id= db.Column(db.interger, unique=True)
    name= db.Column(db.String(100))
    image= db.Column(db.String(255))
