import uproot3 as up
import awkward as ak
import numba
import numpy as np



# 1.Read input argument using "argparse module"
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('file_path', type=str,
            help="python ana.py /hcp/data/data02/jwkim2/WORK/Delphes/Analysis_fatjet/4t_ex1/4t_ex1/")

args = parser.parse_args()
infile = [args.file_path + "*.root"]

# Sample name signal or bkg? for naming outputs
sample_name = 'FourTop_all'
#sample_name = 'QCD_HT2000_all'
#sample_name = 'FourTop_nosel_all'
#sample_name = 'QCD_HT2000_nosel_all'





# 2. Read branch and conver to array ( Efficient memory hanling using "lazy array" )
print(".... Read Trees")
tree = up.lazyarrays(
	infile,
	"Delphes",
	"*",
)

print("Total evt: ",len(tree))



print(".... Read Branches.. need time")
weight = tree['Event.Weight']
HT	   = tree['ScalarHT.HT']


Jet = ak.zip({
	"PT"		: tree["Jet.PT"],
	"Eta"		: tree["Jet.Eta"],
	"Phi"		: tree["Jet.Phi"],
	"T"			: tree["Jet.T"],
	"BTag"			: tree["Jet.BTag"],
})

# 3. Deal negative weight

# -- Loop based method -- ( use this if there is 0 weight )
#weight_list = ak.to_list(ak.flatten(weight))
#def make_weight_arr(weight):
#	inspected_event_weight =[]
#	for w in weight:
#	
#		ins_evt_w = 1
#		if abs(w) > 0:
#			ins_evt_w = w/abs(w)
#		else:
#			ins_evt_w = 0
#
#		inspected_event_weight.append(ins_evt_w)
#	return inspected_event_weight
#
#
#inspected_event_weight = make_weight_arr(weight_list)

# Array based method
inspected_event_weight = weight/abs(weight)
inspected_event_weight = inspected_event_weight.sum()


# 4. Particle Definition and Selections 
print(".... Particle and Event selection")

# make Jet selection mask
Jet_sel_mask = (Jet.PT > 35 ) & (abs(Jet.Eta) < 2.4)
Jet = Jet[Jet_sel_mask] # selected jet


# Baseline selection 

NJet_mask = ak.num(Jet) >= 9 # selected jet >=9 mask
HT_mask = ak.firsts(HT >= 700) # HT cut
Nbtag_mask = ak.sum(Jet.BTag,axis=1) >= 3 # at leat 3 b-tag
base_line_mask = NJet_mask & HT_mask & Nbtag_mask


# Apply cut using boolean indexing
Jet = Jet[base_line_mask]
HT  = HT[base_line_mask]
inspected_event_weight = inspected_event_weight[base_line_mask]
print("After N jet cut: ",len(Jet),len(HT),len(inspected_event_weight))


# 5. Flatten the arrays ( 2D -> 1D )
print(".... Write file")

# Fltten and chage type Awkward array to numpy array
NBtag_hist	 =  ak.to_numpy(ak.sum(Jet.BTag,axis=1))
NJet_hist    =  ak.to_numpy(ak.num(Jet))
HT_hist	     =  ak.to_numpy(ak.flatten(HT))
inspected_event_weight = ak.to_numpy(inspected_event_weight)


histo={}

histo['NBtag_hist'] = NBtag_hist
histo['NJet_hist']  = NJet_hist
histo['HT_hist']	= HT_hist
histo['weight']	= inspected_event_weight

outname = sample_name + '.npy'
np.save(outname,histo)




