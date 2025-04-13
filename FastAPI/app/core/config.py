from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "PDFly API"
    version: str = '1.0.0'
    debug: bool = True

    class Config:
        env_file = ".env"
        CORS_CONFIG = {
            "allow_origins": ["*"],
            "allow_credentials": True,
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        }

settings = Settings()
