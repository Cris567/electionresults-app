from flask import g
import sqlite3

def db_connect():
	return sqlite3.connect('btw_results.sqlite3')

def db_close(db):
	db.close()

def get_db () :
	if not hasattr (g, ’sqlite_db’) :
		db = sqlite3.connect(’btw17.db’)
		g.sqlite_db = db
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error) :
	if hasattr (g, ’sqlite_db’):
		g.sqlite_db.close()

def json_dump(filename):	
	with open(filename, 'w') as outfile:
    	json.dump(collection, outfile, indent=4, default=str)