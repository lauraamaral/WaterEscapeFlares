"""
Script to make the Figure 12 of Amaral et al. 2021 paper  and
Code to run the simulations of the four known
planets show in the Figure 12 of Amaral et al. 2021 paper.

@author: Laura Neves Ribeiro do Amaral
@email: laura.nevesdoamaral(at)gmail(dot)com

Date: Oct. 7st, 2020

"""
import io
import matplotlib as mpl
import matplotlib.pyplot as plt
import vplot as vpl
import numpy as np
import sys
import os
import subprocess
import multiprocessing as mp
from multiprocessing import Pool 
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable
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


home= input("What is the directory that the folder WaterEscapeFlares is placed? Ex: /home/helena/Documents/WaterEscapeFlares ")
print(home)              
              
########################################################
############LOADING DATA #################################              
########################################################              




direc = ["Kepler-1229-b","K2-72-e","TOI-700-d","Kepler-1649-c","Kepler-1229-b","K2-72-e","TOI-700-d","Kepler-1649-c","Kepler-1229-b","K2-72-e","TOI-700-d","Kepler-1649-c","Kepler-1229-b","K2-72-e","TOI-700-d","Kepler-1649-c"]
inside = ["flare_water0","flare_water0","flare_water0","flare_water0","flare_water1","flare_water1","flare_water1","flare_water1","stellar_water0","stellar_water0","stellar_water0","stellar_water0","stellar_water1","stellar_water1","stellar_water1","stellar_water1"]

dirs_mod = []
dirs_actual = []
for i in range(0,16):
        dirs_mod.append('./RealPlanets/modified/'+direc[i]+'/'+inside[i])
        dirs_actual.append('./RealPlanets/actual/'+direc[i]+'/'+inside[i])

print(dirs_mod)

planets = ["./RunPosition/Kepler-1229-b","./RunPosition/K2-72-e","./RunPosition/TOI-700-d","./RunPosition/Kepler-1649-c"]

# Run the simulations
dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

print(1)

def run_vplanet(dir):
         print("\nRunning simulation in %s directory..." % dir)
         os.chdir(dir)
         subprocess.call(['vplanet', 'vpl.in'])
         # Return to top-level directory
         os.chdir(dir_path)
         return dir 

print("Parallelizing")

print(2)
pool = mp.Pool(mp.cpu_count())
print(pool)

results = [pool.map(run_vplanet,[i for i in planets])]

pool.close()

#Enter in the folder to calculate the semi major axis value
semi_mod = []

print(dir)

for dir in planets:
             os.chdir(dir)
             print(dir)
             folder = './system.planet.forward'
             A = np.genfromtxt(folder, usecols=2, unpack=True)
             print(A)
             HZ_RG = A[-1]
             d = HZ_RG*1.052631579
             semi_mod.append(d)
             os.chdir(dir_path)

             
semi_mod = semi_mod*4             
print(semi_mod)

semi_actual = [0.3006,0.106,0.1633,0.0827,0.3006,0.106,0.1633,0.0827,0.3006,0.106,0.1633,0.0827,0.3006,0.106,0.1633,0.0827]
semi_dirs_mod = []
semi_dirs_actual = []
print(4)

for i in range(len(semi_mod)):
                     semi_dirs_mod.append((semi_mod[i],dirs_mod[i]))
                     semi_dirs_actual.append((semi_actual[i],dirs_actual[i]))    
print(semi_dirs_mod)

print('Writting the semi major axis values in the .in files')
for i in semi_dirs_mod:
                    os.chdir(i[1])
                    f = open('b.in', 'r') 
                    list_of_lines = f.readlines()
                    list_of_lines[9]= "dSemi                        -"+ str(i[0]) +" # Semi-major axis, negative -> AU\n"
                    list_of_lines[10]="                                                 \n"
                    list_of_lines[27]="                                                 \n"
                    list_of_lines[28]= "saOutputOrder Time Age XO -SurfWaterMass -EnvelopeMass -OxygenMass -PlanetRadius -HZLimRunaway -HZlimMaxGreenhouse -HZLimRecVenus -HZLimEarlyMars -FXUV -Instellation -RGLimit"
                    f = open('b.in', 'w+')       
                    f.writelines(list_of_lines)
                    f.close()
                    os.chdir(dir_path)

