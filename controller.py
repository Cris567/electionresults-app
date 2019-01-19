from flask import Flask, request, jsonify
from flask_cors import CORS
from main import get_all_counties, get_all_provinces, get_results_by_county_id

app = Flask(__name__)
CORS(app)

@app.route('/getAllProvinces')
def all_provinces():
    return jsonify(results = get_all_provinces())

@app.route('/getAllCounties')
def all_counties():
    return jsonify(results = get_all_counties())

@app.route('/getResultsByCountyId')
def results_by_id():
    county_id = request.args.get('countyId')
    if county_id == None:
        # TODO only placeholder
        county_id = 1
    return jsonify(results = get_results_by_county_id(county_id))

app.run(debug=True)
