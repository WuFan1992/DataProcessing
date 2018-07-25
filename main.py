#!/usr/bin/env python3


from readjson import *
from filtre import *
from rpyprocess import *
from preprocess import *
from timecontrol import *

import os

def main():
	
	#args = get_commandline()
	
	#check_allfiles(args.input)
	"""
	os.chdir(args.input)
	
	data_e = read_datas(args.input)

	raw_list_dict = filtre_datas(data_e)  
	
	rpy_process_all(raw_list_dict)
	"""

	timecontrol()


if __name__ == "__main__":
	main()



