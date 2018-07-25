#!/usr/bin/env python3


import threading
import time

from rpyprocess import r_algo_one, r_algo_ten


class BasicThread(threading.Thread):

	receive_enough_data = True
	
	def __init__(self):
		pass



class Thread(BasicThread):
	""" This class is used to manage the one threading"""

	def __init__(self, r_time):
		threading.Thread.__init__(self)
		self.r_time = r_time


	def run(self):
		r_timecontrol(self.r_time)
			


class ThreadManage(BasicThread):
	""" This class is used to manage all the threading"""
	
	def __init__(self):
		self.r_one_thread = Thread(1)
		self.r_ten_thread = Thread(10)

	def thread_timecontrol(self):
		self.r_one_thread.start()
		self.r_ten_thread.start()



def r_timecontrol(r_time):
	while BasicThread.receive_enough_data:
		if r_time == 1:
			r_algo_one()
			time.sleep(1)
		elif r_time == 10:
			r_algo_ten()
			time.sleep(10)
		else:
			return
		
		
def timecontrol():
	r_thread = ThreadManage()
	r_thread.thread_timecontrol()

	


		

