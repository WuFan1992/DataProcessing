#!/usr/bin/env python3


"""
    filtre

    filtering data according to the below condition :

    1.trigger !=0
    2.trier type= OPTIC
    3.trier dau_idx = 3
    4.trier idx = 1 2 3 4

"""



import ijson
import shutil
import os 


def filtre_data(data,config_NESW_list):
	""" Filtre the data in one file.

        Args:
             data: The container which stock all the json data
	     
	""" 

	afterfiltering_dict = create_afterfiltering_dict(config_NESW_list)

	for data_each in data:
		ret = is_data_correspond_configfile(data_each,config_NESW_list)
		if ret!=None:
			data_frames = data_each["frames"]
			for data_frame in data_frames:
				if is_data_correspond_filtering(data_frame["trigger"]):
					afterfiltering_dict[ret].append({"qu_Date":data_frame["time"], "qu_MeaNorm":data_frame["comp"]})
	return afterfiltering_dict
			
			


def create_afterfiltering_dict(config_NESW_list):
	"""This function is used to save all the filtering
           data in a list of dictionary		
	"""
	afterfiltering_dict = {}
	for section_config in config_NESW_list:
		afterfiltering_dict[section_config["section_name"]] = []

	return afterfiltering_dict
		



def is_data_correspond_configfile(data_each,config_NESW_list):
	"""This function is used to compare the data with
	   the filtering condition written in the
	   configuration file	  	
	"""
	
	for section_config in config_NESW_list:
		if section_config["dau_idx"] == data_each["dau_idx"] and section_config["idx"] == data_each["idx"] and section_config["type"] == data_each["type"]:
			return section_config["section_name"]
	return None


def is_data_correspond_filtering(data_frame_trigger):
	"""This function is used to comparer the data with
	   the general filtering condition	
	"""

	if data_frame_trigger != 0:
		return True
	else:
		return False

	
		   

def filtre_datas(filename_data_dict):
	"""Filtre the data in all files"""

	#Create a raw list who contain all the raw_list
	allfile_data_list = [] 	
	
	for filename, data in filename_data_dict.items():
		onefile_data_list = filtre_data(data)
		allfile_data_list+=onefile_data_list

	return allfile_data_list


		

