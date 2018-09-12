import os
import markdown
import bcrypt

# Import Flask, a lightweight python web app builder framework & markdown
from flask import Flask, g, redirect, url_for, session, request
from flask_restful import Resource, Api, reqparse
# from pymongo import MongoClient
from flask_pymongo import PyMongo


# Create instance
app = Flask(__name__)
mongo = PyMongo(app, uri='mongodb://db/frontmen')

# Create API
api = Api(app)

@app.route("/")
def index():
	# present documentation
	with open(os.path.dirname(app.root_path) + '/API_Documentation.md', 'r') as markdown_file:
		# Read the content of the MD
		content = markdown_file.read()

		# Convert to HTML
		return markdown.markdown(content)

class Login(Resource):
	def get(self):
		if request.method == 'GET':
			# Condition if the user does not exists
			login_user = mongo.db.user.find_one({"username": request.form['username']})
			if login_user:
				password = bytes(request.form['password'], encoding='utf-8')
				if bcrypt.checkpw(password, login_user['password']):
					return {'status': 'Success', 'msg':'Successfully logged in', 'code': 200}, 200
				return {'status': 'Failed', 'msg':'Login credentials incorrect', 'code': 403}, 403
			return {'status': 'Failed', 'msg':'User doesn\'t exist', 'code': 404}, 404
		return {'status': 'Bad Request', 'msg': 'Oops! Something wen\'t wrong', 'code': 400}

class Register(Resource):
	def post(self):
		if request.method == 'POST':
			user = mongo.db.user
			password = bytes(request.form['password'], encoding='utf-8')
			existing_user = user.find_one({'username': request.form["username"]})
			if existing_user is None:
				hashpass = bcrypt.hashpw(password, bcrypt.gensalt())
				user.insert_one({'username': request.form['username'], 'password': hashpass, 'firstName': request.form['first-name'], 'lastName': request.form['last-name']})
				return {'status': 'Success', 'msg':'Successfully registered', 'code': 200}, 200
			return {'status': 'Failed', 'msg':'Username already taken', 'code': 409}, 409
		return {'status': 'Unauthorized', 'msg': 'Not authorized', 'code': 403}, 403

# 	item_doc = {
# 		'username' : request.form['username'],
# 		'password' : request.form['password']
# 	}
# 	db.user.insert_one(item_doc)

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')




