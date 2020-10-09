# Shoping Cart Base
## This is the root app to start the project, is mounted on Python 3.7 with cutting edge Flask, Flask-alchemy and Flasks Migrations.

#### The Front is composed for some BootStrap components and backend is mainly based on Flask. 

## Project Composition : 

#### Flask Backend plus Sql DB for users and products. 
<img src='static/users.png' width="400">

User is able to store products 

<img src='static/users2.png' width="400">

And Also products table is able to store one user as the relation one-to-one was specified 

<img src='static/product.png' width="400">

Also the front works for login user if it's valid.

What's missing?
 - JWT for flask
 - Django endpoints
 - JWt for Django. 
 
 









This App is mounted on Docker and Docker Compose, to run it please run:

```
docker-compose up
```

It will take the changes on the code and reload the container with the new ones

To install the packages locally first install pipenv
```
pip install pipenv
```
And then run 
```
pipenv install
```

## TO Create Tables on DB
Right now this projects has a SQLLite DB, pointing to **/api/data/app.db** 
To change the file or perform an init of the migrations use
```
flask db init
```
To perform a migration
of new tables please use
```
flask db migrate -m "model table"
```
Then:
```
flask db upgrade
```
