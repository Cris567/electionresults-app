from flask import Flask, request, jsonify
from flask_cors import CORS
from main import get_all_counties, get_all_provinces, get_results_by_county_id

app = Flask(__name__)
CORS(app)

@app.route('/getAllProvinces')
def all_provinces():
    return jsonify(get_all_provinces())

@app.route('/getAllCounties')
def all_counties():
    return jsonify(get_all_counties())

@app.route('/getResultsByCountyId')
def results_by_county_id():
    county_id = request.args.get('countyId')
    if county_id == None:
        # TODO only placeholder
        county_id = 1
    return jsonify(get_results_by_county_id(county_id))

@app.route('/getResultsByPartyId')
def results_by_party_id():
    party_id = request.args.get('partyId')
    if party_id == None:
        # id 4 = overall valid votes
        party_id = 4 #
    return jsonify(get_results_by_county_id(party_id))

app.run(debug=True)
