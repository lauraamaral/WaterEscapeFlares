"""
This script produces the Figures 11 from Amaral+2021, the
pearson correlation between stellar and planetary mass and 
surface water loss percentage.

@autor: Laura N.  R. do Amaral, Universidad Nacional Autónoma de México, 2021
@email: laura.nevesdoamaral@gmail.com
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import pandas as pd
import statsmodels as st
import seaborn as sns
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from collections import OrderedDict
import sys
import os
import subprocess
plt.style.use('ggplot')



f1 = './dataframe1.txt'
f2 = './dataframe2.txt'
f3 = './dataframe3.txt'
f4 = './dataframe4.txt'

w1 = np.genfromtxt(f1, usecols=1 ,unpack=True)
x1 = np.genfromtxt(f1, usecols=3 ,unpack=True)  
y1 = np.genfromtxt(f1, usecols=0 ,unpack=True)
z1 = np.genfromtxt(f1, usecols=2 ,unpack=True)

w2 = np.genfromtxt(f2, usecols=1 ,unpack=True)
x2 = np.genfromtxt(f2, usecols=3 ,unpack=True)
y2 = np.genfromtxt(f2, usecols=0 ,unpack=True)
z2 = np.genfromtxt(f2, usecols=2 ,unpack=True)

w3 = np.genfromtxt(f3, usecols=1 ,unpack=True)
x3 = np.genfromtxt(f3, usecols=3 ,unpack=True)
y3 = np.genfromtxt(f3, usecols=0 ,unpack=True)
z3 = np.genfromtxt(f3, usecols=2 ,unpack=True)

w4 = np.genfromtxt(f4, usecols=1 ,unpack=True)
x4 = np.genfromtxt(f4, usecols=3 ,unpack=True)
y4 = np.genfromtxt(f4, usecols=0 ,unpack=True)
z4 = np.genfromtxt(f4, usecols=2 ,unpack=True)

a1 = ((w1-x1)/w1)*100

w1.tolist()
x1.tolist()
y1.tolist()
z1.tolist()
a1.tolist()

a2 = ((w2-x2)/w2)*100

w2.tolist()
x2.tolist()
y2.tolist()
z2.tolist()
a2.tolist()

a3 = ((w3-x3)/w3)*100

w3.tolist()
x3.tolist()
y3.tolist()
z3.tolist()
a3.tolist()

a4 = ((w4-x4)/w4)*100

w4.tolist()
x4.tolist()
y4.tolist()
z4.tolist()
a4.tolist()


dataset1 = { 
    'W1':w1,
    'X1':x1,
    'Y1':y1,
    'Z1':z1,
    'A1':a1
}

dataset2= { 
    'W2':w2,
    'X2':x2,
    'Y2':y2,
    'Z2':z2,
    'A2':a2
}

dataset3 = { 
    'W3':w3,
    'X3':x3,
    'Y3':y3,
    'Z3':z3,
    'A3':a3
}

dataset4 = { 
    'W4':w4,
    'X4':x4,
    'Y4':y4,
    'Z4':z4,
    'A4':a4
}

dataset1 = pd.DataFrame(dataset1)
dataset2 = pd.DataFrame(dataset2)
dataset3 = pd.DataFrame(dataset3)
dataset4 = pd.DataFrame(dataset4)

dataset1.corr()
dataset2.corr()
dataset3.corr()
dataset4.corr()


xyz1 = np.array([y1,z1,a1])
corr_matrix1 = np.corrcoef(xyz1).round(decimals=4)
corr_matrix1

xyz2 = np.array([y2,z2,a2])
corr_matrix2 = np.corrcoef(xyz2).round(decimals=4)
corr_matrix2

xyz3 = np.array([y3,z3,a3])
corr_matrix3 = np.corrcoef(xyz3).round(decimals=4)
corr_matrix3

xyz4 = np.array([y4,z4,a4])
corr_matrix4 = np.corrcoef(xyz4).round(decimals=4)
corr_matrix4

mpl.rcParams['xtick.major.size'] = 7
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 7
mpl.rcParams['ytick.major.width'] = 2

mpl.rcParams['xtick.minor.size'] = 5
mpl.rcParams['xtick.minor.width'] = 2
mpl.rcParams['ytick.minor.size'] = 5
mpl.rcParams['ytick.minor.width'] = 2

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['xtick.bottom'] = True
mpl.rcParams['ytick.right'] = True

mpl.rcParams['font.size'] = 30

fig, ax = plt.subplots(nrows=1, ncols=4, sharey=True ,sharex=True, figsize = (16,4))

lab = ('stellar\nmass', 'planetary\nmass', 'H2O loss  \npercentage')

im1 = sns.heatmap(corr_matrix1, ax=ax[0],cmap='RdYlBu',annot=True,cbar = False,vmin=-1,vmax=1,
           xticklabels=lab, yticklabels=lab)

im2 = sns.heatmap(corr_matrix2, ax=ax[1],cmap='RdYlBu',annot=True,cbar = False,vmin=-1,vmax=1,
           xticklabels=lab, yticklabels=lab)

im3 = sns.heatmap(corr_matrix3, ax=ax[2],cmap='RdYlBu',annot=True,cbar = False,vmin=-1,vmax=1,
           xticklabels=lab, yticklabels=lab)

im4 = sns.heatmap(corr_matrix4, ax=ax[3],cmap='RdYlBu',annot=True,cbar = False,vmin=-1,vmax=1,
           xticklabels=lab, yticklabels=lab, annot_kws = {'fontsize' : 30})

cbar_ax = fig.add_axes([0.96, 0.07, 0.03, 0.853])


fig.subplots_adjust(left = 0.050,bottom=0.07, right=0.95, top=0.91, wspace = 0.05, hspace =-0.52 )

mappable = im1.get_children()[0]

fig.colorbar(mappable, cax=cbar_ax, orientation = 'vertical')
cbar_ax.tick_params(labelsize=22)
ax[0].set_title('a. STELLAR \n RG phase 1 Gyr', fontsize = 24)
ax[1].set_title('b. STELLAR + FLARE\n RG phase 1 Gyr', fontsize = 24)
ax[2].set_title('c. STELLAR\n RG phase during PMS', fontsize = 24)
ax[3].set_title('d. STELLAR + FLARE\n RG phase during PMS', fontsize =24)

im = [im1,im2,im3,im4]

for i in im:
    i.set_xticklabels(i.get_xmajorticklabels(), fontsize = 22, rotation = 90)
    i.set_yticklabels(i.get_xmajorticklabels(), fontsize = 22,rotation = 0)

# Save figure
if (sys.argv[1] == 'pdf'):
    fig.savefig('Correlation.pdf', bbox_inches="tight", dpi=300)
if (sys.argv[1] == 'png'):
    fig.savefig('Correlation.png', bbox_inches="tight", dpi=300)
