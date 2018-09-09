# Hayo's Frontmen Test

## Case
The objective is simple: build a login popup and make it functional with login credentials.

## Planned solution
I want a little more complexity in this application rather than building a quick PHP MYSQL login script that a form submits to through either a HTML form or an AJAX call. So I'm hoping to challenge myself, essentially.

To put it lightly, and probably quite stupidly, I'm going to have my first experience working in Docker containers, inspired partially by Jake Wright (see his youtube). This means I'll be doing the following:
- Create docker containers to run the API call for logging in and storing sessions.
- Have a username, password, userId, firstName, lastName, loggedInLast data storage, haven't decided between simple JSON, MYSQL, or PostgreSQL. I'm leaning towards PostgreSQL just to see what I can do with it
- Code the front-end entirely in Vue
- Have one docker service operate the login API in Python
- have one docker service operate the database
- Have one docker service operate the front-end.

With this, I'm going to save time just by having a simple website template created based off of my ejs template, so I'm going to convert that one to vueJs. Shouldn't be too difficult to do so.

## Contingency
If all else fails, I have a ton of log-in examples with PHP and MySQL. Considering they are asking for a popup, it'll be an easy customization. Although the brief does not explicitly state that they would like me to use a framework, I will do so regardless, just for the experience. If I don't fail, I'll never succeed

This is a little tight scheduled though. I have two more tests to round off, and I'm going to proceed with this without any knowledge of what I'm doing, so this will be a massive learning experience, understanding Python, mastering docker, and understanding how to operate all of this.

## How To Run
This is going to be a guide on how to run the project. This will be updated once the project is ready.

## Where is the info?
This project is divided into 3 sections and folders.
1. API
2. Backend
3. Frontend

Each folder has it's own readme with more information on how I set up the structures of each. See more information there.