from marshmallow import Schema, fields

class TodoItemSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    due_date = fields.DateTime()
    completed = fields.Bool()