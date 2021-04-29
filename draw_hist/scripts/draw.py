import numpy as np


# --- 1. Parameter set

Lumi         = 137 * 1000;

# Signal
infile_Signal = 'FourTop_nosel.npy'
xsec_Signal   = 0.012
gen_Signal	  = 157620


# BKG HT700~1000 ( Fix me )
infile_BKG = 'QCD_HT700_nosel.npy'
xsec_BKG   = 6344.0
gen_BKG    = 502300 


# BKG HT1000~1500 ( Fix me )
infile_BKG_1 = 'QCD_HT1000_nosel.npy'
xsec_BKG_1   = 1092.0
gen_BKG_1    = 264657

# BKG HT1500~2000 ( Fix me )
infile_BKG_2 = 'QCD_HT1500_nosel.npy'
xsec_BKG_2   = 99.76
gen_BKG_2    = 456303

# BKG HT2000~Inf ( Fix me )
infile_BKG_3 = 'QCD_HT2000_nosel.npy'
xsec_BKG_3   = 20.35
gen_BKG_3    = 391581

# --- 2. Read npy files

# Signal
data_Signal = np.load(infile_Signal,allow_pickle=True)
histo_Signal = data_Signal[()]

# BKG HT700~1000
data_BKG = np.load(infile_BKG,allow_pickle=True)
histo_BKG = data_BKG[()]

# BKG HT1000~1500
data_BKG_1 = np.load(infile_BKG_1,allow_pickle=True)
histo_BKG_1 = data_BKG_1[()]

# BKG HT1500~2000
data_BKG_2 = np.load(infile_BKG_2,allow_pickle=True)
histo_BKG_2 = data_BKG_2[()]

# BKG HT2000~Inf
data_BKG_3 = np.load(infile_BKG_3,allow_pickle=True)
histo_BKG_3 = data_BKG_3[()]

# --- 3. Extract arrays

# Signal
Signal_NBtag_hist = histo_Signal['NBtag_hist']
Signal_NJet_hist = histo_Signal['NJet_hist']
Signal_HT_hist   = histo_Signal['HT_hist']
Signal_weight    = histo_Signal['weight']

# BKG HT700~1000
BKG_NBtag_hist = histo_BKG['NBtag_hist']
BKG_NJet_hist = histo_BKG['NJet_hist']
BKG_HT_hist   = histo_BKG['HT_hist']
BKG_weight    = histo_BKG['weight']

# BKG HT1000~1500
BKG_NBtag_hist_1 = histo_BKG_1['NBtag_hist']
BKG_NJet_hist_1 = histo_BKG_1['NJet_hist']
BKG_HT_hist_1   = histo_BKG_1['HT_hist']
BKG_weight_1    = histo_BKG_1['weight']

# BKG HT1500~2000
BKG_NBtag_hist_2 = histo_BKG_2['NBtag_hist']
BKG_NJet_hist_2 = histo_BKG_2['NJet_hist']
BKG_HT_hist_2   = histo_BKG_2['HT_hist']
BKG_weight_2    = histo_BKG_2['weight']

# BKG HT2000~Inf
BKG_NBtag_hist_3 = histo_BKG_3['NBtag_hist']
BKG_NJet_hist_3 = histo_BKG_3['NJet_hist']
BKG_HT_hist_3   = histo_BKG_3['HT_hist']
BKG_weight_3    = histo_BKG_3['weight']

# --- 4. Noramlize

# Signal
norm_Signal		= Lumi * xsec_Signal / gen_Signal
norm_Signal_arr = np.ones(len(Signal_HT_hist)) * norm_Signal

# BKG HT700~1000
norm_BKG		= Lumi * xsec_BKG / gen_BKG
norm_BKG_arr = np.ones(len(BKG_HT_hist)) * norm_BKG

# BKG HT1000~1500
norm_BKG_1		= Lumi * xsec_BKG_1 / gen_BKG_1
norm_BKG_arr_1 = np.ones(len(BKG_HT_hist_1)) * norm_BKG_1

# BKG HT1500~2000
norm_BKG_2		= Lumi * xsec_BKG_2 / gen_BKG_2
norm_BKG_arr_2 = np.ones(len(BKG_HT_hist_2)) * norm_BKG_2

