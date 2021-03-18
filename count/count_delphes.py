import glob
import uproot
#file_list = glob.glob("/xrootd/store/user/soan/work/test_ex2_r/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/test/210310_045611/0000/*.root")
#file_list = glob.glob("/xrootd/store/user/soan/work/test_ex2_rr/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/test/210311_072256/0000/*.root")
file_list = glob.glob("/cms/scratch/syan/work/DelphesTools_1/fourtop_delphes/4top_ex1_v2/*.root")


## 2. Scan N of events

def counter(f_list):
    sum=0
    empty=0
    trash_files=[]
    for cnt,f in enumerate(f_list):
        dat = uproot.open(f)
        tree = dat['Delphes']
        Nevt = len(tree)
        sum += Nevt
        print(cnt+1,f,Nevt)

        if Nevt == 0:
            empty+=1
            trash_files.append(f)

    return cnt,sum,empty,trash_files


cnt,sum,empty,trash_files = counter(file_list)

## 3. Show results
print("##"*22)
print(" Total {0} evts {1} files ".format(sum,cnt+1))
print(" There are {0} number of zero files".format(empty))
for i in trash_files:
   print(i)
print("##"*22)

