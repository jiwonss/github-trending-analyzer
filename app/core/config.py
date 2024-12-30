from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    github_api_base_url: str
    github_token: str

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
