#!/usr/bin/env python3


"""
    error

    Error condition 


"""


class FileTypeError(RuntimeError):
	"""Raised when the file type is not as expected"""
	
	def __init__(self,expected_type,actual_type):
		self.expected_type = expected_type
		self.actual_type = actual_type 
	

