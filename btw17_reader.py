import csv
import json

file = 'btw17_kerg.csv'

def create_list(headers, data):
	list = []
	i = 3

	while i < len(data):
		who = {
			'name': headers[i],
			'first': {
				'current': data[i],
				'previous': data[i + 1]
				},
			'second': {
				'current': data[i + 2],
				'previous': data[i + 3]
			}
		}
		list.append(who)
		i += 4

	return list

def csv_reader():
	collection = []
	headers = []
	try:
		with open(file) as f:
			reader = csv.reader(f, delimiter = ';')
			for line in reader:
				if reader.line_num == 1:
					headers = line

				elif reader.line_num >= 4:
					region = {
						'id': line[0],
						'name': line[1],
						'belongs_to': line[2],
						'results': create_list(headers, line)

					}
					collection.append(region)
	except csv.Error as e:
		print(e)
		sys.exit(-1)

	return collection

# GO
# collection = csv_reader()
# write data to json file
# json_dump('btw17_data.json')
