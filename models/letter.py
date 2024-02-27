from .base import BaseModel
from db import db

class LetterModel(BaseModel):
    __tablename__ = "letter"

    id = db.Column(db.Integer, primary_key = True)
    codepoint = db.Column(db.Integer, nullable=False)  # UNICODE
    symbol = db.Column(db.String(1)) # todo: make computed property
    custom = db.Column(db.Boolean, default=False)
    red = db.Column(db.Integer, nullable=False)
    green = db.Column(db.Integer, nullable=False)
    blue = db.Column(db.Integer, nullable=False)

    alphabet_id = db.Column(
        db.String(127), 
        db.ForeignKey("alphabet.id"), 
        unique = False, 
        nullable = False
        )
    
    def __init__(self, rgb,alphabet=None,codepoint=None,symbol=None, custom=False):
        self.red, self.green, self.blue = rgb
        self.alphabet = alphabet
        self.codepoint = codepoint
        self.symbol = symbol
        self.custom = custom
