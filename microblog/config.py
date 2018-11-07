import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        	'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	POSTS_PER_PAGE = 10
	ADMINS = ['mluqueanguita@gmail.com']
	MAIL_SERVER = 'smtp.googlemail.com'
    	MAIL_PORT = 587
    	MAIL_USE_TLS = 1
    	MAIL_USERNAME = 'mluqueanguita@gmail.com'
    	MAIL_PASSWORD = 'uhramP58'
