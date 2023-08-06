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
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_from = relationship("User", foreign_keys=[user_from_id], back_populates="following")
    user_to = relationship("User", foreign_keys=[user_to_id], back_populates="followers")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    
    following = relationship("Follower", foreign_keys=[Follower.user_from_id], back_populates="user_from")
    followers = relationship("Follower", foreign_keys=[Follower.user_to_id], back_populates="user_to")
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('image', 'video'), nullable=False)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", back_populates="media")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="posts")
    media = relationship("Media", back_populates="post")
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship("User", back_populates="comments")
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", back_populates="comments")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
