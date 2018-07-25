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

	onefile_data_list = []
	
 
	for data_each in data:
		if data_each["type"] == "OPTIC":
			data_frames = data_each["frames"]
			for data_each_frame in data_frames:
				if data_each_frame["trigger"] !=0:
					oneline_dict = data_each_frame.copy()
					oneline_dict["action"] = data_each["action"]
					oneline_dict["SN"] = data_each["SN"]
					oneline_dict["dau_idx"] = data_each["dau_idx"]
					oneline_dict["idx"] = data_each["idx"]
					oneline_dict["type"] = data_each["type"]
					onefile_dict_list.append(oneline_dict)
				   

	return onefile_dict_list



def filtre_datas(filename_data_dict):
	"""Filtre the data in all files"""

	#Create a raw list who contain all the raw_list
	allfile_data_list = [] 	
	
	for filename, data in filename_data_dict.items():
		onefile_data_list = filtre_data(data)
		allfile_data_list+=onefile_data_list

	return allfile_data_list





def select_one_minute_data(files_data_list):
	"""Select the data of one minute"""
	pass
		

