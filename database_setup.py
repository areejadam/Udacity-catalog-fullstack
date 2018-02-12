#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, func, DateTime, \
    String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, desc

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Categories(Base):

    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {'name': self.name, 'id': self.id}


class MenuItem(Base):

    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    created_date = Column(DateTime, default=func.now())

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'category name': self.category_id,
            'name': self.name,
            'description': self.description,
            'id': self.id,
            }


engine = create_engine('sqlite:///categorymenus.db')
Base.metadata.create_all(engine)