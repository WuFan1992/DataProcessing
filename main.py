#!/usr/bin/env python3


from readjson import *
from filtre import *
from rpyprocess import *
from preprocess import *
from timecontrol import *
from writecsv import *
from sync import *
from presync import *
from prerpy import *


import rpy2.rinterface as ri
from rpy2.robjects.vectors import IntVector
from rpy2.robjects import Vector
import rpy2.robjects as robj

import os

def main():
	
	"""
	# Here is the filtering and sync function		
	args = get_commandline()

	config_data = read_fileconfig(args.input)

	data_e = read_data("./0025061978_2018-07-20-16-25-54-138602.json")
	
	afterfiltering_dict = filtre_data(data_e,config_data)

	sync_ret = sync_process(afterfiltering_dict)

	pre_ret = seperate_t_mes(sync_ret)
	
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



