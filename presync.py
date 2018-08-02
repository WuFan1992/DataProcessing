#!/usr/bin/env python3





def get_least_timestamp(t_stamp_dict):
	"""This function is used to select the
	   least value of the timestamps
	   The return value is the section name		 
	"""	
	
	len_dict = {}
	for key in t_stamp_dict:
		len_dict[key] = len(t_stamp_dict[key])
	return (min(len_dict, key=len_dict.get))
		


def sort_timestamps(afterfiltering_dict):
	"""This function is used to sort
	   the timestamps from the dictionary
	   and save it in a list
	"""

	t_stamp_dict = {}
	for key in afterfiltering_dict:
		t_stamp_dict[key] = []
		for dict_e in afterfiltering_dict[key]:
			t_stamp_dict[key].append(dict_e["qu_Date"])

	return t_stamp_dict

		
		
