#!/usr/bin/env python3

"""
     readjson

     Read json file, including the json data and the json configuration file
     Read command line 

"""


from error import FileTypeError
from preprocess import is_json

import argparse
import json
import os

def get_commandline():
	"""Get the command line elements."""

	parser = argparse.ArgumentParser(description="Test json to csv")
	parser.add_argument('--input', help='The input json directory')
	parser.add_argument('--config', help='The configuration file')
	args = parser.parse_args()
	return args


def read_data(filename):
	""" Read the data of one file """

	try:
		is_json(filename)

	except FileTypeError as e:
		print(" File Type Error\n")
		print("Excepted Type is %s, But the actual type is %s" %(e.expected_type, e.actual_type))

	else:
		with open(filename) as f:
			data = json.load(f)
		data_e = data["dau_array"]

		f.close()
	
		return data_e



### Read Configuration File ### 


def read_fileconfig(filename):
	"""Read the configuration file 
	"""   

	with open(filename) as f:
		config_data = json.load(f)

	NESW_dict_list = []
	
	NESW_dict_list.append(add_NESW_list(config_data,"CSection_N"))
	NESW_dict_list.append(add_NESW_list(config_data,"CSection_E"))
	NESW_dict_list.append(add_NESW_list(config_data,"CSection_S"))
	NESW_dict_list.append(add_NESW_list(config_data,"CSection_W"))
	
	return NESW_dict_list


def add_NESW_list(config_data,section_name):
	""" Retrive the essentiel data in the
	    configuration file 	
	"""
	NESW_dict= {}

	for key in config_data[section_name]["INFO_ACQ"]:
		NESW_dict[key]=config_data[section_name]["INFO_ACQ"][key][0]
	NESW_dict["section_name"] = section_name

	return NESW_dict


	
	
		



