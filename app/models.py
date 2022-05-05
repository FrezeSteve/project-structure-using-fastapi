from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Notes(Model):
    id = fields.IntField(pk=True)
    text = fields.CharField(255, null=False)
    completed = fields.BooleanField(default=False)


class Names(Model):
    id = fields.IntField(pk=True)
    text = fields.CharField(255, null=False)
    completed = fields.BooleanField(default=False)


notes_pydantic = pydantic_model_creator(Notes, name='notes')
notes_in_pydantic = pydantic_model_creator(Notes, name='notes_in', exclude_readonly=True)


