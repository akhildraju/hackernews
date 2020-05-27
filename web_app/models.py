from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy()

class Record(DB.Model):
    key_id = DB.Column(DB.Integer, primary_key=True)
    row_id = DB.Column(DB.Integer)
    by = DB.Column(DB.String(25))
    id = DB.Column(DB.Integer)
    # kids = DB.Column(DB.String(100))
    # parent = DB.Column(DB.Integer)
    text = DB.Column(DB.String(1000))
    time = DB.Column(DB.Integer)
    type = DB.Column(DB.String(100))
    # title = DB.Column(DB.String(250))
    # url = DB.Column(DB.String(250))
    vader_score = DB.Column(DB.Float)
    neg_score = DB.Column(DB.Float)

    def __repr__(self):
        return 'Hacker News Data'
