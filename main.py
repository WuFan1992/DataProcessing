#!/usr/bin/env python3


from read_filter_sync import *
from preprocess import *
from timecontrol import *

import rpy2.rinterface as ri
from rpy2.robjects.vectors import IntVector
from rpy2.robjects import Vector
import rpy2.robjects as robj



import pandas as pd

from rpy2.robjects import pandas2ri

from rpy2.robjects.packages import importr



import os

def main():
	
	args = get_commandline()
			
	data_obj = read_filter_sync(args)

	output_data = rpy_process(data_obj, args.config)

	print(output_data)

	"""
	args = get_commandline()
	output_data = rpy_process(args.config)
	r1_output_writecsv(output_data[0],"csvR1.csv")

	lst = []
	for i in range(10):
		lst.append(output_data[1])
	dataf = Vector(lst)
		
	output_data_r10 = rpy_process_r10(args.config,dataf)

	print(output_data_r10)

	"""
	"""
	#csv_name = "mycsv.csv"
	"""
	#r1_output_writecsv(output_data[0],csv_name)
	
	#check_allfiles(args.input)
	"""
	os.chdir(args.input)
	
	data_e = read_datas(args.input)

	raw_list_dict = filtre_datas(data_e)  
	
	rpy_process_all(raw_list_dict)
	"""

	#timecontrol()



if __name__ == "__main__":
	main()



