#!/usr/bin/env python3

import argparse
import json
import os

def get_commandline():
	"""Get the command line elements."""

	parser = argparse.ArgumentParser(description="Test json to csv")
	parser.add_argument('--input', help='The input json directory')
	args = parser.parse_args()
	return args



def read_data(filename):
	""" Read the data of one file """

	with open(filename) as f:
		data = json.load(f)
	data_e = data["dau_array"]

	f.close()
	
	return data_e

		
def get_filenames():
	""" Get all the filenames in the directory"""

	filenames_list = os.listdir()
	return filenames_list



def read_datas(directory):
	"""Read the data of all files"""

	# Get the files names
	filename_list = get_filenames()

	filename_data_dict = {}
		
	for filename in filename_list:
		data_e = read_data(filename)
		filename_data_dict[filename] = data_e

	return filename_data_dict
		



