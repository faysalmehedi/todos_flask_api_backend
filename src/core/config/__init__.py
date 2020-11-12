import os

from datetime import timedelta
from typing import Dict, Any

class FlaskConfig:
    APPLICATION_ROOT: str = "/"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "DEV")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "thisissecret")


class Database:
    _database: str = os.getenv("DB", "postgresql")
    _db_driver: str = os.getenv("DB_DRIVER", "psycopg2")
    _db_host: str = os.getenv("DB_HOST", "127.0.0.1")
    _db_port: int = int(os.getenv("DB_PORT", "5433"))
    _db_username: str = os.getenv("DB_USER", "postgres")
    _db_password: str = os.getenv("DB_PASSWORD", "postgres")
    _db_name: str = os.getenv("DB_NAME", "todo")


class SQLAlchemyConfig:
    track_modifications: bool = False
    database_uri: str = f"{Database._database}+{Database._db_driver}://{Database._db_username}:{Database._db_password}@{Database._db_host}:{Database._db_port}/{Database._db_name}"
    echo: bool = False 
    native_unicode: str = "utf-8"
    commit_on_teardown: bool = False 
    pool_size: int = 125 
    pool_recycle: int = 30 
    engine_options: Dict[str, Any] = {
        "max_overflow": 50,
        "pool_pre_ping": True
    }


class Configuration:
    # application config
    APPLICATION_ROOT: str = FlaskConfig.APPLICATION_ROOT
    ENV: str = FlaskConfig.ENVIRONMENT 
    DEBUG: bool = FlaskConfig.ENVIRONMENT == "DEV"
    SECRET_KEY: str = FlaskConfig.SECRET_KEY


    # sqlalchemy config
    SQLALCHEMY_DATABASE_URI: str = SQLAlchemyConfig.database_uri
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = SQLAlchemyConfig.track_modifications
    SQLALCHEMY_ECHO: bool = SQLAlchemyConfig.echo
    SQLALCHEMY_COMMIT_ON_TEARDOWN: bool = SQLAlchemyConfig.commit_on_teardown
    SQLALCHEMY_NATIVE_UNICODE: str = SQLAlchemyConfig.native_unicode
    SQLALCHEMY_POOL_SIZE: int = SQLAlchemyConfig.pool_size
    SQLALCHEMY_POOL_RECYCLE: int = SQLAlchemyConfig.pool_recycle
    SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = SQLAlchemyConfig.engine_options