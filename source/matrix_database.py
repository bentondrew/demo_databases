#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from drewantech_common.database_operations \
    import PostgresqlDatabaseManipulation
from sqlalchemy.ext.declaritive import declarative_base
from sqlalchemy import (Column,
                        Integer,
                        Float,
                        ForeignKey)
from sqlalchemy.orm import relationship

database_name = 'matrix_database'

db_connection = PostgresqlDatabaseManipulation(db_user='benton',
                                               db_password='benton',
                                               db_host='localhost',
                                               db_port=5432,
                                               default_db='benton')

Base = declarative_base()


class Matrix(Base):
  """Class to interface with the matrix table
  in the database via sqlalchemy"""
  __tablename__ = 'matrix'
  id = Column(Integer, primary_key=True)
  number_of_dimensions = Column(Integer)
  dimensions = relationship('Dimension', back_populates='matrix')
  points = relationship('Point', back_populates='matrix')


class Dimension(Base):
  """Class to interface with the dimension table
  in the database via sqlalchemy"""
  __tablename__ = 'dimension'
  id = Column(Integer, primary_key=True)
  matrix_id = Column(Integer, ForeignKey('matrix.id'))
  index = Column(Integer)
  size = Column(Integer)
  matrix = relationship('Matrix', back_populates='dimensions')


class Point(Base):
  """Class to interface with the point table
  in the database via sqlalchemy"""
  __tablename__ = 'point'
  id = Column(Integer, primary_key=True)
  matrix_id = Column(Integer, ForeignKey('matrix.id'))
  index = Column(Integer)
  value = Column(Float)
  matrix = relationship('Matrix', back_populates='points')


def create_database():
  db_connection.manipulate_database('CREATE', database_name)


def drop_database():
  db_connection.manipulate_database('DROP', database_name)


def create_tables():
  engine = db_connection.connect_to_database(database_name)
  Base.metadata.create_all(bind=engine)


def drop_tables():
  engine = db_connection.connect_to_database(database_name)
  Base.metadata.drop_all(bind=engine)
