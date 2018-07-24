#!/usr/bin/env python3

import os
from error import *


def is_json(filename):
	"""Verify if the file is a json file"""

	file_extension = os.path.splitext(filename)[1]
	if file_extension != ".json":
		raise NotJsonFileError




def check_allfiles(directory):
	"""Check all the files in directory to 
	   be json file
	"""
	
	filenames = os.listdir(directory)
	for file_e in filenames:
		try:
			is_json(file_e)
		except	NotJsonFileError:
			print("%s is not a Json File \n" %(file_e))
	


	
	
