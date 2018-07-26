#!/usr/bin/env python3


import threading
import time

from rpyprocess import r_algo_one, r_algo_ten


class BasicThread(threading.Thread):

	receive_enough_data = True
	num_excute_one = 0
	
	def __init__(self):
		pass



class Thread(BasicThread):
	""" This class is used to manage the one threading"""

	def __init__(self, r_time):
		threading.Thread.__init__(self)
		self.r_time = r_time


	def run(self):
		if self.r_time ==  1:
			r_timecontrol_one()
		elif self.r_time == 10:
			r_timecontrol_ten()
			


class ThreadManage(BasicThread):
	""" This class is used to manage all the threading"""
	
	def __init__(self):
		self.r_one_thread = Thread(1)
		self.r_ten_thread = Thread(10)

	def thread_timecontrol(self):
		self.r_one_thread.start()
		self.r_ten_thread.start()



def r_timecontrol_one():
	
	while BasicThread.receive_enough_data:
		r_algo_one()
		if BasicThread.num_excute_one !=10:
			BasicThread.num_excute_one +=1
		else:
			BasicThread.num_excute_one = 0
		time.sleep(1)
		

def r_timecontrol_ten():

	while BasicThread.receive_enough_data:
		if BasicThread.num_excute_one == 10:
			r_algo_ten()
			time.sleep(10)
			
		
def timecontrol():
	r_thread = ThreadManage()
	r_thread.thread_timecontrol()

	


		