for i in semi_dirs_actual:
                    os.chdir(i[1])
                    f = open('b.in', 'r') 
                    list_of_lines = f.readlines()
                    list_of_lines[9]= "dSemi                        -"+ str(i[0]) +" # Semi-major axis, negative -> AU\n"
                    list_of_lines[10]="                                                 \n"
                    list_of_lines[27]="                                                 \n"
                    list_of_lines[28]= "saOutputOrder Time Age XO -SurfWaterMass -EnvelopeMass -OxygenMass -PlanetRadius -HZLimRunaway -HZlimMaxGreenhouse -HZLimRecVenus -HZLimEarlyMars -FXUV -Instellation -RGLimit"
                    f = open('b.in', 'w+')       
                    f.writelines(list_of_lines)
                    f.close()
                    os.chdir(dir_path)

directory = dirs_mod+dirs_actual

def run_vplanet(dir):
         print("\nRunning simulation in %s directory..." % dir)
         os.chdir(dir)
         subprocess.call(['vplanet', 'vpl.in'])
         # Return to top-level directory
         os.chdir(dir_path)
         return dir 

print("Parallelizing")


pool = mp.Pool(mp.cpu_count())
print(pool)

results = [pool.map(run_vplanet,[i for i in directory])]

pool.close()

print(results)

#home = '/home/laura/Documentos/WaterEscapeFlares'

path = [home+'/Plots/RealPlanets/RealPlanetsSimulation/RealPlanets/actual/',home+'/Plots/RealPlanets/RealPlanetsSimulation/RealPlanets/modified/']

print(path)

dir_names = ['Kepler-1229-b/','K2-72-e/','TOI-700-d/','Kepler-1649-c/']
dir_folder = ['stellar_water0/','stellar_water1/','flare_water0/','flare_water1/']
dir_b = ['flare.b.forward']
dir_star = ['flare.star.forward']
direc_planets = []
direc_stars = []
for i in dir_names:
    for h in path:
        for j in dir_folder:
            for k in dir_b:
                direc_planets.append(f'{h+i+j+k}')
for i in dir_names:
    for h in path:
        for j in dir_folder:
            for k in dir_star:
                direc_stars.append(f'{h+i+j+k}')           
                
                
_1229time = []
_72time = []
_700time = []
_1649time = []

_1229Luminosity = []
_72Luminosity = []
_700Luminosity = []
_1649Luminosity = []

_1229LXUVTot = []
_72LXUVTot = []
_700LXUVTot = []
_1649LXUVTot = []        

                
_1229SurfWaterMass = []
_72SurfWaterMass = []
_700SurfWaterMass = []
_1649SurfWaterMass = []

_1229EnvelopeMass = []
_72EnvelopeMass = []
_700EnvelopeMass = []
_1649EnvelopeMass = []
        
_1229OxygenMass = []
_72OxygenMass = []
_700OxygenMass = []
_1649OxygenMass = []

_1229HZLimEarlyMars = []
_72HZLimEarlyMars = []
_700HZLimEarlyMars = []
_1649HZLimEarlyMars = []

_1229FXUV = []
_72FXUV = []
_700FXUV = []
_1649FXUV = []
        
_1229RGLimit = []
_72RGLimit = []
_700RGLimit = []
_1649RGLimit = []
      


