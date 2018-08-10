#!/usr/bin/env python3


"""
    receivejson

    For notify the whole system if json arrive 

    ##### Currently Not used #########"


"""

from timethread import *
from const import *

class JsonReceive(BasicThread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.receive_times = 0


	def receive_json(self):
		
		while True:
			self.receive_times +=1
			time.sleep(JSON_MINUTES)
			print ("json file arrive")
			if self.receive_times == 2:
				self.receive_times = 0
				BasicThread.threadEvent.set()
				BasicThread.threadEvent.clear()
						
			
	def run(self):
		self.receive_json()


	def receive_json_file():
	
		if receive_one_json_file():
			self.receive_times +=1
			if self.receive_times == 2:
				self.receive_times = 0
				BasicThread.cond_enough_data.notify()
				BasicThread.cond_enough_data.release()
				
				
				
							


	def receive_one_json_file():

		return True

			
			
			
