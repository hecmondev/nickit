from pathlib import Path
from nickit.message import show_success_message
from inspect import cleandoc


def add_env_file():
    env_file_path = Path().resolve() / '.env'

    with open(env_file_path, 'w') as file:
        file.write('API_KEY=ANY_VALUE')


def add_settings_file():
    settings_file_path = Path().resolve() / 'settings.py'

    with open(settings_file_path, 'w') as file:
        code = """
            from pydantic_settings import BaseSettings, SettingsConfigDict
            from functools import lru_cache


            class Settings(BaseSettings):
                def __init__(self) -> None:
                    super().__init__()

                api_key: str

                # set up path
                model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


            @lru_cache
            def load_settings() -> Settings:
                return Settings()
        """
        file.write(cleandoc(code))


def add_settings():
    add_env_file()
    add_settings_file()

    show_success_message('project settings was added successfully')
