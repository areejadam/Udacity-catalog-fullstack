#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, MenuItem, User

engine = create_engine('sqlite:///categorymenus.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user

User1 = User(name='Robo Barista', email='tinnyTim@udacity.com',
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png'
             )
session.add(User1)
session.commit()

# Menu for UrbanBurger

category1 = Categories(user_id=1, name='Snowboarding')

session.add(category1)
session.commit()

menuItem2 = MenuItem(user_id=1, name='Goggles',
                     description='Juicy grilled veggie patty with tomato mayo and lettuce'
                     , categories=category1)

session.add(menuItem2)
session.commit()

menuItem1 = MenuItem(user_id=1, name='Snowboard',
                     description='with garlic and parmesan',
                     categories=category1)

session.add(menuItem1)
session.commit()

# Menu for UrbanBurger

category2 = Categories(user_id=1, name='basket ball')

session.add(category2)
session.commit()

menuItem3 = MenuItem(user_id=1, name='bird',
                     description='Juicy grilled veggie patty with tomato mayo and lettuce'
                     , categories=category2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name='ball',
                     description='with garlic and parmesan',
                     categories=category2)

session.add(menuItem4)
session.commit()