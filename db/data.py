from app import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return self.long_url