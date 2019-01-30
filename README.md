A playground project to test flask, react, docker, ...

pip install -r requirements.txt

* flask-babel - for working with translations (not added yet)
* flask-bootstrap - base template for supporting bootstrap css
* flask-login - To support login functionality (expects certain properties and methods to be implemented in User model)
* flask-mail - For sending emails
* flask-migrate - Uses Alembic to handle database changes.
* flask-moment - wrapper for moment.js for handling client side dates and times
* flask-sqlalchemy - Wrapper for SQLAlchemy package an Object Relational Mapper
* flask-wtf - Flask wrapper around [WTForms](https://wtforms.readthedocs.io/) package for working with HTML forms.
* pyjwt - JSON web tokens - used for secure token in password reset links

## Setup
Create the database using flask shell that gives a python shell with the correct context.
```
flask db init
flask db migrate -m "some message"
flask db upgrade

flask shell
>>> #If not using the database migration framework then use the following line
>>> #db.create_all()
>>> #Add an admin user
>>> u = User(username='admin', email='admin@example.com')
>>> u.set_password('password')
>>> db.session.add(u)
>>> db.session.commit()
```

Verify tables are setup 
```
sqlite3 mydatabase.db .tables
```

Start SMTP debugging server to test sending of emails or set corrent environment variables.
```
python -m smtpd -n -c DebuggingServer localhost:8025
```

## Running

### Command Line

```
# set some environment variables. use export instead on set on Linux
# Note - we don't need the below export as flask will automatically find app.py
# set FLASK_APP=app.py
# set debugging mode (development environment only)
# set FLASK_DEBUG=1
flask run
```

```
flask shell
>>> app.url_map
>>> app.static_folder
>>> app.template_folder
```

### Docker
docker build -t testwebapp:latest .
docker run --name testwebapp -d -p 8000:5000 --rm testwebapp:latest

http://localhost:8000

docker ps
docker stop <ID>

References:
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* [WWW SQL Designer tool](http://ondras.zarovi.cz/sql/demo)
