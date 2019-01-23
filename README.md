# ElectionresultsApp
### Data Visualisation Project

Data analysis and visualisation using Python3, Flask, Angular, SQLAlchemy, sqlite3.

Analysing a *.csv file with Bundestagswahlen 2017 (german elections 2017) results and visualising those.
(CSV-Source https://www.bundeswahlleiter.de/dam/jcr/72f186bb-aa56-47d3-b24c-6a46f5de22d0/btw17_kerg.csv )  

## Backend SETUP:

Basic system (using terminal):

### Setup virtual environment  
(install python3 if not already done `> brew install python`)  
move to your project folder `> cd "path/projectFolder"`  
create virtual environment `> python3 -m venv "/projectFolder/"`  
activate virtual environment `> source "/projectFolder/bin/activate"`  

### Setup Flask  
`> pip install flask`  
`> pip install -U flask_cors`  
Start Flask: `python controller.py`  
Requests `http://127.0.0.1:5000/getProvinces` (check controller.py for all available methods)  

### Create/Open database with sqlite3
`> sqlite3 btw_results.db`  
Run select queries etc. after data import  
i.e. get all provinces, counties and parties:  
`sqlite> select * from provinces; select * from counties; select * from parties;`  

![alt text](https://github.com/Cris567/electionresults-app/blob/master/btw17-db_.png)

### Import csv data
`> python3`  
`>>> from main import insert_csv_data`  
`>>> insert_csv_data()`

## Frontend SETUP
The Angular part of this project was generated with Angular Version 1.7.6.

Run ` npm install angular@1.7.6` to install.

The Charts of this project are visualized with Angular ChartJS.

Run ` npm install chart.js --save` to install.

### Development server

Start Flask as described in Backend Setup above and navigate to `http://localhost:5000/`.

### Further help

To get more help on Angular ChartJS go check out the [Angular Chart README](http://jtblin.github.io/angular-chart.js/).
