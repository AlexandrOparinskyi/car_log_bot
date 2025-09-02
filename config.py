from dataclasses import dataclass
from typing import Optional
from environs import env


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class Db:
    host: str
    port: str
    name: str
    user: str
    password: str


@dataclass
class AdminPanel:
    username: str
    password: str
    secret_key: str


@dataclass
class Config:
    tg_bot: TgBot
    db: Db
    admin_panel: AdminPanel



def get_config(path: Optional[str] = None) -> Config:
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"),
            admin_id=int(env("BOT_ADMIN_ID")),
        ),
        db=Db(
            host=env("DB_HOST"),
            port=env("DB_PORT"),
            name=env("DB_NAME"),
            user=env("DB_USER"),
            password=env("DB_PASSWORD"),
        ),
        admin_panel=AdminPanel(
            username=env("ADMIN_USERNAME"),
            password=env("ADMIN_PASSWORD"),
            secret_key=env("ADMIN_SECRET_KEY")
        )
    )
