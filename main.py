#!/usr/bin/env python3


from timecontrol import timecontrol
from readjson import get_commandline
from preprocess import create_csv_stock_dir

def main():
	
	args = get_commandline()

	create_csv_stock_dir()
				
	timecontrol(args)


if __name__ == "__main__":
	main()



