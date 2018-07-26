#!/usr/bin/env python3

from timethread import *
from const import *

class JsonReceive(BasicThread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.receive_times = 0


	def receive_json(self):
		
		
		#time.sleep(0.5)
		#print ("json file arrive 1")
		#time.sleep(0.5)
		#print ("json file arrive 2")
		#BasicThread.threadEvent.set()
		
		while True:
			self.receive_times +=1
			time.sleep(JSON_MINUTES)
			print ("json file arrive")
			if self.receive_times == 2:
				self.receive_times = 0
				BasicThread.threadEvent.set()
			
				
			

	def run(self):
		self.receive_json()

			
			
			