for i in range(0,8):
    _1229time.append(np.genfromtxt(direc_stars[i],usecols = (1),unpack=True))
    _72time.append(np.genfromtxt(direc_stars[i+8],usecols = (1),unpack=True))
    _700time.append(np.genfromtxt(direc_stars[i+16],usecols = (1),unpack=True))
    _1649time.append(np.genfromtxt(direc_stars[i+24],usecols = (1),unpack=True))

    _1229Luminosity.append(np.genfromtxt(direc_stars[i],usecols = (2),unpack=True))
    _72Luminosity.append(np.genfromtxt(direc_stars[i+8],usecols = (2),unpack=True))
    _700Luminosity.append(np.genfromtxt(direc_stars[i+16],usecols = (2),unpack=True))
    _1649Luminosity.append(np.genfromtxt(direc_stars[i+24],usecols = (2),unpack=True))
        
    _1229LXUVTot.append(np.genfromtxt(direc_stars[i],usecols = (3),unpack=True))
    _72LXUVTot.append(np.genfromtxt(direc_stars[i+8],usecols = (3),unpack=True))
    _700LXUVTot.append(np.genfromtxt(direc_stars[i+16],usecols = (3),unpack=True))
    _1649LXUVTot.append(np.genfromtxt(direc_stars[i+24],usecols = (3),unpack=True))
        


for i in range(0,8):
    _1229SurfWaterMass.append(np.genfromtxt(direc_planets[i],usecols = (3),unpack=True))
    _72SurfWaterMass.append(np.genfromtxt(direc_planets[i+8],usecols = (3),unpack=True))
    _700SurfWaterMass.append(np.genfromtxt(direc_planets[i+16],usecols = (3),unpack=True))
    _1649SurfWaterMass.append(np.genfromtxt(direc_planets[i+24],usecols = (3),unpack=True))

    _1229EnvelopeMass.append(np.genfromtxt(direc_planets[i],usecols = (4),unpack=True))
    _72EnvelopeMass.append(np.genfromtxt(direc_planets[i+8],usecols = (4),unpack=True))
    _700EnvelopeMass.append(np.genfromtxt(direc_planets[i+16],usecols = (4),unpack=True))
    _1649EnvelopeMass.append(np.genfromtxt(direc_planets[i+24],usecols = (4),unpack=True))
        
    _1229OxygenMass.append(np.genfromtxt(direc_planets[i],usecols = (5),unpack=True))
    _72OxygenMass.append(np.genfromtxt(direc_planets[i+8],usecols = (5),unpack=True))
    _700OxygenMass.append(np.genfromtxt(direc_planets[i+16],usecols = (5),unpack=True))
    _1649OxygenMass.append(np.genfromtxt(direc_planets[i+24],usecols = (5),unpack=True))
      
    _1229HZLimEarlyMars.append(np.genfromtxt(direc_planets[i],usecols = (10),unpack=True))
    _72HZLimEarlyMars.append(np.genfromtxt(direc_planets[i+8],usecols = (10),unpack=True))
    _700HZLimEarlyMars.append(np.genfromtxt(direc_planets[i+16],usecols = (10),unpack=True))
    _1649HZLimEarlyMars.append(np.genfromtxt(direc_planets[i+24],usecols = (10),unpack=True))

    _1229FXUV.append(np.genfromtxt(direc_planets[i],usecols = (11),unpack=True))
    _72FXUV.append(np.genfromtxt(direc_planets[i+8],usecols = (11),unpack=True))
    _700FXUV.append(np.genfromtxt(direc_planets[i+16],usecols = (11),unpack=True))
    _1649FXUV.append(np.genfromtxt(direc_planets[i+24],usecols = (11),unpack=True))
        
    _1229RGLimit.append(np.genfromtxt(direc_planets[i],usecols = (13),unpack=True))
    _72RGLimit.append(np.genfromtxt(direc_planets[i+8],usecols = (13),unpack=True))
    _700RGLimit.append(np.genfromtxt(direc_planets[i+16],usecols = (13),unpack=True))
    _1649RGLimit.append(np.genfromtxt(direc_planets[i+24],usecols = (13),unpack=True))
      

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['xtick.bottom'] = True
mpl.rcParams['ytick.right'] = True


fig, axes = plt.subplots(nrows=6, ncols=4,sharey='row',sharex = 'col',figsize=(30,36))

