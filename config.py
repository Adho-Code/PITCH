import os

class Config:
	SECRET_KEY = os.environ.get("SECRET_KEY")
	UPLOADED_PHOTOS_DEST = 'app/static/photos'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	SUBJECT_PREFIX = 'PITCH'
	SENDER_EMAIL = 'adhoadhigal@gmail.com'
class TestConfig(Config):
	pass
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adho:1234@localhost/pitch_test'

class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adho:1234@localhost/pitch'

	DEBUG = True



config_options = {
	'development': DevConfig,
	'production':ProdConfig
}	