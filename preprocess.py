#!/usr/bin/env python3


"""
   preprocess

   Preparation before the launch of the whole process

   #### Currently Not used #####

"""



import os
from error import FileTypeError
from const import OUTPUT_SYNC_DIR , OUTPUT_R1_DIR , OUTPUT_R10_DIR

def is_json(filename):
	"""Verify if the file is a json file"""

	file_extension = os.path.splitext(filename)[1]
	if file_extension != ".json":
		raise FileTypeError("json",file_extension)
	



def create_csv_stock_dir():
	"""Create directory to stock csv if it is 
	   not exist
	"""

	if not os.path.exists(OUTPUT_SYNC_DIR):
		os.makedirs(OUTPUT_SYNC_DIR)
	if not os.path.exists(OUTPUT_R1_DIR):
		os.makedirs(OUTPUT_R1_DIR)
	if not os.path.exists(OUTPUT_R10_DIR):
		os.makedirs(OUTPUT_R10_DIR)
	
	
	


	
	
