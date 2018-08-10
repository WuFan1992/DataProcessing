#!/usr/bin/env python3


"""
    prerpy

    Create dataframe as the input of R1

    In fact, the output of synchronisation is the python-dictionary object,
    which is not accepted as the input of R1. So this part is for making 
    the transformation from python-dictionary to rpy2-R-dataframe,which is 
    the structure accepted by R1 

"""



import rpy2.robjects as robj
import pandas as pd
from rpy2.robjects import pandas2ri

def create_dataframes(sync_ret):
	"""This function is used to create a whole dataframe
	   Which is accepted as the parameters of 
           R1
	"""

	robj.pandas2ri.activate()

	rbase=robj.packages.importr('base')

	N_dataframe = create_one_dataframe(sync_ret["CSection_N"])
	E_dataframe = create_one_dataframe(sync_ret["CSection_E"])
	W_dataframe = create_one_dataframe(sync_ret["CSection_W"])
	S_dataframe = create_one_dataframe(sync_ret["CSection_S"])

	close_string_to_factor()

	robj.globalenv['data_obj'] = rbase.list(CSection_N=rbase.list(data=N_dataframe),CSection_E=rbase.list(data=E_dataframe),CSection_S=rbase.list(data = S_dataframe),CSection_W=rbase.list(data = W_dataframe))

	return robj.r.data_obj

	

def create_one_dataframe(section_list):
	"""This function is used to create one dataframe
	   with its section list

	   (The section list is the value of a dictionary )
	
	"""

	list_date = []
	list_norm = []
	list_output = {}
	for x in section_list:
		list_date.append(x["qu_Date"])
		list_norm.append(x["qu_MeaNorm"])
	list_output["qu_Date"] = list_date
	list_output["qu_MeaNorm"] = list_norm
	
	dataframe = pd.DataFrame(data=list_output)

	dataframe.index +=1

	return dataframe


def close_string_to_factor():
	"""This function is used to close the R - string
	   to factor process	
	"""

	r_opt='options(stringsAsFactors = FALSE)'
	robj.r(r_opt)


	

	
		
	
		
				
