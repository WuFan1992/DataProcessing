#!/usr/bin/env python3

import threading
import time


class BasicThread(threading.Thread):

	receive_enough_data = True
	num_excute_one = 0
	threadEvent = threading.Event()

	cond_enough_data = threading.Condition()

	def __init__(self):
		pass


