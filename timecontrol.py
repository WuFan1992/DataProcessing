#!/usr/bin/env python3

from timethread import *
from const import *
from receivejson import *
from writecsv import *
from rpy2.robjects import Vector
from rpyprocess import *
import threading
import time


class Thread(BasicThread):
	""" This class is used to manage the one threading"""

	def __init__(self, r_time):
		threading.Thread.__init__(self)
		self.r_time = r_time

	def r_timecontrol_one(self):

		csv_name_index = 0
		while True:
			BasicThread.cond.acquire()
			csv_name_index +=1
			output_data_r1 = rpy_process()
			r1_output_writecsv(output_data_r1[0], str(csv_name_index)+"_R1_CSV.csv")
			if BasicThread.num_excute_one !=10:
				BasicThread.num_excute_one +=1
				BasicThread.r1_mecan_data.append(output_data_r1[1])
			else:
				BasicThread.cond.notify()
				BasicThread.cond.release()
				BasicThread.cond.wait()
				BasicThread.cond.release()	
			time.sleep(R_ONE_MINUTE)
		

	def r_timecontrol_ten(self):

		csv_name_index = 0
		while True:
			if BasicThread.num_excute_one == 10:
				BasicThread.cond.acquire()
				csv_name_index+=1
				input_r10 = Vector(BasicThread.r1_mecan_data)
				output_data_r10 = rpy_process_r10(input_r10)
				r10_output_writecsv(output_data_r10, str(csv_name_index)+"_R10_CSV.csv")
				BasicThread.num_excute_one = 0
				del BasicThread.r1_mecan_data[:]
				
				BasicThread.cond.notify()
				BasicThread.cond.release()
				


	def run(self):
		if self.r_time == R_ONE_MINUTE:
			self.r_timecontrol_one()
		elif self.r_time == R_TEN_MINUTES:
			self.r_timecontrol_ten()

			


class ThreadManage(BasicThread):
	""" This class is used to manage all the threading"""
	
	def __init__(self):
		self.r_one_thread = Thread(R_ONE_MINUTE)
		self.r_ten_thread = Thread(R_TEN_MINUTES)
		

	def thread_timecontrol(self):
		self.r_one_thread.start()
		self.r_ten_thread.start()
		

def timecontrol():
	
	r_thread = ThreadManage()
	r_thread.thread_timecontrol()




	


		

