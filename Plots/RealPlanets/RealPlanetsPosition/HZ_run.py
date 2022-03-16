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



#############################  criar pastas dentro de HZ_calculate com nome das massas estelares novas ###############################################

#inputs = ['input_flare','input_stellar']


#for val in inputs:
#                    #os.mkdir('/home/laura/vplanet-private/examples/AtmEsc_flare/M_dwarfs_Water/HZ_calculate/'+str(val)) 
#                  print(val)
#                os.system('cp /home/laura/vplanet-private/examples/AtmEsc_flare/M_dwarfs_Water/HZ_calculate/'+str(val)+'  /home/laura/vplanet-private/vspace/vspace') 
      
      
#############################  criar pastas dentro de HZ_calculate com nome das massas estelares novas ###############################################

vspace_dir = input("What is the directory that the folder '/vplanet-private/vspace/vspace' is placed?")
print(vspace_dir)              
              
########################################################
############LOADING DATA #################################              
########################################################              


# Copia o arquivo input para dentro do vspace 
os.system('cp ./HZ_calculate/input   '+vspace_dir+'/vspace/vspace') 
# Entra no vspace
os.chdir('vspace_dir')
#print(os.getcwd())
# Cria as pastas dentro de HZ_calculate com os arquivos star.in e vpl.in
os.system('python3 vspace.py input')

#############################################  rodar as simulaçoes da pasta ./HZ_calculate  ####################################################

#Entra na pasta HZ_calculate
os.chdir('./HabZone')

dir_path = os.path.dirname(os.path.realpath(__file__))

value_star = int(input("Quantos valores de massa estelar cada simulação tem?: ") )
print(value_star)  

folder_name1= 'star'
range_1 = value_star+1

folders = {}

for i in range(0,range_1):
        folders[f'{i}'] = folder_name1 +  "{:02d}".format(i)

dirs = []
dirs = list(folders.values())



print("\n Os diretórios onde as simulações vão ser corridas são %s " % dirs)

print("definindo função run_vplanet")

def run_vplanet(dir):
         print("\nRunning simulation in %s directory..." % dir)
         os.chdir(os.path.join(dir_path,dir))
         subprocess.call(['vplanet', 'vpl.in'])
         # Return to top-level directory
         os.chdir(dir_path)
         return dir 

print("paralelizando")


pool = mp.Pool(mp.cpu_count())
print(pool)

results = [pool.map(run_vplanet,[i for i in dirs])]

pool.close()

print(results)


