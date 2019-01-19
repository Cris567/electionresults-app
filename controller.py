from flask import Flask, request, jsonfy
from flask_cors import CORS
from main import get_all_counties, get_all_provinces, get_results_by_county_id

app = Flask(__name__)
CORS(app)

@app.route('/getAllProvinces')
def all_provinces():
    return jsonfy(get_all_provinces())

@app.route('/getAllCounties')
def all_counties():
    return jsonfy(get_all_actors())

@app.route('/getResultsByCountyId')
def results_by_id():
    county_id = request.args.get('countyId')
    # if county_id == None:
    #    county_id = 99
    return jsonfy(get_results_by_county_id(county_id))

app.run(debug=True)
