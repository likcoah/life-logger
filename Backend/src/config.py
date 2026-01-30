from os import path
from enum import IntEnum


class BotConfig:
    token: str
    admin_id: int


    def __init__(self, env_variables):
        try:
            self.token = env_variables['BOT_TOKEN']
            self.admin_id = int(env_variables['ADMIN_ID'])
        except ValueError as error:
            raise ValueError(f'{error.args[0]} is not an integer in the env file')
        except KeyError as error:
            raise ValueError(f'{error.args[0]} not found in the env file')


class Categories(IntEnum):
    routine = 0
    work = 1
    hobby = 2
    active_recreation = 3
    passive_recreation = 4


class Config:
    def __init__(self, env_variables: dict):
        self.bot = BotConfig(env_variables)
        self.categories = Categories


def parseEnvFile(env_file_path: str) -> dict:
    try:
        raw_env = {}
        with open(env_file_path, 'r') as file:
            for line in file:
                if not line.strip() or '=' not in line:
                    continue
                key, value = line.strip().split('=', 1)
                raw_env[key.strip()] = value.strip()
        return raw_env
    except FileNotFoundError as error:
        raise FileNotFoundError(f'{env_file_path} not found') from error

MAIN_DIR = path.abspath(path.join(path.dirname(__file__), ".."))
ENV_PATH = path.join(MAIN_DIR, '.env')

config = Config(parseEnvFile(ENV_PATH))

