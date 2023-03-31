import os 
#to  able to acess our enviroment variables

SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_NOTIFICATIONS=False
ADMIN_USERNAME=os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD=os.environ.get('ADMIN_PASSWORD')