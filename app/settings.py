from os import getenv
from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class _Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    ON_HEROKU: bool = getenv("DYNO") is not None
    PORT: int = int(getenv("PORT", "35500"))
    DEVELOPMENT: bool = getenv("DESTER_DEV", "").lower() == "true"

    RCLONE_LISTEN_PORT: int = int(getenv("RCLONE_LISTEN_PORT", "35530"))

MONGODB_DOMAIN=cluster0.uscpkeg.mongodb.net
MONGODB_USERNAME=Fnite
MONGODB_PASSWORD=HEywd6DBYDnbWdtT


settings = _Settings()
