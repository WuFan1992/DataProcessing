#!/usr/bin/env python3

import ijson
import shutil
import os 


def filtre_data(data):
	""" Filtre the data in one file.

        Args:
             data: The container which stock all the json data
	     
	"""

	# New list to save all the raw frame 

	raw_list = []
 
	for data_each in data:
		data_frames = data_each["frames"]
		for data_each_frame in data_frames:
			if data_each_frame["raw"] < 500000:
				raw_list.append(data_each_frame["raw"])
				   

	return raw_list



def filtre_datas(filename_data_dict):
	"""Filtre the data in all files"""

	#Create a raw list who contain all the raw_list
	raw_list_dict = {} 	
	
	for filename, data in filename_data_dict.items():
		raw_list = filtre_data(data)
		raw_list_dict[filename] = raw_list

	return raw_list_dict
		

