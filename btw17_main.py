from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, ForeignKey

engine = create_engine('sqlite:///btw_results.db')
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base ()
class Constituency(Base):
	__tablename__ = 'constituencies'
	id = Column(Integer, primary_key = True)
	belongsTo = Column(Integer)
	name = Column(String)
	parties = relationship('Parties')

class Party(Base):
	__tablename__ = 'parties'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	constituency_id = Column(Integer, ForeignKey('constituencies.id'))
	constituencies = relationship('Constituencies')

class Vote(Base):
	__tablename__ = 'votes'
	id = Column(Integer, primary_key = True)
	e_current = Column(Integer)
	e_previous = Column(Integer)
	p_current = Column(Integer)
	p_previous = Column(Integer)
	party_id = Column(Integer, ForeignKey('parties.id'))
	parties = relationship('Parties')

# generate the DB schema automatically
Base.metadata.create_all(engine)
