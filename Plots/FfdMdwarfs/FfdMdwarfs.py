"""
This script produces the Figures 6 from Amaral+2021, the
Flare frequency distribution of the M dwarf stars between 0.2 and 0.6 Msun
simulated in this work, using VPLANET's STELLAR and FLARE modules.

Laura N. R. do Amaral, Universidad Nacional Autónoma de México, 2021
Date:  July 22th 2021
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from math import exp, expm1, log10, log
import matplotlib.style
import matplotlib as mpl
from scipy.interpolate import interp1d
import sys
import os
import subprocess

try:
    import vplot as vpl
except:
    print('Cannot import vplot. Please install vplot.')

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)

#Typical plot parameters that make for pretty plot
mpl.rcParams['figure.figsize'] = (7,10)
mpl.rcParams['font.size'] = 25.0

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

mpl.style.use('classic')


M = np.genfromtxt('./FFD02.star02.forward',unpack=True)
P = np.genfromtxt('./FFD04.star04.forward',unpack=True)
N = np.genfromtxt('./FFD06.star06.forward',unpack=True)

E02_1 = []
v02_1 = []
E02_10 = []
v02_10 = []
E02_100 = []
v02_100 = []
E02_1000 = []
v02_1000 = []

E04_1 = []
v04_1 = []
E04_10 = []
v04_10 = []
E04_100 = []
v04_100 = []
E04_1000 = []
v04_1000 = []

E06_1 = []
v06_1 = []
E06_10 = []
v06_10 = []
E06_100 = []
v06_100 = []
E06_1000 = []
v06_1000 = []

for i in range(1,5):
    v02_1.append(M[i,0])
    E02_1.append(np.log10((10**(M[i+6,0]))*0.65))
    v04_1.append(P[i,0])
    E04_1.append(np.log10((10**(P[i+6,0]))*0.65))
    v06_1.append(N[i,0])
    E06_1.append(np.log10((10**(N[i+6,0]))*0.65))
    
    v02_10.append(M[i,9])
    E02_10.append(np.log10((10**(M[i+6,9]))*0.65))
    v04_10.append(P[i,9])
    E04_10.append(np.log10((10**(P[i+6,9]))*0.65))
    v06_10.append(N[i,9])
    E06_10.append(np.log10((10**(N[i+6,9]))*0.65))
       
    v02_100.append(M[i,79])
    E02_100.append(np.log10((10**(M[i+6,79]))*0.65))
    v04_100.append(P[i,79])
    E04_100.append(np.log10((10**(P[i+6,79]))*0.65))
    v06_100.append(N[i,79])
    E06_100.append(np.log10((10**(N[i+6,79]))*0.65))
    
    v02_1000.append(M[i,999])
    E02_1000.append(np.log10((10**(M[i+6,999]))*0.65))
    v04_1000.append(P[i,999])
    E04_1000.append(np.log10((10**(P[i+6,999]))*0.65))
    v06_1000.append(N[i,999])
    E06_1000.append(np.log10((10**(N[i+6,999]))*0.65))

R = [0,0,0.26,0.39,0.44,0.49,0.62]
T = [0,0,3100,3250,3400,3600,3800]
prebio = {}
E = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10**33,10**34,10**35,10**36]#,10**37,10**38] 

EE ={}
i=0
j=0

VV_02 = []
VV_04 = []
VV_06 = []


A =[]
for i in range(33,37):
    for j in range(2,7):
            prebio[f'{i}_{j}']=(25.5*((10**34)/((E[i])*0.65))*(R[j]**2)*((T[j]/5772)**4))
            EE[f'{i}_{j}']=np.log10(E[i]*0.65)
            if j==2:
                VV_02.append((25.5*((10**34)/((E[i])*0.65))*(R[j]**2)*((T[j]/5772)**4)))
            if j==4:
                VV_04.append((25.5*((10**34)/((E[i])*0.65))*(R[j]**2)*((T[j]/5772)**4)))
            if j==6:
                VV_06.append((25.5*((10**34)/((E[i])*0.65))*(R[j]**2)*((T[j]/5772)**4)))

import seaborn as sns
cmap = ['coral','lightseagreen','darkslateblue']         
fig= plt.figure(figsize=(13,10))


fp = [1,1,1,1]



np.interp(E06_1,v06_1, fp)
plt.plot(E06_1, v06_1, '-', color = cmap[0], linewidth=7)#, label='1 Myr')

np.interp(E06_10,v06_10, fp)
plt.plot(E06_10, v06_10, '--', color = cmap[0], linewidth=7)#, label='10 Myr')

np.interp(E06_100,v06_100, fp)
plt.plot(E06_100, v06_100, ':', color = cmap[0],linewidth=7)#, label='100 Myr')

np.interp(E06_1000,v06_1000, fp)
plt.plot(E06_1000, v06_1000, '-.', color = cmap[0], linewidth=7)#, label='1 Gyr')


np.interp(E04_1,v04_1, fp)
plt.plot(E04_1, v04_1, '-',color = cmap[1], linewidth=4)#, label='1 Myr')

np.interp(E04_10,v04_10, fp)
plt.plot(E04_10, v04_10, '--',color = cmap[1], linewidth=4)#, label='10 Myr')

np.interp(E04_100,v04_100, fp)
plt.plot(E04_100, v04_100, ':', color = cmap[1], linewidth=4)#, label='100 Myr')

np.interp(E04_1000,v04_1000, fp)
plt.plot(E04_1000, v04_1000, '-.',color = cmap[1], linewidth=4)#, label='1 Gyr')


np.interp(E02_1,v02_1, fp)
plt.plot(E02_1, v02_1, '-', color = cmap[2], linewidth=1.5)#, label='1 Myr')

np.interp(E02_10,v02_10, fp)
plt.plot(E02_10, v02_10, '--', color = cmap[2], linewidth=1.5)#, label='10 Myr')

np.interp(E02_100,v02_100, fp)
plt.plot(E02_100, v02_100, ':',color = cmap[2],linewidth=1.5)#, label='100 Myr')

np.interp(E02_1000,v02_1000, fp)
plt.plot(E02_1000, v02_1000, '-.',color = cmap[2], linewidth=1.5)#, label='1 Gyr')


for i in range(0,4):
    plt.plot( E06_1[i], v06_1[i], color = cmap[0],linewidth=7)
    plt.plot( E06_10[i], v06_10[i], color = cmap[0], linewidth=7)
    plt.plot( E06_100[i], v06_100[i], color = cmap[0], linewidth=7)
    plt.plot( E06_1000[i], v06_1000[i], color = cmap[0], linewidth=7)

    plt.plot( E04_1[i], v04_1[i], color = cmap[1], linewidth=4)
    plt.plot( E04_10[i], v04_10[i], color = cmap[1], linewidth=4)
    plt.plot( E04_100[i], v04_100[i], color = cmap[1], linewidth=4)
    plt.plot( E04_1000[i], v04_1000[i], color = cmap[1], linewidth=4)
      
    plt.plot( E02_1[i], v02_1[i],color = cmap[2], linewidth=1.5)
    plt.plot( E02_10[i], v02_10[i],color = cmap[2],  linewidth=1.5)
    plt.plot( E02_100[i], v02_100[i],color = cmap[2],  linewidth=1.5)
    plt.plot( E02_1000[i], v02_1000[i],color = cmap[2],  linewidth=1.5)

EE1 = [10**33,10**34,10**35,10**36]#,10**37,10**38]
EE = []
EE0 = [33,34,35,36]




for i in range(0,4):
        EE.append(np.log10(EE1[i]*0.65))


plt.fill_between(EE, VV_02, 50, interpolate=False, color=cmap[2],alpha = 0.9)
plt.fill_between(EE, VV_04, 50, interpolate=False, color=cmap[1],alpha = 0.9)
plt.fill_between(EE, VV_06, 50, interpolate=True, color=cmap[0],alpha = 0.9)
plt.legend()
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], ls='-', color='black', lw=3,label='1 Myr'),
                   Line2D([0], [0], ls='--', color='black',lw=3, label='10 Myr'),
                   Line2D([0], [0], ls=':', color='black', lw=3,label='100 Myr'),
                   Line2D([0], [0], ls='-.', color='black', lw=3,label='1 Gyr'),
                   Line2D([0], [0],color = cmap[2], lw=1.5, label=r'0.2 M$_{\odot}$'),
                   Line2D([0], [0], color= cmap[1], lw=4, label=r'0.4 M$_{\odot}$'),
                   Line2D([0], [0], color = cmap[0], lw=6, label=r'0.6 M$_{\odot}$')
]

plt.legend(handles=legend_elements, ncol=2,loc='lower left', fontsize = 24)


plt.yscale('log')
plt.title(r'log Energy$_{kepler}$ (erg)', fontsize=37)  
plt.xlabel(r'log Energy$_{UV}$ (erg)',fontsize=40)        
plt.ylabel("Cumulative Flare Freq (#/day)",fontsize=40)        
plt.xticks(fontsize=30)                         
plt.yticks(fontsize=30)                         
fig.patch.set_facecolor('xkcd:white')
plt.ylim(10**(-5.5),10**(1.5))
plt.xlim(32.81291335664285,35.81291335664285)

axis_2 =plt.twiny()
axis_2.plot(EE0,v06_1, color = cmap[0])

for label in axis_2.xaxis.get_majorticklabels():
        label.set_fontsize(30)

if (sys.argv[1] == 'pdf'):
    fig.savefig('FfdPreBioChem.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    fig.savefig('FfdPreBioChem.png', bbox_inches="tight", dpi=600)
