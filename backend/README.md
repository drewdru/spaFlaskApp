# Backend

Backend for SpaApp
Python 3.5.2

## What is this repository for?

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

## How do I get set up?

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Migrate data base

SQLAlchemy used alembic for migrations http://alembic.zzzcomputing.com/en/latest/index.html
Autogenerate migrations can't generate all type of migrations, check: http://alembic.zzzcomputing.com/en/latest/autogenerate.html

#### To do the migration automatically

    alembic revision --autogenerate -m "migration comment"
    alembic upgrade head

#### To do the migration manually

    alembic revision -m "migration comment"

then fix generated file and use:

    alembic upgrade head


## Contribution guidelines

* Writing tests
* Code review
* Other guidelines

## Who do I talk to?

* Repo owner or admin
* Other community or team contact