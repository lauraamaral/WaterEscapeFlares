"""

Code to generate folders with different semi major axis to which stellar mass

@author: Laura Neves Ribeiro do Amaral
@email: laura.nevesdoamaral(at)gmail(dot)com

Date: Oct. 7st, 2020

"""
import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)

folder_name1_star = './HabZone/star'
range_1 = 19
folders_stellar = []
folders_b = []

for i in range(0,range_1):
     folders_stellar.append(folder_name1_star + "{:02d}".format(i) + '/flare.star.forward')
     folders_b.append(folder_name1_star + "{:02d}".format(i) + '/flare.b.forward')
     
_HZLimRunaway = []
_HZLimMaxGreenhouse = []
_HZLimEarlyMars = []
_HZLimRecVenus = []

for i in range(0,19):
    _HZLimRunaway.append(np.genfromtxt(folders_stellar[i],usecols = (2),unpack=True))
    _HZLimMaxGreenhouse.append(np.genfromtxt(folders_stellar[i],usecols = (3),unpack=True))
    _HZLimEarlyMars.append(np.genfromtxt(folders_stellar[i],usecols = (5),unpack=True))
    _HZLimRecVenus.append(np.genfromtxt(folders_stellar[i],usecols = (4),unpack=True))

HZLimRunaway = []
HZLimMaxGreenhouse = []
HZLimEarlyMars = []
HZLimRecVenus = []

for i in range(0,19):
    HZLimRunaway.append(_HZLimRunaway[i][0])
    HZLimMaxGreenhouse.append(_HZLimMaxGreenhouse[i][0])
    HZLimEarlyMars.append(_HZLimEarlyMars[i][0])
    HZLimRecVenus.append(_HZLimRecVenus[i][0])

    
Masses = [0.175,0.2,0.225,0.25,0.275,0.3,0.325,0.35,0.375,0.4,0.425,0.45,0.475,0.5,0.525,0.55,0.575,0.6,0.625]
    
    
fig, ax = plt.subplots(figsize=(16, 9))


A = HZLimRecVenus
B = HZLimRunaway
C = HZLimEarlyMars
D = HZLimMaxGreenhouse


plt.rcParams['axes.facecolor']='snow'
plt.rcParams['savefig.facecolor']='snow'


plt.fill_betweenx(Masses,B,D, color='skyblue',alpha = 0.6)
plt.fill_betweenx(Masses,A,B, color='gold',alpha = 0.4)
plt.fill_betweenx(Masses,C,D, color='gold',alpha = 0.4)


plt.plot(A, Masses, color = 'red',ls = '--',lw = 4, label = 'Recent Venus')
plt.plot(B, Masses,color = 'royalblue', ls = '-.', lw = 4,label = 'Runaway Greenhouse')
plt.plot(D, Masses,color = 'darkblue', lw = 4, label = 'Max Greenhouse')
plt.plot(C, Masses,color = 'orange',ls = ':', lw = 6, label = 'Early Mars')


ax.annotate('K2-72 e', xy=(0.106,0.271), xytext=(0.12,0.271), color='k',fontsize = 20)
ax.annotate('TOI-700 d', xy=(0.1633,0.415), xytext=(0.1733,0.420), color='k',fontsize = 20)
ax.annotate('Kepler 1649 c', xy=(0.249,0.1977), xytext=(0.0919,0.1977), color='k',fontsize = 20)
ax.annotate('Kepler-1229 b', xy=(0.1654,0.404), xytext=(0.1854,0.490), color='k',fontsize = 20)

ax.scatter(0.3006,0.480,marker= 'o', edgecolor = 'white',color = 'red', s = 305, label= 'Kepler-1229 b')
ax.scatter(0.106,0.271365,marker= 's', edgecolor = 'white',color = 'limegreen', s = 305, label= 'K2-72 e')
ax.scatter(0.1633,0.415,marker= '*', edgecolor = 'white',color = 'cornflowerblue', s = 605, label= 'TOI-700 d')
ax.scatter(0.0827,0.1977,marker= '^', edgecolor = 'white',color = 'gold',s = 305, label= 'Kepler 1649 c')

ax.scatter(0.1754613044514601,0.480,marker= 'o', edgecolor = 'white',color = 'darkred', s = 305)
ax.scatter(0.09099465169519186,0.271365,marker= 's', edgecolor = 'white',color = 'darkgreen', s = 305)
ax.scatter(0.144602097135456,0.415,marker= '*', edgecolor = 'white',color = 'midnightblue', s = 605)
ax.scatter(0.0677858585735443,0.1977,marker= '^', edgecolor = 'white',color = 'darkgoldenrod',s = 305)

plt.xlabel('Distance from star (AU)', fontsize=30)
plt.ylabel(r'Stellar Mass (M$_{\odot}$)',fontsize=30)

legend_elements = [Line2D([0], [0], marker= 'o',markersize=20, markerfacecolor="red", color = 'white', lw=0, label='Kepler-1229 b Actual Semi-major axis'),
                   Line2D([0], [0], marker= 's', markersize=20, markerfacecolor="limegreen",color = 'white', lw=0, label='K2-72 e Actual Semi-major axis'),
                   Line2D([0], [0], marker= '*',markersize=26, markerfacecolor="cornflowerblue", color = 'white', lw=0, label='TOI-700 d Actual Semi-major axis'),
                   Line2D([0], [0], marker= '^', markersize=20, markerfacecolor="gold",color = 'white', lw=0, label='Kepler-1649 c Actual Semi-major axis'),
                 
                   Line2D([0], [0], marker= 'o',markersize=20, markerfacecolor="darkred", color = 'white', lw=0, label='Kepler-1229 b Modified Semi-major axis'),
                   Line2D([0], [0], marker= 's', markersize=20, markerfacecolor="darkgreen",color = 'white', lw=0, label='K2-72 e Modified Semi-major axis'),
                   Line2D([0], [0], marker= '*',markersize=26, markerfacecolor="midnightblue", color = 'white', lw=0, label='TOI-700 d Modified Semi-major axis'),
                   Line2D([0], [0], marker= '^', markersize=20, markerfacecolor="darkgoldenrod",color = 'white', lw=0, label='Kepler-1649 c Modified Semi-major axis'),
                         
                   Line2D([0], [0], color = 'red',ls = '--', lw=4, label = 'Recent Venus HZ limit'),
                   Line2D([0], [0], color = 'royalblue', ls = '-.',lw=3.5,label = 'Runaway Greenhouse HZ limit'),
                   Line2D([0], [0], color = 'darkblue', lw=4,label = 'Maximum Greenhouse HZ limit'),
                   Line2D([0], [0], color = 'orange',ls = ':', lw=6,label = 'Early Mars HZ limit')
]


ax.tick_params(labelsize=30)

plt.xlim(0,0.7)
plt.ylim(0.19,0.61)
ax.legend(handles=legend_elements, loc='lower right', fontsize=17.5,ncol=1)

# Save figure
if (sys.argv[1] == 'pdf'):
    fig.savefig('HZ.pdf', bbox_inches="tight", dpi=400)
if (sys.argv[1] == 'png'):
    fig.savefig('HZ.png', bbox_inches="tight", dpi=250)
