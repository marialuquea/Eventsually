# Mega Flask Tutorial

To run it:

$ pip install flask

$ pip install flask-wtf

$ pip install flask-sqlalchemy

$ pip install flask-migrate

---------------------------------

$ flask db init

$ flask db migrate -m "users table"

$ flask db upgrade

$ flask db migrate -m "posts table"

$ flask db upgrade

To see database:

>>> from app import db

>>> from app.models import User, Post

>>> u = ser(username='john', email='john@example.com')

>>> db.session.add(u)

>>> db.session.commit()

>>> u = User(username='susan', email='susan@example.com')

>>> db.session.add(u)

>>> db.session.commit()

>>> users = User.query.all()

>>> users

[<User john>, <User susan>]

>>> for u in users:

...     print(u.id, u.username)

...

1 john

2 susan

>>> u = User.query.get(1)
>>> u
<User john>

>>> u = User.query.get(1)
>>> p = Post(body='my first post!', author=u)
>>> db.session.add(p)
>>> db.session.commit()

>>> # get all posts written by a user
>>> u = User.query.get(1)
>>> u
<User john>
>>> posts = u.posts.all()
>>> posts
[<Post my first post!>]

>>> # same, but with a user that has no posts
>>> u = User.query.get(2)
>>> u
<User susan>
>>> u.posts.all()
[]

>>> # print post author and body for all posts 
>>> posts = Post.query.all()
>>> for p in posts:
...     print(p.id, p.author.username, p.body)
...
1 john my first post!

# get all users in reverse alphabetical order
>>> User.query.order_by(User.username.desc()).all()
[<User susan>, <User john>]

>>> users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> posts = Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
...
>>> db.session.commit()

--------------------------

$ pip install flask-login

$ pip install pyjwt

$ pip install flask-mail

$ pip install flask-moment

$ source venv2/bin/activate
