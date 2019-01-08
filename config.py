class Configuration():
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://mysql:mysql@127.0.0.1/DocsHub'
	SECRET_KEY = 'very very secret'
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'des_crypt'