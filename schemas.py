from marshmallow import Schema, fields


class PlainLetterSchema(Schema):
    id = fields.Int(dump_only=True)
    codepoint = fields.Int(dump_only=True)
    symbol = fields.Str(dump_only=True)
    custom = fields.Bool(dump_only=True)
    red = fields.Int(dump_only=True)
    green = fields.Int(dump_only=True)
    blue = fields.Int(dump_only=True)

class PlainAlphabetSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)
    created_on = fields.DateTime(dump_only = True)
    updated_on = fields.DateTime(dump_only = True)

class LetterSchema(PlainLetterSchema):
    id = fields.Int(dump_only=True)
    codepoint = fields.Int(dump_only=True)
    symbol = fields.Str(dump_only=True)
    custom = fields.Bool(dump_only=True)
    red = fields.Int(dump_only=True)
    green = fields.Int(dump_only=True)
    blue = fields.Int(dump_only=True)
    alphabet_id = fields.Int(required=True, load_only=True)
    alphabet = fields.Nested(PlainAlphabetSchema(), dump_only=True)

class CustomLetterSchema(LetterSchema):
    codepoint = fields.Int(required=True)


class AlphabetSchema(PlainAlphabetSchema):
    letters = fields.List(fields.Nested(PlainLetterSchema()), dump_only = True)

    

