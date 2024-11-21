#!/usr/bin/env python3
"""
Module for creating user database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Creates/TRepresents table for users
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

Task 2
Right way to import is highlighted in red

#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        # either set echo=False or remove it entirely as the default value is false
        self._engine = create_engine("sqlite:///a.db")
        # Drops existing tables
        Base.metadata.drop_all(self._engine)
        # creates new ones based on the models defined in user.py.
        Base.metadata.create_all(self._engine)
        # Initializes the private __session attribute to None.
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoize session object
        """
        # Checks if the private __session attribute is None.
        if self.__session is None:
            # If it is, creates a new DBSession using the database
            #   engine and assigns it to __session.
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
            # Returns the current value of __session.
        return self.__session

