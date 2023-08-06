import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    follower = relationship("User", foreign_keys=[follower_id])
    followed_id = Column(Integer, ForeignKey('user.id'))
    followed = relationship("User", foreign_keys=[followed_id])

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    def to_dict(self):
        return {}


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
