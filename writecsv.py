#!/usr/bin/env python3

"""
    writecsv

    create the csv file for each step, including:

           1. The output of synchronisation
	   2. The outout of R1 
           3. The output of R10


"""

from const import R1_NUM_COLOM, SEPARATOR, OUTPUT_SYNC_DIR, OUTPUT_R1_DIR, OUTPUT_R10_DIR


sync_csv_index = 1


def r1_output_writecsv(output_r1,csv_name):
	"""create csv file to stock the output of R1 """

	csv_file = open(OUTPUT_R1_DIR+"/"+csv_name, "w")

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


def r10_output_writecsv(output_r10,csv_name):
	"""create csv file to stock the output of R10 """

	csv_file = open(OUTPUT_R10_DIR+"/"+csv_name, "w")

	#Write the header of the csv file
	csv_file.write("Pr_id" + SEPARATOR +
      "Exec_date"+ SEPARATOR +
      "Meas_nb"+ SEPARATOR +
      "Meas_ratio"+ SEPARATOR +
      "N_min"+ SEPARATOR +
      "N_max"+ SEPARATOR +
      "N_amp"+ SEPARATOR +
      "N_mean"+ SEPARATOR +
      "N_median"+ SEPARATOR +
      "N_maxsd"+ SEPARATOR +
      "N_min_timestamp"+ SEPARATOR +
      "N_max_timestamp"+ SEPARATOR +
      "M_min"+ SEPARATOR +
      "M_max"+ SEPARATOR +
      "M_amp"+ SEPARATOR +
      "M_mean"+ SEPARATOR +
      "M_median"+ SEPARATOR +
      "M_maxsd"+ SEPARATOR +
      "M_min_timestamp"+ SEPARATOR +
      "M_max_timestamp"+ SEPARATOR +
      "EpsMax_min"+ SEPARATOR +
      "EpsMax_max"+ SEPARATOR +
      "EpsMax_amp"+ SEPARATOR +
      "EpsMax_mean"+ SEPARATOR +
      "EpsMax_median"+ SEPARATOR +
      "EpsMax_maxsd"+ SEPARATOR +
      "EpsMax_min_timestamp"+ SEPARATOR +
      "EpsMax_max_timestamp"+ SEPARATOR +
      "EpsMin_min"+ SEPARATOR +
      "EpsMin_max"+ SEPARATOR +
      "EpsMin_amp"+ SEPARATOR +
      "EpsMin_mean"+ SEPARATOR +
      "EpsMin_median"+ SEPARATOR +
      "EpsMin_maxsd"+ SEPARATOR +
      "EpsMin_min_timestamp"+ SEPARATOR +
      "EpsMin_max_timestamp"+ SEPARATOR +
      "MN_min"+ SEPARATOR +
      "MN_max"+ SEPARATOR +
      "MN_amp"+ SEPARATOR +
      "MN_mean"+ SEPARATOR +
      "MN_median"+ SEPARATOR +
      "MN_maxsd"+ SEPARATOR +
      "MN_min_timestamp"+ SEPARATOR +
      "MN_max_timestamp"+ SEPARATOR +
      "ME_min"+ SEPARATOR +
      "ME_max"+ SEPARATOR +
      "ME_amp"+ SEPARATOR +
      "ME_mean"+ SEPARATOR +
      "ME_median"+ SEPARATOR +
      "ME_maxsd"+ SEPARATOR +
      "ME_min_timestamp"+ SEPARATOR +
      "ME_max_timestamp"+ SEPARATOR +
      "Angle_min"+ SEPARATOR +
      "Angle_max"+ SEPARATOR +
      "Angle_amp"+ SEPARATOR +
      "Angle_mean"+ SEPARATOR +
      "Angle_median"+ SEPARATOR +
      "Angle_maxsd"+ "\n")

	#Write the csv data
	num_data = len(output_r10[0])
	
	for j in range(num_data): 
		csv_file.write(str(output_r10[0][j][0]) + SEPARATOR)
	
			

	csv_file.close()


def writecsv_sync(output):
	"""create csv file to stock the output of synchronisation """
	
	global sync_csv_index

	for key in output:
		csv_file = open(OUTPUT_SYNC_DIR+"/"+key+"__"+str(sync_csv_index)+"__"+"csv.csv", "w")
		write_header_filtrage(csv_file)
		for dict_e in output[key]:
			csv_file.write(str(dict_e["qu_Date"]) + SEPARATOR + str(dict_e["qu_MeaNorm"])+ "\n")
			
		csv_file.close()
	
	sync_csv_index += 1


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




	


	
