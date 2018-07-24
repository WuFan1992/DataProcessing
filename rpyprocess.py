#!/usr/bin/env python3

import rpy2.robjects as robj
from rpy2.robjects.packages import STAP
from rpy2.robjects.packages import importr


def rpy_process(data_e):
	
	#with open('../algo_R.R','r') as f:
	#	string = f.read()
	#rpy_func = STAP(string, "algo_R")

	#output_data = rpy_func.r_data_processing(robj.IntVector(data_e))

	rpy_module = importr('smile')
	output_data = rpy_module.r_data_processing(robj.IntVector(data_e))

	return output_data


def rpy_process_all(raw_list_dict):
	"""Rpy process to all the raw list"""

	for filename, data_e in raw_list_dict.items():
		output_data = rpy_process(data_e)
		show_info(filename, output_data) 




def show_info(filename, output_data):
	"""Show the mean/min/max value in the terminal"""

	print ("Filenmae : %s  mean value : %f   max value : %f  min value:  %f" % (filename, output_data[0],output_data[1], output_data[2]))
		
	


