"""
Code to generate the time in the runaway greenhouse phase of stars
between 0.2 and 0.6 Msun, Figure 7 from Amaral+2021

@autor: Laura N.  R. do Amaral, Universidad Nacional Autónoma de México, 2021
@email: laura.nevesdoamaral@gmail.com

Date: Apr. 27st, 2021

"""
import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors
import sys
import os
import itertools

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)


mpl.rcParams['figure.figsize'] = (10,6)
mpl.rcParams['font.size'] = 20
plt.rcParams['axes.facecolor']='darkseagreen'

mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 5
mpl.rcParams['ytick.major.width'] = 2

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['xtick.bottom'] = True
mpl.rcParams['ytick.right'] = True


folder = './RGphase.txt'
RGphase = np.genfromtxt(folder,unpack=True)


dirs_keys_RG = []
folders = {}

range1 = 41
range3 = 91

for i in range(0,range1):
        for j in range(0,range3):
                dirs_keys_RG.append(f'{i}_{j}')    

outputs_RGphase = dict(zip(dirs_keys_RG,RGphase))
stellar_mass = []

for i in range(20,61):
    i = 0+i*0.01
    stellar_mass.append(i)

wf = []
for ik, val in outputs_RGphase.items():
    wf.append(val)

age = []    
for i in range(0,41):
    age.append(wf[(i*91)])
    
fig, ax = plt.subplots()
plt.fill_betweenx(stellar_mass,age, interpolate=True,color = 'navajowhite', alpha = 0.99)

a = [0.5,1,1.5]

plt.xticks(ticks=a)
ax.xaxis.set_major_locator(MaxNLocator(4)) 
ax.text(0.35e8,0.38, 'Outside\n the HZ', fontsize=30, color = 'k')
plt.ylim(0.2,0.6)
plt.xlim(0,2e8)
plt.xlabel(r'Time (years)', fontsize = 25)
plt.ylabel(r'Stellar Mass (M$_{\odot}$)', fontsize = 25)

# Save figure
if (sys.argv[1] == 'pdf'):
    fig.savefig('RGphase.pdf', bbox_inches="tight", dpi=300)
if (sys.argv[1] == 'png'):
    fig.savefig('RGphase.png', bbox_inches="tight", dpi=200)
