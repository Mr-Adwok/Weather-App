from pydantic_settings import BaseSettings,SettingsConfigDict




class Setting(BaseSettings):

    SECRET_KEY:str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


config = Setting()


# print(config.SECRET_KEY)