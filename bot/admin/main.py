from fastapi import FastAPI
from sqladmin import Admin, ModelView

from bot.config import load_config
from db.db import DBUser

from .auth import AdminAuth
from sqlalchemy.ext.asyncio import (
    create_async_engine,
)

config = load_config()
engine = create_async_engine(url=config.database.url, echo=True)

app = FastAPI()
authentication_backend = AdminAuth(secret_key=config.admin_config.secret_key)
admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend, templates_dir='bot/admin/templates')


class UserAdmin(ModelView, model=DBUser):
    column_list = [DBUser.first_name, DBUser.second_name, DBUser.username, DBUser.created_at, DBUser.language]
    column_default_sort = "created_at"


admin.add_view(UserAdmin)
