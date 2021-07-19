"""

Code to generate folders with different semi major axis to which stellar mass

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

results = [pool.map(run_vplanet,[i for i in planets])]

pool.close()

#Enter in the folder to calculate the semi major axis value
semi_mod = []

for dir in planets:
             os.chdir(dir)
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

