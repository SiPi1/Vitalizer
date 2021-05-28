# Where the heart of the program resides, used to let everything communicate with each other
# Gets files from 'original_presets' directory

import os
import json_handler as jh
import gui
import processing

def main():

	data_full = {}

	# Call gui.py and add User Input variables to data_full
	# for now I will just add in the default user inputs
	user_inputs = {
    	"round_amount": 3,
    	"pretty_file": True,
    	"round_lfos": True,
    	"delete_unused": True
    }

	# Get prefixes able to be enabled 
	to_check = jh.open_json('data/prefixes.json')

	# Loop through directory
	paths = os.listdir('original_presets')

	preset_data_full = {}
	preset_data_used = {}

	for path in paths:
		preset_data_full[path] = jh.open_json("original_presets/" + path)
		prefix = []
		patch_name = str(preset_data_full[path]['preset_name'])
		#jh.write_json("original_presets/" + path, preset_data_full[path], 4)

		for pref in to_check:
			if preset_data_full[path]['settings'][pref + 'on'] == 0.0:
				prefix.append(pref)

		data_full[patch_name] = {}
		data_full[patch_name]['file_path'] = "original_presets/" + path
		data_full[patch_name]['disabled_prefixes'] = prefix
		data_full[patch_name]['file_data'] = 'hi'#preset_data_full[path]
	data_full['user_inputs'] = user_inputs
	print(data_full)
	#processing.main(data) # call processing.py processing 



main()