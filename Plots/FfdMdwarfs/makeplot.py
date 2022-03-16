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
import seaborn as sns


# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)


mpl.style.use('classic')


mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 2

mpl.rcParams['xtick.minor.size'] = 7
mpl.rcParams['xtick.minor.width'] = 2
mpl.rcParams['ytick.minor.size'] = 7
mpl.rcParams['ytick.minor.width'] = 2

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['xtick.bottom'] = True
mpl.rcParams['ytick.right'] = True


mpl.rcParams['font.size'] = 57.0



M = np.genfromtxt('./FFD.star02.forward',unpack=True)
P = np.genfromtxt('./FFD.star04.forward',unpack=True)
N = np.genfromtxt('./FFD.star06.forward',unpack=True)

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
    E02_1.append(np.log10((M[i+4,0])*0.65))
    v04_1.append(P[i,0])
    E04_1.append(np.log10((P[i+4,0])*0.65))
    v06_1.append(N[i,0])
    E06_1.append(np.log10((N[i+4,0])*0.65))
    
    v02_10.append(M[i,9])
    E02_10.append(np.log10((M[i+4,9])*0.65))
    v04_10.append(P[i,9])
    E04_10.append(np.log10((P[i+4,9])*0.65))
    v06_10.append(N[i,9])
    E06_10.append(np.log10((N[i+4,9])*0.65))
       
    v02_100.append(M[i,79])
    E02_100.append(np.log10((M[i+4,79])*0.65))
    v04_100.append(P[i,79])
    E04_100.append(np.log10((P[i+4,79])*0.65))
    v06_100.append(N[i,79])
    E06_100.append(np.log10((N[i+4,79])*0.65))
    
    v02_1000.append(M[i,999])
    E02_1000.append(np.log10((M[i+4,999])*0.65))
    v04_1000.append(P[i,999])
    E04_1000.append(np.log10((P[i+4,999])*0.65))
    v06_1000.append(N[i,999])
    E06_1000.append(np.log10((N[i+4,999])*0.65))

R = [0,0,0.26,0.39,0.44,0.49,0.62]
T = [0,0,3100,3250,3400,3600,3800]
prebio = {}
E = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10**33,10**34,10**35,10**36]
EE ={}
i=0
j=0


path = ['./age/FFD.star02.forward','./age/FFD.star04.forward','./age/FFD.star06.forward']

                
time = []
age = []
ffd = []
energy = []              

      


for i in range(0,3):
    time.append(np.genfromtxt(path[i],usecols = (0),unpack=True))
    age.append(np.genfromtxt(path[i],usecols = (1),unpack=True))
    ffd.append(np.genfromtxt(path[i],usecols = (3),unpack=True))
    energy.append(np.genfromtxt(path[i],usecols = (5),unpack=True))


    
cmap = ['#FFC107','#1E88E5','#D81B60']         


fig, ax = plt.subplots(figsize=(26,10), nrows=1, ncols=2)
fp = [1,1,1,1]



np.interp(E06_1,v06_1, fp)
ax[1].plot(E06_1, v06_1, '-', color = cmap[0], linewidth=7)#, label='1 Myr')

np.interp(E06_10,v06_10, fp)
ax[1].plot(E06_10, v06_10, '--', color = cmap[0], linewidth=7)#, label='10 Myr')

np.interp(E06_100,v06_100, fp)
ax[1].plot(E06_100, v06_100, ':', color = cmap[0],linewidth=7)#, label='100 Myr')

np.interp(E06_1000,v06_1000, fp)
ax[1].plot(E06_1000, v06_1000, '-.', color = cmap[0], linewidth=7)#, label='1 Gyr')


np.interp(E04_1,v04_1, fp)
ax[1].plot(E04_1, v04_1, '-',color = cmap[1], linewidth=4)#, label='1 Myr')

np.interp(E04_10,v04_10, fp)
ax[1].plot(E04_10, v04_10, '--',color = cmap[1], linewidth=4)#, label='10 Myr')

np.interp(E04_100,v04_100, fp)
ax[1].plot(E04_100, v04_100, ':', color = cmap[1], linewidth=4)#, label='100 Myr')

np.interp(E04_1000,v04_1000, fp)
ax[1].plot(E04_1000, v04_1000, '-.',color = cmap[1], linewidth=4)#, label='1 Gyr')


np.interp(E02_1,v02_1, fp)
ax[1].plot(E02_1, v02_1, '-', color = cmap[2], linewidth=1.5)#, label='1 Myr')

np.interp(E02_10,v02_10, fp)
ax[1].plot(E02_10, v02_10, '--', color = cmap[2], linewidth=1.5)#, label='10 Myr')

