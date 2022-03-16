"""
This script produces a reproduction of Figure 10
from Davenport+2019 (Figure 4 from Amaral+2022) ,
the flare frequency distribution of a 0.5 Msun star, 
using VPLANET's STELLAR and FLARE modules.

@autor: Laura N.  R. do Amaral, Universidad Nacional Autónoma de México, 2021
@email: laura.nevesdoamaral@gmail.com
Date: May 2021
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from math import exp, expm1, log10, log
import matplotlib.style
import seaborn as sns
from scipy.interpolate import interp1d
import matplotlib as mpl
import sys
import os
import subprocess


mpl.style.use('classic')

     

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
mpl.rcParams['font.size'] = 18.0

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



data = np.loadtxt("./FFD.star.forward")
age = data[:,0]

print(age)

Mdata = []
Ndata = []
Odata = []
Pdata = []

for idx, val in enumerate(age):
    if val == (1e6):
        Mdata = data[idx,:]
        print(Mdata[5:9])
    if val == (1e7):
        Ndata = data[idx,:]
        print(Ndata)
    if val == (1e8):
        Odata=data[idx,:]
    if val == (1e9):
        Pdata = data[idx,:]
                     

fig= plt.figure(figsize=(13,10))


fp = [1,1,1,1]
np.interp(np.log10(Mdata[5:9]), Mdata[1:5], fp)
plt.plot(np.log10(Mdata[5:9]), Mdata[1:5], '-', color = "cornflowerblue", linewidth=2.5)

np.interp(np.log10(Ndata[5:9]), Ndata[1:5], fp)
plt.plot(np.log10(Ndata[5:9]), Ndata[1:5], '-', color = "darkviolet", linewidth=2.5)

np.interp(np.log10(Odata[5:9]), Odata[1:5], fp)
plt.plot(np.log10(Odata[5:9]), Odata[1:5], '-', color = "darkred", linewidth=2.5)

np.interp(np.log10(Pdata[5:9]), Pdata[1:5], fp)
plt.plot(np.log10(Pdata[5:9]), Pdata[1:5], '-', color = "red", linewidth=2.5)




for i in range(1,5):
           plt.plot(np.log10(Mdata[i+4]), Mdata[i], color = "cornflowerblue", linewidth=2, label='t')
           plt.plot(np.log10(Ndata[i+4]), Ndata[i], color = "darkviolet", linewidth=2, label='t')
           plt.plot(np.log10(Odata[i+4]), Odata[i], color = "darkred", linewidth=2, label='t')
           plt.plot(np.log10(Pdata[i+4]), Pdata[i], color = "red", linewidth=2, label='t')                            
           
plt.yscale('log')


#plt.title('Flare Frequency Distribution', fontsize=37)  #Define el título de la gráfica 
plt.xlabel("log Flare Energy (erg)",fontsize=40)         #Define el título y el tamaño del título en X
plt.ylabel("Cumulative Flare Freq (#/day)",fontsize=40)        #Define el título y el tamaño del título en Y
plt.xticks(fontsize=40)                         #Define el tamaño de los números en el eje X
plt.yticks(fontsize=40)                         #Define el tamaño de los números en el eje Y


plt.ylim(10**(-4.02),10**(-0.5))
plt.xlim(32.85,36.15)

a = [33,34,35,36]

plt.xticks(ticks=a)
plt.locator_params(axis='x', nbins=4)


if (sys.argv[1] == 'pdf'):
    fig.savefig('FfdReproduced.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    fig.savefig('FfdReproduced.png', bbox_inches="tight", dpi=600)
