from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100)
    # Add other user fields as needed

class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    author = fields.ForeignKeyField('models.User', related_name='posts')
    category = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)