np.interp(E02_100,v02_100, fp)
ax[1].plot(E02_100, v02_100, ':',color = cmap[2],linewidth=1.5)#, label='100 Myr')

np.interp(E02_1000,v02_1000, fp)
ax[1].plot(E02_1000, v02_1000, '-.',color = cmap[2], linewidth=1.5)#, label='1 Gyr')


for i in range(0,4):
    ax[1].plot( E06_1[i], v06_1[i], color = cmap[0],linewidth=7)
    ax[1].plot( E06_10[i], v06_10[i], color = cmap[0], linewidth=7)
    ax[1].plot( E06_100[i], v06_100[i], color = cmap[0], linewidth=7)
    ax[1].plot( E06_1000[i], v06_1000[i], color = cmap[0], linewidth=7)

    ax[1].plot( E04_1[i], v04_1[i], color = cmap[1], linewidth=4)
    ax[1].plot( E04_10[i], v04_10[i], color = cmap[1], linewidth=4)
    ax[1].plot( E04_100[i], v04_100[i], color = cmap[1], linewidth=4)
    ax[1].plot( E04_1000[i], v04_1000[i], color = cmap[1], linewidth=4)
      
    ax[1].plot( E02_1[i], v02_1[i],color = cmap[2], linewidth=1.5)
    ax[1].plot( E02_10[i], v02_10[i],color = cmap[2],  linewidth=1.5)
    ax[1].plot( E02_100[i], v02_100[i],color = cmap[2],  linewidth=1.5)
    ax[1].plot( E02_1000[i], v02_1000[i],color = cmap[2],  linewidth=1.5)

EE1 = [10**33,10**34,10**35,10**36]
EE = []
EE0 = [33,34,35,36]




for i in range(0,4):
        EE.append(np.log10(EE1[i]*0.65))

cmap2 = ['#D81B60','#1E88E5','#FFC107'] 

lwi = [1.5,4,7]

for i in range(0,3):
    ax[0].plot(age[i], ffd[i], color = cmap2[i],linewidth= lwi[i])
 
ax[0].set_xscale('symlog')
ax[0].set_yscale('log')

ax[0].set_xlim(1e6,1e9)


ax[0].set_yscale('log')  
ax[0].set_xlabel(r'Stellar Age (yr)',fontsize=40)        
ax[0].set_ylabel("Cumulative Flare Freq (#/day)",fontsize=37)       


plt.legend()
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0],color = cmap2[0], lw=1.5, label=r'0.2 M$_{\odot}$'),
                   Line2D([0], [0], color= cmap2[1], lw=4, label=r'0.4 M$_{\odot}$'),
                   Line2D([0], [0], color = cmap2[2], lw=7, label=r'0.6 M$_{\odot}$')
]

ax[0].legend(handles=legend_elements, ncol=1,loc='lower left', fontsize = 35)

legend_elements = [Line2D([0], [0], ls='-', color='black', lw=4,label='1 Myr'),
                   Line2D([0], [0], ls='--', color='black',lw=4, label='10 Myr'),
                   Line2D([0], [0], ls=':', color='black', lw=4,label='100 Myr'),
                   Line2D([0], [0], ls='-.', color='black', lw=4,label='1 Gyr')
]

ax[1].legend(handles=legend_elements, ncol=2,loc='lower left', fontsize = 35)

fig.text(0.35, 0.78,r'AD Leo Great Flare'' \nlog Energy$_{Kepler}$ = 33.42', ha='center',  fontsize = 37)
ax[1].set_yscale('log')
fig.text(0.725, 0.99,r'log Energy$_{kepler}$ (erg)', ha='center',  fontsize = 37)
ax[1].set_xlabel(r'log Energy$_{UV}$ (erg)',fontsize=40)        
                        
fig.patch.set_facecolor('xkcd:white')
ax[1].set_ylim(10**(-4.5),10**(0.2))
ax[1].set_xlim(32.81291335664285,35.81291335664285)
ax[0].set_ylim(10**(-2),10**(-0.4))

axis_2 =plt.twiny()
axis_2.plot(EE0,v06_1, color = cmap[0])

for label in axis_2.xaxis.get_majorticklabels():
        label.set_fontsize(42)

for ax in ax.flatten():
    for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(42)
fig.subplots_adjust(left = 0.050,bottom=0.045, right=0.95, top=0.91, wspace = 0.12, hspace =0.08 )   

fig.text(0.055, 0.99,r'a', ha='center',  fontsize = 57)
fig.text(0.53, 0.99,r'b', ha='center',  fontsize = 57)



   
        
if (sys.argv[1] == 'pdf'):
	fig.savefig('FfdMdwarfs.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
	fig.savefig('FfdMdwarfs.png', bbox_inches="tight", dpi=600)    
