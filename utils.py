import json

def json_dump(filename, data):	
	with open(filename, 'w') as outfile:
		json.dump(data, outfile, indent=4, default=str)