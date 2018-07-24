#!/usr/bin/env python3

class Error(Exception):
	"""Base class for other exceptions"""
	pass

class NotJsonFileError(Error):
	"""Raised when the file is not json file"""
	pass


