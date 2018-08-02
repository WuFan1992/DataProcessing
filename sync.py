#!/usr/bin/env python3


import numpy as np


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
	tmp_array = arrange_by_order(ordX,ItmX)
	ResY = tmp_array

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










	
		
		 

	

	
	
