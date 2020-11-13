# Todos backend api fully written in Flask

## Installation

- Please make sure docker engine install in the system; go throuh official documentation: [https://docs.docker.com/engine/install/]

- Also installed docker-compose in the system; Go throuh official documentation: [https://docs.docker.com/compose/install/]

## For Database Running

```
$ sudo docker-compose up -d
$ sudo docker-compose ps
```

## For application Running

```
$ pip install -r requirments.txt
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python server.py
```
### Go to http://0.0.0.0:5050/

## Endpoints:

- User and Authentication Endpoints
```
- /api/v1/users (Get all users from DB. Only admin can do that.)
- /api/v1/user/<email> (Get indivisual user from DB by email(unique). Only admin can do that.)
- /api/v1/create_user (Anyone can create user.)
- /api/v1/update/<email> (Update existing indivisual user in DB by email(unique). Only admin can do that.)
- /api/v1/delete/<email> (Delete indivisual user from DB by email(unique). Only admin can do that.)
- /api/v1/login (Registered user can login.)
```

- Todo Endpoints
```
- /api/v1/todos (Get all todos list for logged in user.)
- /api/v1/todo/<todo_id> (Get todo by id for Logged in user)
- /api/v1/todo/create (create todo for Logged in user)
- /api/v1/todo/update/complete (Mark "true" for todo by id for Logged in user)
- /api/v1/todo/delete/<todo_id> (Get todo by id for Logged in user)
```

## JSON DATA FORMAT
```
{
    "name": "Faysal",
    "email": "fmehedi1992@gmail.com",
    "password": "testpass123",
    "admin": "True"
}

{
    "text": "Todo Number One"
}

```
## JSON WEB TOKEN SAMPLE
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSIsImV4cCI6MTYwNDA2MTU3OX0.fn5ZaswE4VmbbtuIP76caIXKDcpGlD467YA1BiV4ilA"
}
```

 
