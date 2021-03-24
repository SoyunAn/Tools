import uproot3 as up
import awkward1 as ak
import numba

# --Read file
infile = "/cms/scratch/syan/work/DelphesTools_1/fourtop_delphes/4top_ex1_v2/4top_ex1_v2-2018-1.root"
dat = up.open(infile)

# Read Tree
tree = dat['Delphes']

# Read branch and conver to array
weight = tree['Event.Weight'].array()


# -- cheat: ak to list (ak-array is not suportted in numba)
weight_list = ak.to_list(ak.flatten(weight))

# -- numba boost speed
@numba.njit
def make_weight_arr(weight):
	inspected_event_weight =[]
	for w in weight:
	
		ins_evt_w = 1
		if abs(w) > 0:
			ins_evt_w = ins_evt_w * (w/abs(w))
		else:
			ins_evt_w = 0

		inspected_event_weight.append(ins_evt_w)
	return inspected_event_weight


inspected_event_weight = make_weight_arr(weight_list)


#print(len(weight))
#print(len(inspected_event_weight))






import matplotlib.pyplot as plt

plt.hist(inspected_event_weight, bins=20)
plt.grid()
plt.xlabel('Weight')
plt.title('Weight')
plt.show()

