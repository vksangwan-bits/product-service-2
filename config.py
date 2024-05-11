# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres2:Mango43@host.docker.internal:5433/product' # to be used when hosting with docker
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres2:Mango43@product-db:5433/product' # to be used with kubectl minikube (the service name has to be provided)


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres2:Mango43@host.docker.internal:5433/product' # to be used when hosting with docker
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres2:Mango43@product-db:5433/product'
