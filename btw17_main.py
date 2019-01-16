from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String

engine = create_engine('sqlite:///btw_results.db')
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base ()
class Constituencies(Base):
	__tablename__ = 'constituencies'
	id = Column(Integer, primary_key = True)
	belongsTo = Column(Integer)
	name = Column(String)

class Parties(Base):
	__tablename__ = 'parties'
	id = Column(Integer, primary_key = True)
	id_c = Column(Integer)
	name = Column(String)

class Votes(Base):
	__tablename__ = 'votes'
	id = Column(Integer, primary_key = True)
	id_p = Column(Integer)
	e_current = Column(Integer)
	e_previous = Column(Integer)
	p_current = Column(Integer)
	p_previous = Column(Integer)

# generate the DB schema automatically
Base.metadata.create_all(engine)
