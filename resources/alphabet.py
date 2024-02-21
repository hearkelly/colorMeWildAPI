from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from wonderwords import RandomWord
from utils import colorful, color_128

from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from models import AlphabetModel, LetterModel
from schemas import AlphabetSchema


blp = Blueprint("alphabets", __name__, description="Operations on alphabets")
WORDS = RandomWord()

# METHODVIEW CLASSES: each method maps to one endpoint
@blp.route("/alphabet/<string:name>")
class Alphabet(MethodView):
    @blp.response(200, AlphabetSchema)
    def get(self, name): # return alphabet where id == id
        abc = AlphabetModel.query.filter(AlphabetModel.name == name).first()
        return abc


@blp.route("/alphabet")
class AlphabetList(MethodView):
    @blp.response(200, AlphabetSchema(many=True))
    def get(self): # get all alphabets
        return AlphabetModel.query.all()

    @blp.response(200, AlphabetSchema)
    def post(self):
        name = WORDS.word(include_categories=["adjective"]) + WORDS.word(include_categories=["noun"])
        print(name)
        abc = AlphabetModel(
            name=name)
        colors = color_128()
        unicode = 0
        letters = []
        for rgb in colors:
            letter = LetterModel(
                red=rgb[0],
                green=rgb[1],
                blue=rgb[2],
                alphabet=abc,
                codepoint=unicode,
                symbol=chr(unicode)
            ) # would like to tighten this call up utilizing a proper __init__ and **kwargs
            letters.append(letter)
            unicode += 1
        try:
            db.session.add(abc)
            db.session.add_all(letters)
            db.session.commit()
        except IntegrityError as e:
            abort(400, message=f"{e}")
        except SQLAlchemyError:
            abort(500,message="Database not changed.")
 
        return abc