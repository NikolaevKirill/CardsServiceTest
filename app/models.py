from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=True)
    references = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Card %r>' % self.id

