import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Boolean
Base = declarative_base()

class Follower(Base):
    __tablename__= 'follower'
    id = Column(Integer, primary_key = True)
    user_from_id = Column()
    user_to_id = Column()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key = True)
    username = Column(String(250), nullable = False)
    first_name = Column(String(100), nullable = False)
    Last_name = Column(String(100), nullable = False)
    email = Column(String(100), nullable = False)
    pasword = Column(String(100), nullable = False)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    Follower = relationship(Follower)

class Another_user(Base):
    __tablename__ = 'another_user'
    id = Column(Integer, primary_key = True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post_menu(Base):
    __tablename__= 'post_menu'
    id = Column(Integer, primary_key = True)
    save = Column(Boolean, nullable = True)
    report = Column(Boolean, nullable = True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Post_sound(Base):
    __tablename__ = 'post_sound'
    id = Column(Integer, primary_key = True)
    sound = Column(Boolean, nullable = True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'coment'
    id = Column(Integer, primary_key = True)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Send(Base):
    __tablename__ = 'send'
    id = Column(Integer, primary_key = True)
    post_id = Column(Integer, ForeignKey('post'))
    post = relationship(Post)
    Another_user_id = Column(Integer, ForeignKey('another_user.id'))
    Another_user = relationship(Another_user)


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key = True)
    type = Column(String(100), nullable = False)
    url = Column(String(100), nullable = False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
