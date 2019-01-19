### Data Visualisation Project ###

Data analysis and visualisation using Python3, Flask, Angular, SQLAlchemy, sqlite3.

Analysing a *.csv file with Bundestagswahlen 2017 (german elections 2017) results and visualising those.

SETUP using terminal:

Create/Open database with sqlite3
> sqlite3 btw_results.db
Run select queries etc. after data import
i.e. get all provinces, counties and parties:
sqlite> select * from provinces; select * from counties; select * from parties;

![alt text](https://github.com/Cris567/electionresults-app/blob/master/btw17-db_.png)

Import csv data:
> python3
>>> from main import insert_csv_data
>>> insert_csv_data()

