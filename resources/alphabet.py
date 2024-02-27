from flask.views import MethodView
from flask_smorest import Blueprint, abort
from utils import color_1, color_128, make_name

from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import select
from models import AlphabetModel, LetterModel
from schemas import AlphabetSchema


blp = Blueprint("alphabets", __name__, description="Operations on alphabets")


@blp.route("/alphabet/<string:name>")
class Alphabet(MethodView):
    @blp.response(200, AlphabetSchema)
    def get(self, name):
        abc = db.first_or_404(db.select(AlphabetModel).filter_by(name=name))
        """
        .first_or_404(statement_or_query) imports from 
        Flask-SQLAlchemy and not the sqlalchemy.orm
        therefore, we are not importing .select from sqlalchemy!
        unlike .execute(statement), this returns the model
        instead of rows
        """
        return abc


@blp.route("/alphabet")
class AlphabetList(MethodView):
    @blp.response(200, AlphabetSchema(many=True))
    def get(self): # get all alphabets
        """
        uses "legacy" query call until I can figure
        out how to create dict() or AlphabetModel
        from Result Row object
        """
        return AlphabetModel.query.all()

    @blp.response(200, AlphabetSchema)
    def post(self):
        """
        generates and persists new alphabet
        containing unicode codepoints 0-127,
        each with a random RGB color value
        """
        try:
            name = make_name()
            abc = AlphabetModel(name)
            db.session.add(abc)
        except SQLAlchemyError as e: 
            print(f"{e}")
        colors = color_128()
        unicode = 0
        letters = []
        for rgb in colors:
            letter = LetterModel(
                rgb,
                alphabet=abc,
                codepoint=unicode
            )
            letters.append(letter)
            unicode += 1
        try:
            db.session.add_all(letters)
            abc.update()
            db.session.commit()
        except IntegrityError as e:
            abort(400, message=f"{e}")
        except SQLAlchemyError:
            abort(500,message="Database not changed.")
 
        return abc