axes[0,0].set_title('Kepler-1229 b', fontsize = 45)
axes[0,1].set_title('K2-72 e', fontsize = 45)
axes[0,2].set_title('TOI-700 d', fontsize = 45)
axes[0,3].set_title('Kepler-1649 c', fontsize = 45)

style = ['-','--',':','-.','-','--',':','-.']
color=['red','red','red','red','darkred','darkred','darkred','darkred','limegreen','limegreen','limegreen','limegreen','darkgreen','darkgreen','darkgreen','darkgreen','cornflowerblue','cornflowerblue','cornflowerblue','cornflowerblue','midnightblue','midnightblue','midnightblue','midnightblue','gold','gold','gold','gold','darkgoldenrod','darkgoldenrod','darkgoldenrod','darkgoldenrod']

a=5

for i in range(0,8):
        axes[0,0].plot(_1229time[i], _1229EnvelopeMass[i],color=color[i], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[0,1].plot(_72time[i], _72EnvelopeMass[i],color=color[i+8], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[0,2].plot(_700time[i], _700EnvelopeMass[i],color=color[i+16], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[0,3].plot(_1649time[i], _1649EnvelopeMass[i],color=color[i+24], linewidth = a, linestyle = style[i],alpha = 0.4)

        axes[1,0].plot(_1229time[i], _1229SurfWaterMass[i],color=color[i], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[1,1].plot(_72time[i], _72SurfWaterMass[i],color=color[i+8], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[1,2].plot(_700time[i], _700SurfWaterMass[i],color=color[i+16], linewidth =a, linestyle = style[i],alpha = 0.4)
        axes[1,3].plot(_1649time[i], _1649SurfWaterMass[i],color=color[i+24], linewidth = a, linestyle = style[i],alpha = 0.4)

        axes[2,0].plot(_1229time[i], _1229OxygenMass[i],color=color[i], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[2,1].plot(_72time[i], _72OxygenMass[i],color=color[i+8], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[2,2].plot(_700time[i], _700OxygenMass[i],color=color[i+16], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[2,3].plot(_1649time[i], _1649OxygenMass[i],color=color[i+24], linewidth = a, linestyle = style[i],alpha = 0.4)

        axes[4,0].plot(_1229time[i], _1229LXUVTot[i]/_1229Luminosity[i],color=color[i], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[4,1].plot(_72time[i], _72LXUVTot[i]/_72Luminosity[i],color=color[i+8], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[4,2].plot(_700time[i], _700LXUVTot[i]/_700Luminosity[i],color=color[i+16], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[4,3].plot(_1649time[i], _1649LXUVTot[i]/_1649Luminosity[i],color=color[i+24], linewidth = a, linestyle = style[i],alpha = 0.4)
                       
        axes[5,0].plot(_1229time[i], _1229FXUV[i],color=color[i], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[5,1].plot(_72time[i], _72FXUV[i],color=color[i+8], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[5,2].plot(_700time[i], _700FXUV[i],color=color[i+16], linewidth = a, linestyle = style[i],alpha = 0.4)
        axes[5,3].plot(_1649time[i], _1649FXUV[i],color=color[i+24], linewidth = a, linestyle = style[i],alpha = 0.4)
        



for j in range(0,6):
         for i in range(0,4):
                  axes[j,i].set_xticks([1e7,1e8,1e9])
                  axes[j,i].get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())
                  axes[j,i].get_xaxis().set_tick_params(which='minor', size=5)
                  axes[j,i].get_xaxis().set_tick_params(which='minor', width=1) 
                  axes[j,i].get_xaxis().set_tick_params(which='major', size=6)
                  axes[j,i].get_xaxis().set_tick_params(which='major', width=2) 
         
                  axes[j,i].get_yaxis().set_tick_params(which='minor', size=5)
                  axes[j,i].get_yaxis().set_tick_params(which='minor', width=1) 
                  axes[j,i].get_yaxis().set_tick_params(which='major', size=6)
                  axes[j,i].get_yaxis().set_tick_params(which='major', width=2) 
         
axes[3,0].annotate("HZ", xy=(0.13, 0.3), xycoords='axes fraction', fontsize=44, horizontalalignment='left', verticalalignment='bottom',color='k')
axes[3,1].annotate("HZ", xy=(0.05, 0.25), xycoords='axes fraction', fontsize=44, horizontalalignment='left', verticalalignment='bottom',color='k')
axes[3,2].annotate("HZ", xy=(0.09, 0.3), xycoords='axes fraction', fontsize=44, horizontalalignment='left', verticalalignment='bottom',color='k')
axes[3,3].annotate("HZ", xy=(0.05, 0.2), xycoords='axes fraction', fontsize=44, horizontalalignment='left', verticalalignment='bottom',color='k')
    
         
for i in range(0,4):
        axes[0,i].set_xscale('log')
        axes[1,i].set_xscale('log')    
        axes[2,i].set_xscale('log')
        axes[3,i].set_xscale('log') 
        axes[4,i].set_xscale('log')
        axes[5,i].set_xscale('log') 
        axes[0,i].set_yscale('log')  
        #axes[2,i].set_yscale('log')    
        axes[1,i].set_yscale('log')    
        axes[4,0].set_ylabel(r'L$_{XUV}$/L$_{bol}$', fontsize = 45)
        axes[3,0].set_ylabel('Semi-Major\n Axis (AU)', fontsize = 45)
        axes[1,0].set_ylabel('Surface \n  Water (TO)', fontsize = 45)
        axes[0,0].set_ylabel(r"Envelope Mass (M$_{\oplus}$)", fontsize = 45)
        axes[5,0].set_ylabel(r'XUV flux (W/m$^{2}$)', fontsize = 45)
        axes[2,0].set_ylabel('Oxygen\n Pressure (bars)', fontsize = 45)
        axes[0,i].set_xlim(1e6,1e9)
        axes[1,i].set_xlim(1e6,1e9)
        axes[2,i].set_xlim(1e6,1e9)
        axes[3,i].set_xlim(1e6,1e9)
        axes[4,i].set_xlim(1e6,1e9)
        axes[5,i].set_xlim(1e6,1e9)
                
                
for i in range(1,4):    
        axes[4,i].set_ylabel(' ')
        axes[3,i].set_ylabel(' ')
        axes[1,i].set_ylabel(' ')
        axes[0,i].set_ylabel(' ')
        axes[5,i].set_ylabel(' ')
        axes[2,i].set_ylabel(' ')               

for i in range(0,4):            
        axes[5,i].set_xlabel('System Age (years)', fontsize = 45)        
 


axes[3,0].fill_between(_1229time[0],_1229RGLimit[0],_1229HZLimEarlyMars[0],color='red',alpha = 0.4)
axes[3,1].fill_between(_72time[0],_72RGLimit[0],_72HZLimEarlyMars[0],color='limegreen',alpha = 0.4)
axes[3,2].fill_between(_700time[0],_700RGLimit[0],_700HZLimEarlyMars[0],color='cornflowerblue',alpha = 0.4)
axes[3,3].fill_between(_1649time[0],_1649RGLimit[0],_1649HZLimEarlyMars[0],color='gold',alpha = 0.4)

# Exoplanet Archive
axes[3,0].axhline(y=0.3006 , xmin=0.0, xmax=1e11, color ="red", lw = 0.5)
axes[3,1].axhline(y=0.106 , xmin=0.0, xmax=1e11, color ="limegreen", lw = 0.5)
axes[3,2].axhline(y=0.1633 , xmin=0.0, xmax=1e11, color ="cornflowerblue", lw = 0.5)
axes[3,3].axhline(y=0.0827 , xmin=0.0, xmax=1e11, color ="gold", lw = 0.5)


#equivalente
axes[3,0].axhline(y=0.18634357906194876, xmin=0.0, xmax=1e11, color ="darkred", lw = 0.5) 
axes[3,1].axhline(y=0.09697016642590114 , xmin=0.0, xmax=1e11, color ="darkgreen", lw = 0.5)
axes[3,2].axhline(y=0.1553371071656616, xmin=0.0, xmax=1e11, color ="midnightblue", lw = 0.5)
axes[3,3].axhline(y=0.07376109168789859 , xmin=0.0, xmax=1e11, color ="darkgoldenrod", lw = 0.5)


g = '-'
for i in range(0,6):

#RGLimit AGE      EXOPLANET ARCHIVE
      axes[i,0].axvline(1.476e7, color ='red',ls=g, linewidth=3.5) #1229 EA   time 1.3760000000e+07 1.4760000000e+07
      axes[i,1].axvline(1.0552e8   , color ='limegreen',ls=g, linewidth=3.5) #k2 72 1.0452000000e+08 1.0552000000e+08
      axes[i,2].axvline(8.540e7, color ='cornflowerblue',ls=g, linewidth=3.5) #toi 700 8.4400000000e+07 8.5400000000e+07
      axes[i,3].axvline(1.1805e8, color ='gold',ls=g, linewidth=3.5) # 1649 1.1705000000e+08 1.1805000000e+08


#RGLimit AGE      EQUIVALENTE
      axes[i,0].axvline(1.154e+08, color ='darkred', linewidth=1.5) #1229 time 6.4830000000e+07 6.5830000000e+07
      axes[i,1].axvline(1.5784e+08, color ='darkgreen', linewidth=1.5) #k2 72 1.1947000000e+08 1.2047000000e+08
      axes[i,2].axvline(1.1405e+08, color ='midnightblue', linewidth=1.5) #toi 700 8.6470000000e+07 8.7470000000e+07
      axes[i,3].axvline(1.9295e+08, color ='darkgoldenrod', linewidth=1.5) # 1649 time 1.5983000000e+08 Age 1.6083000000e+08

for i in range(0,5):
        axes[i,0].set_xlabel(' ')
        axes[i,1].set_xlabel(' ')
        axes[i,2].set_xlabel(' ')
        axes[i,3].set_xlabel(' ')


legend_elements = [Line2D([0], [0], color='red', lw=18, label='Kepler-1229 b'),
                   Line2D([0], [0], color='limegreen', lw=18, label='K2-72 e'),
                   Line2D([0], [0], color='cornflowerblue', lw=18, label='TOI-700 d'),
                   Line2D([0], [0], color='gold', lw=18, label='Kepler-1649 c'),                   
                   Line2D([0], [0], color='darkred', lw=18, label='Kepler-1229 b modified'),
                   Line2D([0], [0], color='darkgreen', lw=18, label='K2-72 e modified'),
                   Line2D([0], [0], color='midnightblue', lw=18, label='TOI-700 d modified'),
                   Line2D([0], [0], color='darkgoldenrod', lw=18, label='Kepler-1649 c modified'),
                   Line2D([0], [0], ls='-', color='black', lw=7,label='stellar, 1 TO'),
                   Line2D([0], [0], ls='--', color='black',lw=7, label='stellar, 10 TO'),
                   Line2D([0], [0], ls=':', color='black', lw=7,label='stellar+flare, 1 TO'),
                   Line2D([0], [0], ls='-.', color='black',lw=7, label='stellar+flare, 10 TO')
]



for ax in axes.flatten():
    for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(45)

fig.subplots_adjust(left = 0.050,bottom=0.045, right=0.95, top=0.91, wspace = 0.18, hspace =0.08 )
plt.legend(handles=legend_elements,bbox_to_anchor=(-1.45,-1.15), loc="lower center", ncol=3, fontsize = 45)
fig.tight_layout()


# Save figure
if (sys.argv[1] == 'pdf'):
    fig.savefig('RealPlanetsSimulation.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    fig.savefig('RealPlanetsSimulation.png', bbox_inches="tight", dpi=250)     
