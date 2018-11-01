#!/usr/bin/env python3


"""
    timecontrol

    Main part of this program
    Class Thread is the class of each thread, each thread
    has its instance by initializing this class

    In this program , two thread are created
    one for R1 and the other for R10

    Each time R1 is executed, the countor of R1 add 1 and when 
    it arrive at 10 , the countor is set to 0 and R10 is executed
    	


"""



from timethread import *
from const import R_ONE_MINUTE, R_TEN_MINUTES
from writecsv import r1_output_writecsv, r10_output_writecsv

from rpy2.robjects import Vector
from rpyprocess import rpy_process, rpy_process_r10
import threading
import time


class Thread(BasicThread):
	""" This class is used to manage the one threading"""

	def __init__(self, r_time,args):
		threading.Thread.__init__(self)
		self.r_time = r_time
		self.args = args

	def r_timecontrol_one(self):

		csv_name_index = 0
		while True:
			BasicThread.cond.acquire()
			csv_name_index +=1
			output_data_r1 = rpy_process(self.args)
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
				output_data_r10 = rpy_process_r10(self.args.config, input_r10)
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
	
	def __init__(self, args):
		self.r_one_thread = Thread(R_ONE_MINUTE,args)
		self.r_ten_thread = Thread(R_TEN_MINUTES,args)
		

	def thread_timecontrol(self):
		self.r_one_thread.start()
		self.r_ten_thread.start()
		

def timecontrol(args):
	
	r_thread = ThreadManage(args)
	r_thread.thread_timecontrol()




	


		

