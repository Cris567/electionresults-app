from flask import Flask, request, jsonify
from flask_cors import CORS
from main import get_counties, get_provinces, get_results_by_county_party_id

app = Flask(__name__)
CORS(app)

@app.route('/getProvinces')
def provinces():
    return jsonify(get_provinces())

@app.route('/getCounties')
def counties():
    province_id = request.args.get('provinceId')
    return jsonify(get_counties(province_id))

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
