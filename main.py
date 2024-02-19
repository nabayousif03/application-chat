from tortoise import fields
from tortoise.models import Model
from pydantic import BaseModel
from fastapi import FastAPI

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=978)
    content = fields.TextField()
    author = fields.ForeignKeyField('models.User', related_name='posts')
    category = fields.CharField(max_length=670)
    from fastapi import FastAPI, HTTPException


from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

from tortoise import User, Post


app = FastAPI()

class UserIn(BaseModel):
    username: str
    email: str

class PostIn(BaseModel):
    title: str
    content: str
    author_id: int
    category: str

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    return await User.filter(id=user_id).first()

@app.get("/posts")
async def get_posts(author: str = None, category: str = None):
    filters = {}
    if author:
        filters['author__username'] = author
    if category:
        filters['category'] = category

    posts = await Post.filter(**filters).prefetch_related('author')
    return [{
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username,
        "category": post.category
    } for post in posts]

# Register Tortoise models
register_tortoise(
    app,
    db_url='sqlite://:memory:',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)