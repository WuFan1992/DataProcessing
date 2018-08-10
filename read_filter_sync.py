#!/usr/bin/env python3

from readjson import read_fileconfig, read_data
from filtre import filtre_data
from writecsv import writecsv_sync
from sync import sync_process
from prerpy import create_dataframes




def read_filter_sync(args):
	"""This function combine the reading JSON
	   filtering and the synchronisation 
	"""

	config_data = read_fileconfig(args.config)

	data_e = read_data(args.input)
	
	afterfiltering_dict = filtre_data(data_e,config_data)

	sync_ret = sync_process(afterfiltering_dict)

	writecsv_sync(sync_ret)

	data_obj = create_dataframes(sync_ret)

	return data_obj
