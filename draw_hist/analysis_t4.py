import uproot3 as up
import awkward1 as ak


# --Read file
infile = "/cms/scratch/syan/work/DelphesTools_1/draw_histo/no_cut/F4top_ex1_no_cut.root"
dat = up.open(infile)

# Read Tree
tree = dat['Delphes']

# Read branch and conver to array
weight = tree['Event.Weight'].array()

#Generator may have given event negative weight
inspected_event_weight = 1
if abs(weight) > 0:
    inspected_event_weight=inspected_event_weight*(weight/abs(weight))
else:
    inspected_event_weight = 0


# Draw hist
import matplotlib.pyplot as plt

plt.hist(weight.sum(), bins=20)
plt.grid()
plt.xlabel('Weight')
plt.title('Weight')
plt.show()
