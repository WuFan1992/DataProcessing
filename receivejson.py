#!/usr/bin/env python3

from timethread import *

class JsonReceive(BasicThread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.receive_times = 0


	def receive_json(self):
		while True:
			self.receive_times +=1
			print ("json file arrive %d" %(self.receive_times))
			if self.receive_times == 2:
				self.receive_times = 0
				
			time.sleep(0.5)

	def run(self):
		self.receive_json()

			
			
			
