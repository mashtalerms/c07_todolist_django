# SkyPro Python Course #


## Mashtaler Maksim 10/2022 - 11/2022
Backend for online application for monitoring the execution of tasks

# Description #


### Stack ###
- python3.9, Django - backend
- Postgres - database


## Features ##

1. Authentication (todolist/core)
   - VK Oauth
   - django authentication
   - profile update
2. Main logic (todolist/goals)
   - full CRUD with filters and soring for boards, categories, goals and comments
   - permissions are correctly configured to read/update/delete for all entities 
3. Telegram bot (todolist/bot) 
   - user have to verify his account due to verification code
   - user can get and create his goals
   - bot username - @Todolist_MMS_Bot
4. Tests for whole CRUD of goals and user apps (./tests)


## How to: ##

## Development local configuration ##
1) Create venv
2) Install dependencies
   - `pip install -r requirements.dev.txt`
3) Set env variables with .env file 
   - create .env file main folder
   - copy data from .env.example
4) Run docker container for postgres
   - `docker-compose --env-file .env -f deploy/docker-compose.db.yaml up -d`
5) Make migrations
   - `cd todolist`
   - `manage.py makemigrations`
   - `manage.py migrate`
6) Run server 
   - `manage.py runserver`
7) Createsuperuser
   - `manage.py createsuperuser`
8) Connect to admin panel at http://127.0.0.1:8000/admin/
9) Run tests from main folder
   - `pytest`


## Development local configuration with Frontend 
1) Create venv
2) Install dependencies
   - `pip install -r requirements.txt`
3) Set env variables with .env file 
   - create .env file in main folder
   - copy data from .env.example
4) Run docker container for postgres
   - `docker-compose --env-file .env -f deploy/docker-compose.db.yaml up -d`
5) Make migrations
   - `cd todolist`
   - `manage.py makemigrations`
   - `manage.py migrate`
6) Run server 
   - `manage.py runserver`
7) Createsuperuser
   - `manage.py createsuperuser`
8) Connect to admin panel at http://127.0.0.1:8000/admin/


1) Set env variables with .env file 
   - create .env file in main folder
   - copy data from .env.example
   - make sure to set DB_HOST to db which is a container name
2) Use docker-compose.dev.yaml from within deploy folder
   - `cd deploy`
   - `docker compose --env-file ../.env -f docker-compose.dev.yaml up -d`
3) The following would be done:
   - postgresql container would start
   - migrations would apply
   - api container would start
   - front container would start


## Project links
1) Frontend - http://skypro-mmashtaler.ga
2) Admin - http://skypro-mmashtaler.ga/admin
3) Swagger - http://skypro-mmashtaler.ga/api/schema/swagger-ui