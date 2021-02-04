import glob
import subprocess
import numpy as np
##################################################################
#  * Purpose: run excute.py code with input files			    
#  * There are many input files								
#  * You wan't to run like this:							    
#																
#  - Suppose the number of total input files = 11				
#  - You wan to input maxium 4 input files for each run															 
#    >python excute.py input0 input1 input2 input3				 
#    >python excute.py input4 input5 input6 input7				 
#    >python excute.py input8 input9 input10	    			 
#																 
#  You can choose maxfile ( max input file number )			     
#  The number of ouput files are automatically calculated		 
##################################################################

file_list  = glob.glob("/xrootd/store/mc/RunIIFall15MiniAODv2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/70000/*.root")
outfile_name = "outfile.txt"

def calc_Nout(maxfile,nfile):
		nfile = maxfile + nfile - 1
		nout = int(nfile / maxfile)
		return(nout)

maxfile=200 # Max number of input files for each run ( argumnet )
nfile=len(file_list) #  Number of total input files
print(nfile)
nout  = calc_Nout(maxfile,nfile) # Number of output files

arr_list = []

for i in range(nout):
    start = i*maxfile
    end = start + maxfile

    if i == 2: end -= 7

    filename = "ttbar_70000_" + str(i+1) + ".txt"
    txtfile = open(filename,'w')
    for j in range(start, end):
        txtfile.write(file_list[j]+"\n")
    txtfile.close()
