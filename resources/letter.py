from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from utils import colorful

from models import LetterModel, AlphabetModel
from schemas import LetterSchema, CustomLetterSchema

from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

blp = Blueprint("letters", __name__, description="Operations on letters")
"""
- get letter info
- add letter
- add letter to alphabet
"""
@blp.route("/alphabet/<string:name>/letter/<int:unicode>")
class Letter(MethodView):
    @blp.response(200, LetterSchema)
    def get(self, name, unicode):
        abc = AlphabetModel.query.filter(AlphabetModel.name == name).first()
        letter = abc.letters.filter(LetterModel.codepoint == unicode).first()
        return letter or abort(400,message="Letter not in alphabet.")
    
    @blp.response(201, LetterSchema)
    def put(self, name, unicode):
        abc = AlphabetModel.query.filter(AlphabetModel.name == name).first()
        letters = abc.letters.all()
        for each in letters:
            if unicode == each.codepoint and not each.custom:
                abort(400,message="Letter already in alphabet")
        rgb = colorful()
        try:
            # would like to differentiate between "added new custom letter"
            # and "updated custom letter with new rgb values"
            # maybe I should use post for new letters and put for existing letters
            letter = LetterModel(
                red=rgb[0],
                green=rgb[1],
                blue=rgb[2],
                alphabet=abc,
                codepoint=unicode,
                symbol=chr(unicode),
                custom=True
            )  # would like to simplify this call using ** and a proper LetterModel.__init__
            db.session.add(letter)
            db.session.commit()
            return letter
        except IntegrityError as e1:
            abort(400,message=f"{e1}")
        except SQLAlchemyError as e2:
            abort(500,message=f"{e2}")

    @blp.response(200,LetterSchema)
    def delete(self, name, unicode):
        abc = AlphabetModel.query.filter(AlphabetModel.name == name).first()
        letters = abc.letters.all() # can we use filter here AND properties of the child obj?
        for each in letters:
            if unicode == each.codepoint and each.custom:
                db.session.delete(each)
                db.session.commit()
                return each
        abort(400,message="Letter does not exist in this alpabet or is not a custom letter.")

@blp.route("/letters")
class LetterList(MethodView):
    @blp.response(200, LetterSchema(many=True))
    def get(self):
        return LetterModel.query.all()
    
    @blp.arguments(LetterSchema)
    @blp.response(201, LetterSchema)
    def post(self, letter_data):
        letter = LetterModel(letter_data)
        # if letter not in alphabet:
        # create new colorful letter
        # return letter model
        try:
            db.session.add(letter)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"{e}")
        return letter
