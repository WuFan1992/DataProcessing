#!/usr/bin/env python3


"""
	timethread

	BasicThread class, it is the base class of all the thread
        
	num_execute_one is a countor of the R1 , it count how many
	times R1 launch, when it arrive at 10 , the program launch
	R10 and then set it to 0  

	r1_mecan_data stock 10 output of R1 and then it is set as 
	the input parameter of R10. after R10 is executed , all
	the elements in it are deleted     

"""

import threading
import time


class BasicThread(threading.Thread):

	num_excute_one = 0
	r1_mecan_data = []
	cond = threading.Condition()


	def __init__(self):
		pass



