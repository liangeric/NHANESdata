# this reads and merges the public NHANES 2017-2018 Examination Data

# first make sure you do everything below in the comments using terminal
# (terminal commands start with a $)

# make sure xport is installed, if not run the line below in terminal
# $ sudo pip install xport

# download all the xpt data files from NHANES then for each file in terminal
# to convert to csv follow this format
# $ xport downloadedFile.XPT convertedFile.csv

import pandas as pd

# We will start by reading in all the converted csv data files using pandas
# In the quotations, replace with your file path to the appropriate file.
BPX_data = pd.read_csv("BPX_J.csv")
BMX_data = pd.read_csv("DATA/BMX_J.csv")
DXX_data = pd.read_csv("DXX_J.csv")
LUX_data = pd.read_csv("LUX_J.csv")
OHXREF_data = pd.read_csv("OHXREF_J.csv")
# note I manually changed types to string because of mixed types, this can be cleaned
# later in analysis
OHXDEN_data = pd.read_csv("OHXDEN_J.csv",dtype = str)
# here we change the column type of SEQN to numeric so that we can merge later
OHXDEN_data["SEQN"] = pd.to_numeric(OHXDEN_data["SEQN"])

# here we begin merging the data files into a master list based on the SEQN number
# note this only keeps the participants who have a SEQN number show up
# in every test from the examination data files
masterlist = BPX_data.merge(BMX_data,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(DXX_data,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(LUX_data,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(OHXREF_data,left_on = "SEQN",right_on = "SEQN")
masterlist = masterlist.merge(OHXDEN_data,left_on = "SEQN",right_on = "SEQN")

# here we will read out the master list to a csv file that can be used for analysis
masterlist.to_csv("masterList.csv",index = False)