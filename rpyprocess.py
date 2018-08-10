#!/usr/bin/env python3

"""
    rpyprocess

    Two rpy process, in both process, rpy2 is used
    to create a embedded R environment in Python

    library cocalculateur is created which integrate
    all the function R given by OSMOS Group
    

"""

from read_filter_sync import *

import rpy2.robjects as robj
from rpy2.robjects.packages import STAP
from rpy2.robjects.packages import importr
import threading


def rpy_process(args):
	""" Launch R1 function in Python   
	"""

	rpy_module = importr('cocalculateur')
	loadjson_module = importr('jsonlite')

	json_data = read_filter_sync(args)
	
	#json_data_json = loadjson_module.fromJSON(txt = './input_f01.json',flatten=True)
	config_data = loadjson_module.fromJSON(txt = args.config ,flatten=True)
	output_data = rpy_module.f_01(json_data,config_data)

	return output_data




def rpy_process_r10(config_file, json_data):
	""" Launch R10 function in Python
	"""

	rpy_module = importr('cocalculateur')
	loadjson_module = importr('jsonlite')
	
	#json_data = loadjson_module.fromJSON(txt = './input_f02.json',flatten=True)
	config_data = loadjson_module.fromJSON(txt = config_file ,flatten=True)
	output_data = rpy_module.f_02(json_data,config_data)

	return output_data

	



		
	


