from pydantic_settings import BaseSettings,SettingsConfigDict

class Setting(BaseSettings):

    SECRET_KEY:str
    REDIS_HOST:str = "localhost"
    REDIS_PORT:int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra = "ignore"
    )


config = Setting()


print(config.SECRET_KEY,"helloooo -------------------------------------------------------------------------------------------")