
# FastAPI Project

I create this project as an challenge for [Coodesh](https://coodesh.com/)
## Acknowledgements

 - [Coodesh Slack Support](desafios-dev.slack.com)
 

## Features

- CRUD using Restful Architecture;
- Unitary Tests using Pytest;
- Alembic Migration Tool for database maintainability;
- FastAPI micro-framework for creating fast api's;
- Postman for testing routes and documenting;
- Pydantic for data models and typing;
- SQLAlchemy for creating a native way to manipulate databases with Python;
- CORS for domains controls;
- Docker for make easy to create and manage deploys;
- 

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DATABASE_HOSTNAME = String`

`DATABASE_PORT = Integer`

`DATABASE_NAME = String`

`DATABASE_PASSWORD = String`

`DATABASE_USERNAME = String`

`POSTGRES_DB = String`

`POSTGRES_PASSWORD = String`


## Installation Locally (Full Guide)

Clone this project with:

```bash
  git clone https://github.com/gabriel-henriq/Flight-Api-Coodesh-Challenge-.git
```

CD the folder project:

```bash
  cd Flight-Api-Coodesh-Challenge-
```

Then install a python virtual environment with:

```bash
  virtualenv env
```

Activate your virtual environment

```bash
source env/bin/activate.bash
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

After all the code above, you will need an postgres database already configured to run 
with your environment variables, finally run the last commands to create your database schemas.

```bash
alembic upgrade head
```

To turn on your server you can use:


```bash
uvicorn app.main:app
```

or

```bash
uvicorn app.main:app --reload
```
## API Reference

You can use [this public postman](https://www.postman.com/spacecraft-geoscientist-97585229/workspace/my-workspace/collection/16203062-a4bf6c42-2118-4663-a1c0-241325f89243?action=share&creator=16203062).

Don't forget to setup the enviroment in right top to **Space Fly Api**

After start the server, you can check the API Documentation at [Fast API Docs with Open API](http://127.0.0.1:8000/docs)`
