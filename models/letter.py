from db import db

class LetterModel(db.Model):
    __tablename__ = "letters"

    id = db.Column(db.Integer, primary_key = True)
    codepoint = db.Column(db.Integer, nullable=False)  # UNICODE
    symbol = db.Column(db.String(1))
    custom = db.Column(db.Boolean, default=False)
    red = db.Column(db.Integer, nullable=False)
    green = db.Column(db.Integer, nullable=False)
    blue = db.Column(db.Integer, nullable=False)

    alphabet_id = db.Column(
        db.Integer, 
        db.ForeignKey("alphabets.id"), 
        unique = False, 
        nullable = False
        )

    # alphabet = db.relationship("AlphabetModel", back_populates="letters") 
    # populates with alphabet model object
    # nested object ?