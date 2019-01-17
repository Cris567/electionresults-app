from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, ForeignKey
from reader import csv_reader
from utils import json_dump

engine = create_engine('sqlite:///btw_results.db')
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base ()

class Province(Base):
	__tablename__ = 'provinces'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	counties = relationship('County')

class County(Base):
	__tablename__ = 'counties'
	id = Column(Integer, primary_key = True)
	belongs_to = Column(Integer, ForeignKey('provinces.id'))
	name = Column(String)
	provinces = relationship('Province')
	parties = relationship('Party')

class Party(Base):
	__tablename__ = 'parties'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	county_id = Column(Integer, ForeignKey('counties.id'))
	counties = relationship('County')
	results = relationship('Result')

class Result(Base):
	__tablename__ = 'results'
	id = Column(Integer, primary_key = True)
	e_current = Column(Integer)
	e_previous = Column(Integer)
	z_current = Column(Integer)
	z_previous = Column(Integer)
	party_id = Column(Integer, ForeignKey('parties.id'))
	parties = relationship('Party')

# generate the DB schema automatically
Base.metadata.create_all(engine)

def insert_results(county, id_c):

	for r in county.get('results'):
		name = r.get('name')
		county_id = id_c
		new1 = Party(name = name, county_id = county_id)
		session.add(new1)
		session.flush()

		e_current = r.get('first').get('current')
		e_previous = r.get('first').get('previous')
		z_current = r.get('second').get('current')
		z_previous = r.get('second').get('previous')
		new2 = Result(e_current = e_current, e_previous = e_previous, z_current = z_current, z_previous = z_previous, party_id = new1.id)
		session.add(new2)
		session.commit()
	return 'SUCCESS'

def insert_csv_data():
	data = csv_reader()
	json_dump('btw17_data.json', data)
	for c in data:
		id = c.get('id')
		belongs_to = c.get('belongs_to')
		name = c.get('name')
		if belongs_to == '99' or belongs_to == '':
			new = Province(id = id, name = name)
		else:
			new = County(id = id, belongs_to = belongs_to, name = name)
		session.add(new)
		session.commit()

		if insert_results(c, id) == 'SUCCESS':
			print('Results inserted for ' + name)

	print('SUCCESS - Provinces/Counties inserted')
	return 'SUCCESS'

# insert_csv_data()

