from flask import Flask, request, jsonify
from flask_cors import CORS
from main import get_all_counties, get_all_provinces, get_results_by_county_party_id

app = Flask(__name__)
CORS(app)

@app.route('/getAllProvinces')
def all_provinces():
    return jsonify(get_all_provinces())

@app.route('/getAllCounties')
def all_counties():
    return jsonify(get_all_counties())

@app.route('/getResultsByCountyPartyId')
def results_by_county_party_id():
    county_id = request.args.get('countyId')
    party_id = request.args.get('partyId')
    if county_id == None:
        # TODO only placeholder
        county_id = 1
    if party_id == None:
        # id 4 = overall valid votes
        party_id = 4 #
    return jsonify(get_results_by_county_party_id(county_id, party_id))

# TODO /getResultsByProvince

# TODO /getResultsByPartyAndProvince

app.run(debug=True)
