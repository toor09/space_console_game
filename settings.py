from pydantic import BaseSettings


class Settings(BaseSettings):
    TIC_TIMEOUT: float = 0.1

    class Config:
        env_file = ".env"
        case_sensitive = True
