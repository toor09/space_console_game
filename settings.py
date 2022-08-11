from pydantic import BaseSettings


class Settings(BaseSettings):
    TIC_TIMEOUT: float = 0.1
    SPACE_SYMBOLS: str = "+*.:|"
    SPACE_SYMBOLS_MAX_COUNT: int = 100

    class Config:
        env_file = ".env"
        case_sensitive = True
