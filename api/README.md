# Frontman Test - API

## Set up

This API is set up in Python, and by using a docker service will run in the background consistently until there is a request made.

## Usage
2 calls to be made, considering hashing needs to be stored as well.
All code will return RESTful JSON in the following structure

```json
{
	"status": "<status>",
	"msg": {
		"return": "data"
	},
	"code": "<response-code>"
}
```

### Login
The main login call to log the user into a session.

url: GET "/login"

200:
```json
[
	{
		"status": "Success",
		"msg": "Logged In",
		"code": 200
	}
]
```
404:
```json
[
	{
		"status": "Not Found",
		"msg": "Uh oh, that user doesn't exist",
		"code": 404
	}
]
```

### Register
Calling the register function will enable me to register a user so we can actually make the login work. Reason why I'm adding this call is so that I can have a hashed example working in python as well.

url: POST "/register"

**Arguments**
- username
- password

**Response**
201:
```json
[
	{
		"status": "success",
		"msg" :{
			"id": "1",
			"username": "johnDoe1",
			"passsword": "Passw0rd!",
			"firstName": "John",
			"lastName": "Doe",
			"loggedInLast": "",
		},
		"code": 201
	}
]
```
