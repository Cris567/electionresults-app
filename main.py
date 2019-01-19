from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm.exc import NoResultFound
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
	results = relationship('Result')

class Party(Base):
	__tablename__ = 'parties'
	id = Column(Integer, primary_key = True)
	name = Column(String)
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
	county_id = Column(Integer, ForeignKey('counties.id'))
	counties = relationship('County')

# generate the DB schema automatically
Base.metadata.create_all(engine)

def get_party_by_name(party_name):
	try:
		party = session.query(Party).filter_by(name = party_name).one()
	except NoResultFound:
		party = []
	return party

def insert_results(county, id_c):

	for r in county.get('results'):
		name = r.get('name')
		county_id = id_c
		party = get_party_by_name(name)
		if party != []:
			party_id = party.id
		else:
			new_party = Party(name = name)
			session.add(new_party)
			session.flush()
			session.refresh(new_party)
			party_id = new_party.id

		e_current = r.get('first').get('current')
		e_previous = r.get('first').get('previous')
		z_current = r.get('second').get('current')
		z_previous = r.get('second').get('previous')
		new_results = Result(e_current = e_current, e_previous = e_previous, z_current = z_current, z_previous = z_previous, party_id = party_id, county_id = id_c)
		session.add(new_results)
		session.commit()
	return 'SUCCESS'

def insert_counties(data):
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

	return 'SUCCESS'

def insert_csv_data():
	data = csv_reader()
	print('Data import in process...')
	# json_dump('btw17_data.json', data)
	if insert_counties(data) == 'SUCCESS':
		print('Data import successful')

def get_all_provinces():
	return session.query(Province).all()

def get_all_counties():
	return session.query(County).all()

def get_results_by_county_id(county_id):
	return = session.query(Result).filter_by(county_id = county_id)
