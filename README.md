# Octopus_Server

<img src="http://i.imgur.com/B4rBF3b.png=100x20" alt="Octopus Logo" width="300">

## Introduction
API access for Back-end server supports Octopus, the in-store navigating iOS App. The http API service is built by Flask, the Python microframework. This is a part of the Team Octopus project for 2016 Spring CSCI-4440 Software Design & Documentation course.
 
 
## Requirement
- Python
- Flask
  - A Python super lightweight microframework
- MySQL
- SQLAlchemy
  - Flask-SQLAlchemy, in specific
- PyMySQL
  - Mysql directory helper module
  
Most of the requirements can be installed by calling like `pip install Flask` in terminal.

## Usage
- Create a new database `Shopping_List` in MySQL
- Go into Python Interpreter, call
  ```
  python
  >> from db_shema import db
  >>db.create_all()
  ```
  to genearate the schema of the database
- Add data into Database
- Run `Python api.py` to start the service. The default port is *:5000*
- testing HTTP GET/POST requests can be excecuted in test_client/ directory.

## Functional API
- login
- register
  - login and register are encrypted by SHA1 + salt.
- search
  - search for a list of items using keyword
- get_item
  - get a specific item detailed information using item id
- get_store
  - get all store info
- get_loc
  - get the related location (x,y) of ta specific item
  

# Credit
- SDD Octopus Team
  - Main Maintainer: Ruiqi Ma
- Related Repo:
  - Android Client
  - https://github.com/McFlyRemix/OctopusNew
