from db import db

from datetime import datetime


class AlphabetModel(db.Model):
    __tablename__= "alphabets"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(127), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow)

    letters = db.relationship(
        "LetterModel", 
        backref="alphabet",  
        lazy="dynamic"
        )
        # with lazy="dynamic", items not fetched until program calls

    def __repr__(self):
        return f"Alphabet <{self.name}>"