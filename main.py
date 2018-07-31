#!/usr/bin/env python3


from readjson import *
from filtre import *
from rpyprocess import *
from preprocess import *
from timecontrol import *
from writecsv import *

import os

def main():
	
	args = get_commandline()

	config_data = read_fileconfig(args.input)

	data_e = read_data("./0025061978_2018-07-20-16-25-54-138602.json")

	afterfiltering_dict = filtre_data(data_e,config_data)

	print(len(afterfiltering_dict["CSection_W"]))
	
	#output_data = rpy_process(args.input)

	#csv_name = "mycsv.csv"

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



