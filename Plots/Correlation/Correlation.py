"""
This script produces the Figures 13 from Amaral+2021, the
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

f1 = './rgstellar.txt'
f2 = './rgflare.txt'
f3 = './stopstellar.txt'
f4 = './stopflare.txt'

star1 = np.genfromtxt(f1, usecols=0 ,unpack=True)
water1 = np.genfromtxt(f1, usecols=1 ,unpack=True)
planet1 = np.genfromtxt(f1, usecols=2 ,unpack=True)  
waterfinal1 = np.genfromtxt(f1, usecols=3 ,unpack=True)

star2 = np.genfromtxt(f2, usecols=0 ,unpack=True)
water2 = np.genfromtxt(f2, usecols=1 ,unpack=True)
planet2 = np.genfromtxt(f2, usecols=2,unpack=True)
waterfinal2 = np.genfromtxt(f2, usecols=3 ,unpack=True)

star3 = np.genfromtxt(f3, usecols=0 ,unpack=True)
water3 = np.genfromtxt(f3, usecols=1 ,unpack=True)
planet3 = np.genfromtxt(f3, usecols=2,unpack=True)
waterfinal3 = np.genfromtxt(f3, usecols=3 ,unpack=True)

star4 = np.genfromtxt(f4, usecols=0 ,unpack=True)
water4 = np.genfromtxt(f4, usecols=1 ,unpack=True)
planet4 = np.genfromtxt(f4, usecols=2,unpack=True)
waterfinal4 = np.genfromtxt(f4, usecols=3 ,unpack=True)

a1 = ((water1-waterfinal1)/water1)*100

water1.tolist()
waterfinal1.tolist()
star1.tolist()
planet1.tolist()
a1.tolist()

a2 = ((water2-waterfinal2)/water2)*100

water2.tolist()
waterfinal2.tolist()
star2.tolist()
planet2.tolist()
a2.tolist()

a3 = ((water3-waterfinal3)/water3)*100

water3.tolist()
waterfinal3.tolist()
star3.tolist()
planet3.tolist()
a3.tolist()

a4 = ((water4-waterfinal4)/water4)*100

water4.tolist()
waterfinal4.tolist()
star4.tolist()
planet4.tolist()
a4.tolist()


dataset1 = { 
    'waterfinal1':waterfinal1,
    'water1':water1,
    'star1':star1,
    'planet1':planet1,
    'A1':a1
}

dataset2= { 
    'waterfinal2':waterfinal2,
    'water2':water2,
    'star2':star2,
    'planet2':planet2,
    'A2':a2
}

dataset3 = { 
    'waterfinal3':waterfinal3,
    'water3':water3,
    'star3':star3,
    'planet3':planet3,
    'A3':a3
}

dataset4 = { 
    'waterfinal4':waterfinal4,
    'water4':water4,
    'star4':star4,
    'planet4':planet4,
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


xyz1 = np.array([star1,planet1,a1])
corr_matrix1 = np.corrcoef(xyz1).round(decimals=4)
corr_matrix1

xyz2 = np.array([star2,planet2,a2])
corr_matrix2 = np.corrcoef(xyz2).round(decimals=4)
corr_matrix2

xyz3 = np.array([star3,planet3,a3])
corr_matrix3 = np.corrcoef(xyz3).round(decimals=4)
corr_matrix3

xyz4 = np.array([star4,planet4,a4])
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


fig, ax = plt.subplots(nrows=1, ncols=4, sharey=True ,sharex=False, figsize = (16,4))

lab1 = ('stellar\nmass','planetary\nmass')

lab2 = ('planetary\nmass','H2O loss  \npercentage')

im1 = sns.heatmap(corr_matrix1[1:,:2],  ax=ax[0],cmap='RdYlBu',annot=True,cbar = False,vmin=-1,vmax=1,
           xticklabels=lab1, yticklabels=lab2)

im2 = sns.heatmap(corr_matrix2[1:,:2], ax=ax[1],cmap='RdYlBu',annot=True,cbar = False,vmin=-1,vmax=1,
           xticklabels=lab1, yticklabels=lab2)

im3 = sns.heatmap(corr_matrix3[1:,:2], ax=ax[2],cmap='RdYlBu',annot=True,cbar = False,vmin=-1,vmax=1,
           xticklabels=lab1, yticklabels=lab2)

im4 = sns.heatmap(corr_matrix4[1:,:2], ax=ax[3],cmap='RdYlBu',annot=True,cbar = False,vmin=-1,vmax=1,
           xticklabels=lab1, yticklabels=lab2, annot_kws = {'fontsize' : 30})

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

#for i in im:
 #   i.set_xticklabels(i.get_xmajorticklabels(), fontsize = 22, rotation = 90)
   # i.set_yticklabels(i.get_xmajorticklabels(), fontsize = 22,rotation = 0)



# Save figure
if (sys.argv[1] == 'pdf'):
    fig.savefig('Correlation.pdf', bbox_inches="tight", dpi=300)
if (sys.argv[1] == 'png'):
    fig.savefig('Correlation.png', bbox_inches="tight", dpi=300)
