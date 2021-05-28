# Contains general and JSON functions, import json_handler as jh
# Everything should be contained in functions except imports

import json

def open_json(path):
	f = open(path, 'r')
	contents = json.load(f)
	f.close()
	return contents

def write_json(path, contents, indent):
	f = open(path, 'w')
	f.write(json.dumps(contents, indent = indent))
	f.close()

def dict_to_json(dictionary, indent):
	return json.dumps(dictionary, indent = indent)

