from flask.views import MethodView
from flask_smorest import Blueprint, abort
from utils import color_1, color_unique

from models import LetterModel, AlphabetModel
from schemas import LetterSchema

from db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("letters", __name__, description="Operations on letters")
"""
- get letter data
- add custom letter to alphabet
- update custom letter in alphabet
"""
@blp.route("/alphabet/<string:name>/letter/<int:unicode>")
# using /alphabet/alpabet_name/letter/letter_codepoint
# until i determine if nested routes work with flask-smorest
class Letter(MethodView):
    @blp.response(200, LetterSchema)
    def get(self, name, unicode):
        abc = db.first_or_404(db.select(AlphabetModel).filter_by(name=name))
        letter = abc.letters.filter(LetterModel.codepoint == unicode).first()
        return letter or abort(400,message="Letter not in alphabet.")
    
    @blp.response(201, LetterSchema)
    def post(self, name, unicode):
        if unicode < 128:
            abort(405,
                  message="ASCII character values are read-only. Try adding a different letter.")
        abc = db.first_or_404(db.select(AlphabetModel).filter_by(name=name),
                              description="Alphabet not found.")
        letters = abc.letters.all()
        if unicode in [o.codepoint for o in letters]:
            abort(405,
                  message="Letter has existing color values in alphabet. Try a PUT operation to rewrite values.")
        letter_colors = [[o.red,o.green,o.blue] for o in letters]
        new_color = color_unique(letter_colors)
        letter = LetterModel(
            new_color,alphabet=abc,codepoint=unicode,symbol=chr(unicode), custom=True)
        try:
            # abc.append(letter) TODO: PrettyPrinted says we can .append() like a list and the db will be updated.
            db.session.add(letter)
            abc.update()
            db.session.commit()
            return letter
        except SQLAlchemyError as e:
            print(f"{e}")

    @blp.response(201, LetterSchema)
    def put(self, name, unicode):
        if unicode < 128:
            abort(405, message="ASCII character values are read-only. Try updating a different letter.")
        abc = db.first_or_404(db.select(AlphabetModel).filter_by(name=name),
                              description="Alphabet not found.")
        letter = db.one_or_404(db.select(LetterModel).filter_by(alphabet=abc,codepoint=unicode),
                               description="Letter not found. Try a POST operation to write letter to alphabet.")
        letters = abc.letters.all()
        letter_colors = [[o.red,o.green,o.blue] for o in letters]
        try:
            letter.red,letter.green,letter.blue = color_unique(letter_colors)
            abc.update()
            db.session.commit()
            return letter
        except SQLAlchemyError as e:
            abort(500,message=f"Update failed. No new RGB values saved. Error: {e}")

    @blp.response(200,LetterSchema)
    def delete(self, name, unicode):
        if unicode < 128:
            abort(405, message="ASCII character values are read-only. Try deleting a different letter.")
        abc = db.first_or_404(db.select(AlphabetModel).filter_by(name=name),
                              description="Alphabet not found.")
        letter = db.one_or_404(db.select(LetterModel).filter_by(alphabet=abc,codepoint=unicode),
                               description="Letter not found.")
        try:
            db.session.delete(letter)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="Update failed.")

@blp.route("/letters")
class LetterList(MethodView):
    @blp.response(200, LetterSchema(many=True))
    def get(self):
        return LetterModel.query.all()  # exhaustive