# BKG HT2000~Inf
norm_BKG_3		= Lumi * xsec_BKG_3 / gen_BKG_3
norm_BKG_arr_3 = np.ones(len(BKG_HT_hist_3)) * norm_BKG_3

# --- 5. Draw hist
import matplotlib.pyplot as plt

a = np.concatenate((norm_BKG_arr,norm_BKG_arr_1,norm_BKG_arr_2,norm_BKG_arr_3),axis=0) # BKG normalize array combine 

b_1 = np.array(BKG_NJet_hist)
b_2 = np.array(BKG_NJet_hist_1)
b_3 = np.array(BKG_NJet_hist_2)
b_4 = np.array(BKG_NJet_hist_3)
bb = np.concatenate((b_1,b_2,b_3,b_4),axis=0) #  BKG NJet histo combine 

c_1 = np.array(BKG_NBtag_hist)
c_2 = np.array(BKG_NBtag_hist_1)
c_3 = np.array(BKG_NBtag_hist_2)
c_4 = np.array(BKG_NBtag_hist_3)
cc = np.concatenate((c_1,c_2,c_3,c_4),axis=0) # BKG NBtag histo combine

d_1 = np.array(BKG_HT_hist)
d_2 = np.array(BKG_HT_hist_1)
d_3 = np.array(BKG_HT_hist_2)
d_4 = np.array(BKG_HT_hist_3)
dd = np.concatenate((d_1,d_2,d_3,d_4),axis=0) # BKG HT histo combine

# yes-Weight

#plt.hist(Signal_NJet_hist,weights = norm_Signal_arr * Signal_weight,bins=np.linspace(0,22,23),color='royalblue',label='FourTop',) # Signal NJet
#plt.hist(Signal_NBtag_hist,weights = norm_Signal_arr * Signal_weight,bins=np.linspace(0,8,9),color='royalblue',label='FourTop') # Signal NBtag
#plt.hist(Signal_HT_hist,weights = norm_Signal_arr * Signal_weight, bins=20,range=(0,6000),color='royalblue',label='FourTop') # Signal HT

#plt.hist(Signal_NJet_hist,weights = norm_Signal_arr * Signal_weight,bins=np.linspace(0,22,23),color='royalblue',label='FourTop',histtype="step") # Signal NJet
plt.hist(Signal_NBtag_hist,weights = norm_Signal_arr * Signal_weight,bins=np.linspace(0,8,9),color='royalblue',histtype="step",label='FourTop') # Signal NBtag
#plt.hist(Signal_HT_hist,weights = norm_Signal_arr * Signal_weight, bins=20,range=(0,8000),color='royalblue',histtype="step",label='FourTop') # Signal HT

# no-Weight
# --signal
#plt.hist(Signal_NJet_hist,weights = norm_Signal_arr,bins=np.linspace(0,25,26),color='royalblue',label='FourTop') # Signal NJet
#plt.hist(Signal_NBtag_hist,weights = norm_Signal_arr * Signal_weight,bins=np.linspace(0,9,10),color='royalblue',label='FourTop') # Signal NBtag
#plt.hist(Signal_HT_hist,weights = norm_Signal_arr, bins=20,range=(0,6000)) # HT

# --BKG

#plt.hist(bb,weights = a, bins=np.linspace(0,22,23),color='darkorange',label="QCD") # BKG NJet
#plt.hist(cc,weights = a, bins=np.linspace(0,8,9),color='darkorange',label="QCD") # BKG NBtag
#plt.hist(dd,weights = a, bins=20,range=(0,8000),color='darkorange',label="QCD") # BKG HT

#plt.hist(bb,weights = a, bins=np.linspace(0,22,23),color='darkorange',histtype = 'step',label="QCD") # BKG NJet
plt.hist(cc,weights = a, bins=np.linspace(0,8,9),color='darkorange',histtype = 'step',label="QCD") # BKG NBtag
#plt.hist(dd,weights = a, bins=20,range=(0,8000),color='darkorange',histtype = 'step',label="QCD") # BKG HT


plt.title("No selection")
plt.xlabel('NBtag')
plt.ylabel("Number of events")
plt.yscale("log")
plt.legend()
plt.grid()
plt.show()



