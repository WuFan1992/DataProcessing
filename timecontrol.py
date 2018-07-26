#!/usr/bin/env python3

from timethread import *

from const import *
from  receivejson import *

from rpyprocess import r_algo_one, r_algo_ten

class Thread(BasicThread):
	""" This class is used to manage the one threading"""

	def __init__(self, r_time):
		threading.Thread.__init__(self)
		self.r_time = r_time


	def run(self):
		if self.r_time == R_ONE_MINUTE:
			r_timecontrol_one()
		elif self.r_time == R_TEN_MINUTES:
			r_timecontrol_ten()

			


class ThreadManage(BasicThread):
	""" This class is used to manage all the threading"""
	
	def __init__(self):
		self.serveur_thread = JsonReceive()
		self.r_one_thread = Thread(R_ONE_MINUTE)
		self.r_ten_thread = Thread(R_TEN_MINUTES)
		

	def thread_timecontrol(self):
		
		self.serveur_thread.start()
		self.r_one_thread.start()
		self.r_ten_thread.start()
		

def r_timecontrol_one():

	BasicThread.threadEvent.wait()
	while BasicThread.receive_enough_data:
		
		r_algo_one()
		if BasicThread.num_excute_one !=10:
			BasicThread.num_excute_one +=1
		else:
			BasicThread.num_excute_one = 0
		time.sleep(R_ONE_MINUTE)
		

def r_timecontrol_ten():

	BasicThread.threadEvent.wait()
	while BasicThread.receive_enough_data:
		if BasicThread.num_excute_one == 10:
			r_algo_ten()
			time.sleep(R_TEN_MINUTES)


				
def timecontrol():
	r_thread = ThreadManage()
	r_thread.thread_timecontrol()




	


		

