from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Default: SQLite (no setup). You can switch to Postgres via docker-compose.
    database_url: str = "sqlite:///./app.db"

    # Model settings
    model_path: str = "./model.joblib"
    model_version: str = "xgb-breastcancer-v1"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
