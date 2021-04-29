import glob
import subprocess

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

file_list  = glob.glob("/cms/scratch/syan/work/DelphesTools_1/QCD_delphes/HT700/QCD_HT700_1/*.root")
outfile_name = "QCD_HT700_1.root"


def calc_Nout(maxfile,nfile):
    nfile = maxfile + nfile - 1
    nout = int(nfile / maxfile)
    return(nout)

maxfile= 10 # Max number of input files for each run ( argumnet )
nfile=len(file_list) #  Number of total input files
nout  = calc_Nout(maxfile,nfile) # Number of output files


for i in range(nout):
    start = i*maxfile
    end = start + maxfile

    infiles = (' '.join(file_list[start:end]))

    fn = outfile_name.split('.')[0]
    fn_out = fn + '_' + str(i) + ".root"

    print(infiles)

    # Run specific excutable codes
    args = 'python' + ' '+ 'ana.py' + ' ' + '-option' + ' ' + fn_out + ' '+  infiles
    subprocess.call(args,shell=True)
