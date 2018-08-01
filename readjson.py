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


	
	
		



