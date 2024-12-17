from dataclasses import dataclass

from environs import Env

@dataclass
class TgBot:
    token: str


@dataclass
class Database:
    url: str

# @dataclass
# class Redis:
#     redis_host: str
#     redis_port: int
#     redis_db: int
#     redis_data: str

@dataclass
class AdminConfig:
    admin_login: str
    admin_password: str
    secret_key: str

@dataclass
class TelethonClient:
    api_id: str
    api_hash: str



@dataclass
class Config:
    tg_bot: TgBot
    database: Database
    telethon: TelethonClient
    admin_config: AdminConfig 




def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(token=env("BOT_TOKEN")),
        database=Database(url=env("DATABASE_URL")),
        telethon=TelethonClient(
            api_id=env("API_ID"),
            api_hash=env("API_HASH")),
        admin_config=AdminConfig(
            admin_login=env("ADMIN_LOGIN"),
            admin_password=env("ADMIN_PASSWORD"),
            secret_key=env("SECRET_KEY"),
        )
    )
