#!/usr/bin/env python3

import rpy2.robjects as robj
from rpy2.robjects.packages import STAP
from rpy2.robjects.packages import importr
import threading


def rpy_process(json_data, config_file):
	

	rpy_module = importr('cocalculateur')
	loadjson_module = importr('jsonlite')

	
	#json_data_json = loadjson_module.fromJSON(txt = './input_f01.json',flatten=True)
	config_data = loadjson_module.fromJSON(txt = config_file ,flatten=True)
	output_data = rpy_module.f_01(json_data,config_data)

	return output_data




def rpy_process_r10(config_file,json_data):

	rpy_module = importr('cocalculateur')
	loadjson_module = importr('jsonlite')
	
	#json_data = loadjson_module.fromJSON(txt = './input_f02.json',flatten=True)
	config_data = loadjson_module.fromJSON(txt = config_file ,flatten=True)
	output_data = rpy_module.f_02(json_data,config_data)

	return output_data

	



def rpy_process_all(raw_list_dict):
	"""Rpy process to all the raw list"""

	for filename, data_e in raw_list_dict.items():
		output_data = rpy_process(data_e)
		show_info(filename, output_data) 




def show_info(filename, output_data):
	"""Show the mean/min/max value in the terminal"""

	print ("Filenmae : %s  mean value : %f   max value : %f  min value:  %f" % (filename, output_data[0],output_data[1], output_data[2]))




def r_algo_one():
	print("This is R 1 algo")

def r_algo_ten():
	print("This is R 10 algo")


		
	


