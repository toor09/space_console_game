from pydantic import BaseSettings


class Settings(BaseSettings):
    pass

    class Config:
        env_file = ".env"
        case_sensitive = True
