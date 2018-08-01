#!/usr/bin/env python3


def select_least_timestamp(afterfiltering_dict):
	"""This function is used to select the
	   least value of the timestamps	 
	"""	

	length_NESW = {}
	for key in afterfiltering_dict:
		length_NESW[key] = len(afterfiltering_dict)
	return (min(length_NESW,key=length_NESW.get))
