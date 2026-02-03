import os
from enum import IntEnum
from dataclasses import dataclass


@dataclass(frozen=True)
class BotConfig:
    token: str
    admin_id: int


class Categories(IntEnum):
    routine = 0
    work = 1
    hobby = 2
    active_recreation = 3
    passive_recreation = 4


def fill_data_class(data_class: type, env_vars: dict) -> object:
    try:
        return data_class(**dict((var, var_type(env_vars[var.upper()])) if var.upper() in env_vars
                                 else (var, var_type(os.getenv(var.upper())))
                                 for var, var_type in data_class.__annotations__.items()))
    except Exception as error:
        raise ValueError(f'{error}\nCheck the .env file or environment variables')


class Config:
    def __init__(self, env_variables: dict):
        self.bot = fill_data_class(BotConfig, env_variables)
        self.categories = Categories


def parse_env_file(env_file_path: str) -> dict:
    try:
        with open(env_file_path, 'r') as file:
            return {parts[0].strip(): parts[1].strip() for line in file
                    if '=' in line and not line.strip().startswith('#') and (parts := line.strip().split('=', 1))}
    except FileNotFoundError as error:
        raise FileNotFoundError(f'{env_file_path} not found') from error

MAIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_PATH, ENV_PATH = os.getenv('ENV_PATH'), os.path.join(MAIN_DIR, '.env')

config = Config(parse_env_file(ENV_PATH))

