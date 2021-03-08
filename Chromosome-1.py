import pandas as pd
import numpy as np
import re

########################################
# Functions
def no_repeats(nparray):
    place = []
    for i in range(0,size):
        temp = []
        temp = np.unique(nparray[i])
        place.append(temp)
    return(place)
        
# Mining gene ID
def extract(lists):
    place =[]
    for i in range(0,size):
        temp = []
        temp = re.findall("ENSG...........", lists[i])
        place.append(temp)
    return(place)

# Looking for differences
def difference(array1,array2):
    place =[]
    for i in range(0,size):
        temp = []
        temp = np.setdiff1d(array1[i], array2[i], assume_unique = True)
        place.append(temp)
    return(place)

def counter(arrays):
    place = 0
    for i in range(0,size):
        if(arrays[i].size > 0):
            place = place + 1
    return place
########################################

# file location
ifile = 'C:/Users/bryan/Desktop/Data-1.csv'

# reading file
cdata = pd.read_csv(ifile)

# Selecting data
AN_ID_1 = cdata["ANNOVAR_ensembl_Gene_ID"]  #Gene ID should be here
AN_ID_2 = cdata["ANNOVAR_ensembl_Closest_gene(intergenic_only)"]    #alternative place for Gene ID

SN_ID_1 = cdata["SnpEff_ensembl_Gene_ID"]   #Gene ID for SnpEff

# Finding length of dataset
size = len(AN_ID_1)

# Liberating memory
del cdata

# Finding the Gene ID in ANNOVAR
AN_ID_tog = []
for i in range(0,size):
    if(AN_ID_1[i] == "."):
        AN_ID_tog.append(AN_ID_2[i])
    else:
        AN_ID_tog.append(AN_ID_1[i])
        
# extracting Gene ID in ANNOVAR
AN_ID = []
AN_ID = extract(AN_ID_tog)

# extracting Gene ID in SnpEff
SN_ID = []
SN_ID = extract(SN_ID_1)

# converting lists to arrays
AN_ID = np.array(AN_ID, dtype=object)
SN_ID = np.array(SN_ID, dtype=object)

# Getting rid of repeated Gene IDs
AN_ID_clean = no_repeats(AN_ID)
SN_ID_clean = no_repeats(SN_ID)

# Comparing Gene IDs 1 vs 2
dif_1 = []
dif_1 = difference(SN_ID_clean, AN_ID_clean)
dif_1_sum = counter(dif_1)

# Comparing Gene IDs 2 vs 1
dif_2 = []
dif_2 = difference(AN_ID_clean, SN_ID_clean)
dif_2_sum = counter(dif_2)

# Data Frame for results together
results = pd.DataFrame(data = [AN_ID_clean, SN_ID_clean, dif_1, dif_2], 
                       index = ["ANNOVAR", "SnpEff","SnpEff v ANNOVAR",
                                "ANNOVAR v SnpEff"])
results = results.swapaxes("index", "columns")


# Creating a .txt file with results inside
results.to_csv(path_or_buf=('C:/Users/bryan/Desktop/Chr_1.txt'),sep="\t",index=False)



