#!/usr/bin/env python3

from collections import defaultdict
from rpy2.robjects.vectors import StrVector, FloatVector
from rpy2.robjects import DataFrame

def seperate_t_mes(sync_ret):

	section_dic = defaultdict(list)
	for key in sync_ret:
		r_mes_dic = defaultdict(list)
		data_dic = defaultdict(list)
		for row in sync_ret[key]:
			for colname in row:
				r_mes_dic[colname].append(row[colname])
		r_mes_dic["qu_Date"] = StrVector(r_mes_dic["qu_Date"])
		r_mes_dic["qu_MeaNorm"] = FloatVector(r_mes_dic["qu_MeaNorm"])

		#data_dic["data"] = r_mes_dic
		#section_dic[key] = data_dic

	return r_mes_dic
		
	
		
				
