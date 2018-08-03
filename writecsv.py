#!/usr/bin/env python3


from const import *


def r1_output_writecsv(output_r1,csv_name):

	csv_file = open(csv_name, "w")

	#Write the header of the csv file
	csv_file.write("timestamp" + SEPARATOR +
		      "Moment_N" + SEPARATOR + 
		      "Moment_M" + SEPARATOR + 
		      "Moment_EpsMax" + SEPARATOR + 
	              "Moment_EpsMin" + SEPARATOR + 
                      "Moment_Angle" + SEPARATOR+
		      "Moment_MN" +SEPARATOR + 
		      "Moment_ME" + "\n")

	#Write the csv data
	num_data = len(output_r1[0])
	
	for j in range(num_data): 
		for i in range(R1_NUM_COLOM):
			csv_file.write(str(output_r1[i][j]) + SEPARATOR)
		csv_file.write("\n")
			

	csv_file.close()


	return


def writecsv(output,csv_name):

	csv_file = open(csv_name, "w")

	#Write the header of the csv file
	csv_file.write("qu_Date" + SEPARATOR +
		      "qu_MeaNorm" + SEPARATOR + "\n")

	#Write the csv data
	
	for key in output:
		csv_file.write("Smile         "+key+"               Smile    \n")
		for dict_e in output[key]:
			csv_file.write(str(dict_e["qu_Date"]) + SEPARATOR + str(dict_e["qu_MeaNorm"])+ "\n")
		csv_file.write("\n")
			
	csv_file.close()


	return


def writecsv_sync(output):

	
	for key in output:
		csv_file = open(key+"csv.csv", "w")
		write_header_filtrage(csv_file)
		for dict_e in output[key]:
			csv_file.write(str(dict_e["qu_Date"]) + SEPARATOR + str(dict_e["qu_MeaNorm"])+ "\n")
			
		csv_file.close()


	return


def write_header_filtrage(csv_file):
	"""Write the header and the rule of filtering
	"""

	csv_file.write("Fitrage par (1)trigger !=0 \n")
	csv_file.write("(2) trier type= OPTIC\n")
	csv_file.write("(3) trier dau_idx = 3\n")
	csv_file.write("(4) trier idx = 1 2 3 4\n")
	
	

	csv_file.write("qu_Date" + SEPARATOR +
		      "qu_MeaNorm" + SEPARATOR + "\n")




	


	
