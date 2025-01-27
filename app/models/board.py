from app import db

class Board(db.Model):

    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False) 
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship('Card', backref='board', lazy=True)

    def to_dict(self):
        """Returns model info as a dictionary."""
        return {
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }