#!/usr/bin/env python3


import numpy as np
from presync import *


def sync_data(X, Y):
	""" OSMOS sync function"""
	# OrdX <- sort.int(X,index.return=T)$ix
	ordX = np.argsort(X)

	# OrdY <- sort.int(Y,index.return=T)$ix
	ordY = np.argsort(Y)

	# XY <- c(X,Y)
	XY = np.concatenate((X,Y),axis=0)
	
	# Ref <- c(rep(0,length(X)),1:length(Y))
	Ref = np.repeat(0,len(X))
	tmp_array = np.arange(1,len(Y)+1)
	Ref = np.concatenate((Ref,tmp_array),axis=0)

	# OrdXY <- sort.int(XY,index.return=T)$ix
	ordXY = np.argsort(XY)

	# OrdRef <- Ref[OrdXY]
	ordRef = arrange_by_order(Ref,ordXY)

	
	# NumX <- cusum(OrdRef == 0)
	NumX = count_zero(ordRef)
	
	
	# ItmX <- NumX[OrdRef != 0]
	ItmX = select_no_zero(NumX,ordRef)

	
	
	# Itm <- ItmX[OrdY]
	ItmX = arrange_by_order(ItmX,ordY)
	

	# ResY <- ItmX
	ResY = ItmX

	# ResY[ItmX != 0] <- OrdX[ItmX]
	ResY = select_no_zero(ResY,ItmX)
	ItmX = [x-1 for x in ItmX]
	tmp_array = arrange_by_order(ordX,ItmX)
	ResY = [x+1 for x in tmp_array]

	return ResY


def arrange_by_order(basic_array, order_array):
	"""This function is used to sort an array
	   according to the order in another array	
	"""
	list_after_arrange = []	
	for order in order_array:
		list_after_arrange.append(basic_array[order])

	return list_after_arrange


def count_zero(basic_array):
	"""This function is used to count the
	   zero in the array	
	"""
	list_after_count = []
	i=0
	for x in basic_array:
		if x == 0:
			i +=1
		list_after_count.append(i)
	return list_after_count


def select_no_zero(basic_array,ref_array):
	"""This function is used to take off
	   zero in the array
	"""
	list_after_select=[]
	for i in range(len(ref_array)):
		if ref_array[i] !=0:
			list_after_select.append(basic_array[i])
	return list_after_select


def sync_process(t_mes_list):
	"""Complet synchronisation process
	"""

	# Define T1 to T4 vectors of timestamps
	t_stamps = sort_timestamps(t_mes_list)

	# Define Tref the least value of T1 to T4
	t_ref_name = get_least_timestamp(t_stamps)

	# Define I1 TO I4
	I_N = sync_data(t_stamps["CSection_N"],t_stamps[t_ref_name])
	I_E = sync_data(t_stamps["CSection_E"],t_stamps[t_ref_name])
	I_S = sync_data(t_stamps["CSection_S"],t_stamps[t_ref_name])
	I_W = sync_data(t_stamps["CSection_W"],t_stamps[t_ref_name])

	# Replace 0 to 1 for I1 TO I4
	I_N = replace_zero(I_N)
	I_E = replace_zero(I_E)
	I_S = replace_zero(I_S)
	I_W = replace_zero(I_W)

	# Extract X1 to X4 with the row given in I1 to I4
	X_N = extract_X_by_I(t_mes_list["CSection_N"],I_N)
	X_E = extract_X_by_I(t_mes_list["CSection_E"],I_E)
	X_S = extract_X_by_I(t_mes_list["CSection_S"],I_S)
	X_W = extract_X_by_I(t_mes_list["CSection_W"],I_N)
	
	# Return data with the form of dictionary 

	sync_ret = {}
	sync_ret["CSection_N"] = X_N
	sync_ret["CSection_E"] = X_E
	sync_ret["CSection_S"] = X_S
	sync_ret["CSection_W"] = X_W
	
	return sync_ret


def replace_zero(I):
	"""Replace the value 0 to 1 in I1 to I4
	"""
	return [x if x!=0 else 1 for x in I ]

def extract_X_by_I(X,I):
	"""Extract X with the row given in I
	"""
	X_ret = []
	I = [i-1 for i in I]
	for i in I:
		X_ret.append(X[i])
	return X_ret
	
	
	
	





	
		
		 

	

	
	
