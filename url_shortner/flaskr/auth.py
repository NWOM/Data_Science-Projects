#to create authentication
from functools import wraps
from flask import request,Response,current_app

def check_auth(username,password):
	return username==current_app.config['ADMIN_USERNAME'] and password==current_app.config['ADMIN_PASSWORD']
def authenticate():
	return Response(
		'verify with proper credentials',401,
		{'WWW-Authenticate':'Basic realm="LOGIN REQD"'})
def require_auth(f):
	@wraps(f) #wraps is a higher ordeer function 
	def decor(*args, **kwargs):
		auth=request.authorization
		if not authentication or not check_auth(auth.username,auth.password):
			return authenticate()
		return f(*args,**kwargs)
	return decor		

