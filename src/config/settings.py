from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding="utf-8")

    bot_token: SecretStr = Field(alias="BOT_TOKEN")
    openai_api_key: SecretStr = Field(alias="OPENAI_API_KEY")