"""
This script produces the Figures 8 (bottom) from Amaral+2021, the
water escape by flares for stars between 0.2 and 0.6 Msun,
initial surface water between 1 and 10 TO, and planetary mass
between 0.5 and 5 Mearth, considering that planets cannot
lose the water when enters in the HZ, using VPLANET's AtmEsc,
STELLAR and FLARE modules.

Laura N. R. do Amaral, Universidad Nacional Autónoma de México, 2021
Date:  July 18th 2021
"""
import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
#import seaborn as sns
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import matplotlib.colors as colors


# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)


#NÚMERO DE ESTRELAS SIMULADAS
range_1 = 17
#NÚMERO DE OCEANOS SIMULADOS
range_2 = 37
#NÚMERO DE PLANETAS SIMULADOS
range_3 = 10


dirs_keys = []

for i in range(0,range_2):
    for k in range(0,range_3):
        for j in range(0,range_1):
              dirs_keys.append(f'{j}_{k}_{i}')            
              
#home = input("What is the directory that the folder water_escape_flares is placed?")
#print(home)              
              
########################################################
############LOADING DATA #################################              
########################################################              

path = './'#home+'/water_escape_flares/Data/'

folder = path+'flareRG.txt'
WL_flare,WI_flare = np.genfromtxt(folder, usecols = (6,7), unpack=True)
outputs_WI_flare = dict(zip(dirs_keys,WI_flare))
outputs_WL_flare = dict(zip(dirs_keys,WL_flare))

folder = path+'flareStopRG.txt'
WL_flare,WI_flare = np.genfromtxt(folder,usecols = (6,7), unpack=True)
outputs_WI_flare_stop = dict(zip(dirs_keys,WI_flare))
outputs_WL_flare_stop = dict(zip(dirs_keys,WL_flare))

folder = path+'stellarStopRG.txt'
WL_stellar,WI_stellar = np.genfromtxt(folder,usecols = (6,7), unpack=True)
outputs_WI_stellar_stop = dict(zip(dirs_keys,WI_stellar))
outputs_WL_stellar_stop = dict(zip(dirs_keys,WL_stellar))

folder = path+'stellarRG.txt'
WL_stellar,WI_stellar = np.genfromtxt(folder,usecols = (6,7), unpack=True)
outputs_WI_stellar = dict(zip(dirs_keys,WI_stellar))
outputs_WL_stellar = dict(zip(dirs_keys,WL_stellar))

################################################
keys = dict(zip(dirs_keys,WI_stellar)) 

water_esc_flare = {}
for ik in keys.keys():
        water_esc_flare[ik] = outputs_WI_flare[ik]-outputs_WL_flare[ik]
        
water_esc_stellar = {}
for ik in keys.keys():
        water_esc_stellar[ik] = outputs_WI_stellar[ik]-outputs_WL_stellar[ik]

water_esc_flare_stop = {}
for ik in keys.keys():
        water_esc_flare_stop[ik] = outputs_WI_flare_stop[ik]-outputs_WL_flare_stop[ik]

water_escP_flare_stop = {}
for ik in keys.keys():
        water_escP_flare_stop[ik] = (water_esc_flare_stop[ik]*100)/outputs_WI_flare_stop[ik]
 
water_esc_stellar_stop = {}
for ik in keys.keys():
        water_esc_stellar_stop[ik] = outputs_WI_stellar_stop[ik]-outputs_WL_stellar_stop[ik]

water_escP_stellar_stop = {}
for ik in keys.keys():
        water_escP_stellar_stop[ik] = (water_esc_stellar_stop[ik]*100)/outputs_WI_stellar_stop[ik]

######################################################
Masses = [0.2,0.225,0.25,0.275,0.3,0.325,0.35,0.375,0.4,0.425,0.45,0.475,0.5,0.525,0.55,0.575,0.6]
water_init = []
planetary = []
stellar_mass = []

for i in range(0,37):
    i = 1+i*0.25
    water_init.append(i)

for i in range(20,61):
    i = 0+i*0.01
    stellar_mass.append(i)

for i in range(10,101):
    i = 0+i*0.05
    planetary.append(i)
    
########################################################
####################  P L O T ##############################
########################################################
M = 17

wf = []
ws = []
Af = []
As = []

for ik, val in water_escP_flare_stop.items():
    wf.append(val)

        
for ik, val in water_escP_stellar_stop.items():
    ws.append(val)
    
    
for i in range(0,10):
        Af.append(wf[(i*M):(i+1)*M]+ wf[(i+10)*M:(i+11)*M]+wf[(i+20)*M:(i+21)*M]+wf[(i+30)*M:(i+31)*M]+wf[(i+40)*M:(i+41)*M]+wf[(i+50)*M:(i+51)*M]+wf[(i+60)*M:(i+61)*M]+wf[(i+70)*M:(i+71)*M]+wf[(i+80)*M:(i+81)*M]+wf[(i+90)*M:(i+91)*M]+wf[(i+100)*M:(i+101)*M]+wf[(i+110)*M:(i+111)*M]+wf[(i+120)*M:(i+121)*M]+wf[(i+130)*M:(i+131)*M]+wf[(i+140)*M:(i+141)*M]+wf[(i+150)*M:(i+151)*M]+wf[(i+160)*M:(i+161)*M]+wf[(i+170)*M:(i+171)*M]+wf[(i+180)*M:(i+181)*M]+wf[(i+190)*M:(i+191)*M]+wf[(i+200)*M:(i+201)*M]+wf[(i+210)*M:(i+211)*M]+wf[(i+220)*M:(i+221)*M]+wf[(i+230)*M:(i+231)*M]+wf[(i+240)*M:(i+241)*M]+wf[(i+250)*M:(i+251)*M]+wf[(i+260)*M:(i+261)*M]+wf[(i+270)*M:(i+271)*M]+wf[(i+280)*M:(i+281)*M]+wf[(i+290)*M:(i+291)*M]+wf[(i+300)*M:(i+301)*M]+wf[(i+310)*M:(i+311)*M]+wf[(i+320)*M:(i+321)*M]+wf[(i+330)*M:(i+331)*M]+wf[(i+340)*M:(i+341)*M]+wf[(i+350)*M:(i+351)*M]+wf[(i+360)*M:(i+361)*M])
        As.append(ws[(i*M):(i+1)*M]+ ws[(i+10)*M:(i+11)*M]+ws[(i+20)*M:(i+21)*M]+ws[(i+30)*M:(i+31)*M]+ws[(i+40)*M:(i+41)*M]+ws[(i+50)*M:(i+51)*M]+ws[(i+60)*M:(i+61)*M]+ws[(i+70)*M:(i+71)*M]+ws[(i+80)*M:(i+81)*M]+ws[(i+90)*M:(i+91)*M]+ws[(i+100)*M:(i+101)*M]+ws[(i+110)*M:(i+111)*M]+ws[(i+120)*M:(i+121)*M]+ws[(i+130)*M:(i+131)*M]+ws[(i+140)*M:(i+141)*M]+ws[(i+150)*M:(i+151)*M]+ws[(i+160)*M:(i+161)*M]+ws[(i+170)*M:(i+171)*M]+ws[(i+180)*M:(i+181)*M]+ws[(i+190)*M:(i+191)*M]+ws[(i+200)*M:(i+201)*M]+ws[(i+210)*M:(i+211)*M]+ws[(i+220)*M:(i+221)*M]+ws[(i+230)*M:(i+231)*M]+ws[(i+240)*M:(i+241)*M]+ws[(i+250)*M:(i+251)*M]+ws[(i+260)*M:(i+261)*M]+ws[(i+270)*M:(i+271)*M]+ws[(i+280)*M:(i+281)*M]+ws[(i+290)*M:(i+291)*M]+ws[(i+300)*M:(i+301)*M]+ws[(i+310)*M:(i+311)*M]+ws[(i+320)*M:(i+321)*M]+ws[(i+330)*M:(i+331)*M]+ws[(i+340)*M:(i+341)*M]+ws[(i+350)*M:(i+351)*M]+ws[(i+360)*M:(i+361)*M])
        
        
Zf = []
Zs = []

for i in range(0,10):
    Zf.append((np.reshape(Af[i], (range_2, range_1))).T)
    Zs.append((np.reshape(As[i], (range_2, range_1))).T)
# CRIANDO LISTAS PARA ARMAZENAR OS VALORES DE ÁGUA FINAL DE DIFERENTES PLANETAS(0,1,2,3)
maximum = [max(Af[0]),max(Af[1]),max(Af[3]),max(Af[5]),max(Af[9]),
           max(As[0]),max(As[1]),max(As[3]),max(As[5]),max(As[9])]

round_to_tenths = ['max '+str(round(num, 2))+'%' for num in maximum]



wf = []
ws = []
Af1 = []
As1 = []

for ik, val in water_esc_flare.items():
    wf.append(val)

        
for ik, val in water_esc_stellar.items():
    ws.append(val)
    
    
for i in range(0,10):
        Af1.append(wf[(i*M):(i+1)*M]+ wf[(i+10)*M:(i+11)*M]+wf[(i+20)*M:(i+21)*M]+wf[(i+30)*M:(i+31)*M]+wf[(i+40)*M:(i+41)*M]+wf[(i+50)*M:(i+51)*M]+wf[(i+60)*M:(i+61)*M]+wf[(i+70)*M:(i+71)*M]+wf[(i+80)*M:(i+81)*M]+wf[(i+90)*M:(i+91)*M]+wf[(i+100)*M:(i+101)*M]+wf[(i+110)*M:(i+111)*M]+wf[(i+120)*M:(i+121)*M]+wf[(i+130)*M:(i+131)*M]+wf[(i+140)*M:(i+141)*M]+wf[(i+150)*M:(i+151)*M]+wf[(i+160)*M:(i+161)*M]+wf[(i+170)*M:(i+171)*M]+wf[(i+180)*M:(i+181)*M]+wf[(i+190)*M:(i+191)*M]+wf[(i+200)*M:(i+201)*M]+wf[(i+210)*M:(i+211)*M]+wf[(i+220)*M:(i+221)*M]+wf[(i+230)*M:(i+231)*M]+wf[(i+240)*M:(i+241)*M]+wf[(i+250)*M:(i+251)*M]+wf[(i+260)*M:(i+261)*M]+wf[(i+270)*M:(i+271)*M]+wf[(i+280)*M:(i+281)*M]+wf[(i+290)*M:(i+291)*M]+wf[(i+300)*M:(i+301)*M]+wf[(i+310)*M:(i+311)*M]+wf[(i+320)*M:(i+321)*M]+wf[(i+330)*M:(i+331)*M]+wf[(i+340)*M:(i+341)*M]+wf[(i+350)*M:(i+351)*M]+wf[(i+360)*M:(i+361)*M])
        As1.append(ws[(i*M):(i+1)*M]+ ws[(i+10)*M:(i+11)*M]+ws[(i+20)*M:(i+21)*M]+ws[(i+30)*M:(i+31)*M]+ws[(i+40)*M:(i+41)*M]+ws[(i+50)*M:(i+51)*M]+ws[(i+60)*M:(i+61)*M]+ws[(i+70)*M:(i+71)*M]+ws[(i+80)*M:(i+81)*M]+ws[(i+90)*M:(i+91)*M]+ws[(i+100)*M:(i+101)*M]+ws[(i+110)*M:(i+111)*M]+ws[(i+120)*M:(i+121)*M]+ws[(i+130)*M:(i+131)*M]+ws[(i+140)*M:(i+141)*M]+ws[(i+150)*M:(i+151)*M]+ws[(i+160)*M:(i+161)*M]+ws[(i+170)*M:(i+171)*M]+ws[(i+180)*M:(i+181)*M]+ws[(i+190)*M:(i+191)*M]+ws[(i+200)*M:(i+201)*M]+ws[(i+210)*M:(i+211)*M]+ws[(i+220)*M:(i+221)*M]+ws[(i+230)*M:(i+231)*M]+ws[(i+240)*M:(i+241)*M]+ws[(i+250)*M:(i+251)*M]+ws[(i+260)*M:(i+261)*M]+ws[(i+270)*M:(i+271)*M]+ws[(i+280)*M:(i+281)*M]+ws[(i+290)*M:(i+291)*M]+ws[(i+300)*M:(i+301)*M]+ws[(i+310)*M:(i+311)*M]+ws[(i+320)*M:(i+321)*M]+ws[(i+330)*M:(i+331)*M]+ws[(i+340)*M:(i+341)*M]+ws[(i+350)*M:(i+351)*M]+ws[(i+360)*M:(i+361)*M])
        

Zf1 = []
Zs1 = []

for i in range(0,10):
    Zf1.append((np.reshape(Af1[i], (range_2, range_1))).T)
    Zs1.append((np.reshape(As1[i], (range_2, range_1))).T)

X, Y = np.meshgrid(water_init,Masses)


fig, axes = plt.subplots(figsize=(12,8),nrows=5, ncols=2, sharey=True ,sharex=True)
divnorm = mpl.colors.Normalize(vmin=0, vmax=max(wf))
v = np.linspace(0,3.5, 8, endpoint=True) # define quais valores dos datos reais vão aparecer no colorbar

dtf = {}
dts = {}

for ik, val in enumerate(Zs1):
    dts[ik] = [X,Y,val]
        
for ik, val in enumerate(Zf1):
    dtf[ik] = [X,Y,val]
    

vmax=max(wf)
vmin=0
levels = np.linspace(vmin,vmax,100)    
    
imfwater = axes[3,1].contourf(dtf[5][0], dtf[5][1], dtf[5][2], levels=levels,vmax=vmax,vmin=vmin, cmap = 'plasma_r',contours_showlines=False)
       


wf = []
ws = []
Af2 = []
As2 = []

for ik, val in water_esc_flare_stop.items():
    wf.append(val)

        
for ik, val in water_esc_stellar_stop.items():
    ws.append(val)
    
    
for i in range(0,10):
        Af2.append(wf[(i*M):(i+1)*M]+ wf[(i+10)*M:(i+11)*M]+wf[(i+20)*M:(i+21)*M]+wf[(i+30)*M:(i+31)*M]+wf[(i+40)*M:(i+41)*M]+wf[(i+50)*M:(i+51)*M]+wf[(i+60)*M:(i+61)*M]+wf[(i+70)*M:(i+71)*M]+wf[(i+80)*M:(i+81)*M]+wf[(i+90)*M:(i+91)*M]+wf[(i+100)*M:(i+101)*M]+wf[(i+110)*M:(i+111)*M]+wf[(i+120)*M:(i+121)*M]+wf[(i+130)*M:(i+131)*M]+wf[(i+140)*M:(i+141)*M]+wf[(i+150)*M:(i+151)*M]+wf[(i+160)*M:(i+161)*M]+wf[(i+170)*M:(i+171)*M]+wf[(i+180)*M:(i+181)*M]+wf[(i+190)*M:(i+191)*M]+wf[(i+200)*M:(i+201)*M]+wf[(i+210)*M:(i+211)*M]+wf[(i+220)*M:(i+221)*M]+wf[(i+230)*M:(i+231)*M]+wf[(i+240)*M:(i+241)*M]+wf[(i+250)*M:(i+251)*M]+wf[(i+260)*M:(i+261)*M]+wf[(i+270)*M:(i+271)*M]+wf[(i+280)*M:(i+281)*M]+wf[(i+290)*M:(i+291)*M]+wf[(i+300)*M:(i+301)*M]+wf[(i+310)*M:(i+311)*M]+wf[(i+320)*M:(i+321)*M]+wf[(i+330)*M:(i+331)*M]+wf[(i+340)*M:(i+341)*M]+wf[(i+350)*M:(i+351)*M]+wf[(i+360)*M:(i+361)*M])
        As2.append(ws[(i*M):(i+1)*M]+ ws[(i+10)*M:(i+11)*M]+ws[(i+20)*M:(i+21)*M]+ws[(i+30)*M:(i+31)*M]+ws[(i+40)*M:(i+41)*M]+ws[(i+50)*M:(i+51)*M]+ws[(i+60)*M:(i+61)*M]+ws[(i+70)*M:(i+71)*M]+ws[(i+80)*M:(i+81)*M]+ws[(i+90)*M:(i+91)*M]+ws[(i+100)*M:(i+101)*M]+ws[(i+110)*M:(i+111)*M]+ws[(i+120)*M:(i+121)*M]+ws[(i+130)*M:(i+131)*M]+ws[(i+140)*M:(i+141)*M]+ws[(i+150)*M:(i+151)*M]+ws[(i+160)*M:(i+161)*M]+ws[(i+170)*M:(i+171)*M]+ws[(i+180)*M:(i+181)*M]+ws[(i+190)*M:(i+191)*M]+ws[(i+200)*M:(i+201)*M]+ws[(i+210)*M:(i+211)*M]+ws[(i+220)*M:(i+221)*M]+ws[(i+230)*M:(i+231)*M]+ws[(i+240)*M:(i+241)*M]+ws[(i+250)*M:(i+251)*M]+ws[(i+260)*M:(i+261)*M]+ws[(i+270)*M:(i+271)*M]+ws[(i+280)*M:(i+281)*M]+ws[(i+290)*M:(i+291)*M]+ws[(i+300)*M:(i+301)*M]+ws[(i+310)*M:(i+311)*M]+ws[(i+320)*M:(i+321)*M]+ws[(i+330)*M:(i+331)*M]+ws[(i+340)*M:(i+341)*M]+ws[(i+350)*M:(i+351)*M]+ws[(i+360)*M:(i+361)*M])
        
        
Zf2 = []
Zs2 = []

for i in range(0,10):
    Zf2.append((np.reshape(Af2[i], (range_2, range_1))).T)
    Zs2.append((np.reshape(As2[i], (range_2, range_1))).T)

X, Y = np.meshgrid(water_init,Masses)



fig.text(0.5, 0.0, 'Initial Water Content (TO)', ha='center',  fontsize = 16)
fig.text(0.0, 0.5, 'Stellar Mass (M$_{\odot})$', va='center', rotation='vertical', fontsize = 16)


mpl.rcParams['font.size'] = 18;
mpl.rcParams.update({'font.size': 18})

mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.major.width'] = 1; mpl.rcParams['ytick.major.size'] = 4;mpl.rcParams['ytick.major.width'] = 1
mpl.rcParams['ytick.minor.size'] = 4; mpl.rcParams['xtick.direction'] = 'in';mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True;mpl.rcParams['xtick.bottom'] = True; mpl.rcParams['ytick.right'] = True

divnorm = mpl.colors.Normalize(vmin=0, vmax=3.5)
v = np.linspace(0,3.5, 8, endpoint=True) 

dtf = {}
dts = {}

for ik, val in enumerate(Zs2):
    dts[ik] = [X,Y,val]
        
for ik, val in enumerate(Zf2):
    dtf[ik] = [X,Y,val]
    
CSf = []
CSs = []

planet = [r'0.5 M$_{\oplus}$', r'1 M$_{\oplus}$', r'2 M$_{\oplus}$',r'3 M$_{\oplus}$', r'5 M$_{\oplus}$',]

vv = [0,10,20,40]
levels = np.array(vv)

vv = [0,10,30]
levels1 = np.array(vv)

CSs.append(axes[0,0].contour(X, Y,Zs[0], levels , colors=  ('k','k','k','k','k','k','k','k')))
CSs.append(axes[1,0].contour(X, Y,Zs[1], levels , colors= ('black','black','black','k','k')))
CSs.append(axes[2,0].contour(X, Y,Zs[3], levels , colors= ('black','black','black','k')))
CSs.append(axes[3,0].contour(X, Y,Zs[5], levels, colors= 'black'))
CSs.append(axes[4,0].contour(X, Y,Zs[9], levels, colors= 'black'))

CSf.append(axes[0,1].contour(X, Y,Zf[0], levels, colors= ('k','k','k','k','k','k','k','k')))
CSf.append(axes[1,1].contour(X, Y,Zf[1], levels, colors= ('k','k','k','k','k','k','k','k')))
CSf.append(axes[2,1].contour(X, Y,Zf[3], levels, colors=  ('black','black','black','k')))
CSf.append(axes[3,1].contour(X, Y,Zf[5], levels, colors=  ('black','black','black','k')))
CSf.append(axes[4,1].contour(X, Y,Zf[9], levels, colors=  ('black','black','k')))

#import seaborn as sns; sns.set_theme()
#cmap = sns.palplot(sns.cubehelix_palette(start=2.8, rot=.1))

for i in range(0,5):
    plt.clabel(CSs[i],CSs[i].levels[0::], inline=True, fontsize=12,fmt= '%1.0f'+str('%%'),inline_spacing= 5.5)
    plt.clabel(CSf[i],CSf[i].levels[0::], inline=True, fontsize=12,fmt= '%1.0f'+str('%%'),inline_spacing= 5.5)
    # stellar plots
    axes[i,0].annotate(planet[i], xy=(8.7, 0.23),  fontsize = 12, color = 'black', fontweight='bold',bbox=dict(boxstyle='round,pad=0.1', fc='white', edgecolor = 'white', alpha=0.9))
    # flare plots
    axes[i,1].annotate(planet[i], xy=(8.7, 0.23),  fontsize = 12, color = 'black', fontweight='bold',bbox=dict(boxstyle='round,pad=0.1', fc='white', edgecolor = 'white', alpha=0.9))
    #maximum values
    axes[i,0].annotate(round_to_tenths[i+5], xy=(1.1, 0.54),  fontsize = 12, color = 'black', fontweight='bold',bbox=dict(boxstyle='round,pad=0.1', fc='white', edgecolor = 'white', alpha=0.9))
    axes[i,1].annotate(round_to_tenths[i], xy=(1.1, 0.54),  fontsize = 12, color = 'black', fontweight='bold',bbox=dict(boxstyle='round,pad=0.1', fc='white', edgecolor = 'white', alpha=0.9))   
    
    
    
plt.clabel(CSs[0],CSs[0].levels[3:4], inline=True, fontsize=18,fmt= '%1.0f',inline_spacing= 5.5)
plt.clabel(CSs[1],CSs[1].levels[3:4], inline=True, fontsize=18,fmt= '%1.0f',inline_spacing= 5.5)
  
index = [0,1,3,5,9]



vmax=3.5
vmin=0
levels = np.linspace(vmin,vmax,100)    
    
    
for j,i in enumerate(index):
    imf = axes[j,1].contourf(dtf[i][0], dtf[i][1], dtf[i][2],levels=levels,vmax=vmax,vmin=vmin, cmap = 'plasma_r',contours_showlines=False)
    ims = axes[j,0].contourf(dts[i][0], dts[i][1], dts[i][2],levels=levels,vmax=vmax,vmin=vmin,  cmap = 'plasma_r',contours_showlines=False)
    for c in imf.collections:
          c.set_edgecolor("face")
    for c in ims.collections:
          c.set_edgecolor("face")


#2.93292387714033,1.34  
axes[3,0].scatter(1.2,0.480,marker= 'o', edgecolor = 'k',color = 'red', s = 50, label= 'Kepler 1229b') 
axes[3,0].scatter(9.8,0.480,marker= 'o', edgecolor = 'k',color = 'red', s = 50, label= 'Kepler 1229b') 
axes[3,1].scatter(1.2,0.480,marker= 'o', edgecolor = 'k',color = 'red', s = 50, label= 'Kepler 1229b') 
axes[3,1].scatter(9.8,0.480,marker= 'o', edgecolor = 'k',color = 'red', s = 50, label= 'Kepler 1229b') 
  
    
#2.550251841969678,1.29
axes[2,0].scatter(1.2,0.271365,marker= 's', edgecolor = 'k',color = 'green', s = 50, label= 'K2 72e')
axes[2,0].scatter(9.8,0.271365,marker= 's', edgecolor = 'k',color = 'green', s = 50, label= 'K2 72e')
axes[2,1].scatter(1.2,0.271365,marker= 's', edgecolor = 'k',color = 'green', s = 50, label= 'K2 72e')
axes[2,1].scatter(9.8,0.271365,marker= 's', edgecolor = 'k',color = 'green', s = 50, label= 'K2 72e')

#1.6398468083961741,1.144
axes[2,0].scatter(1.2, 0.415 ,marker= '*', edgecolor = 'k',color = 'blue', s = 100, label= 'TOI 700d')
axes[2,0].scatter(9.8, 0.415 ,marker= '*', edgecolor = 'k',color = 'blue', s = 100, label= 'TOI 700d')
axes[2,1].scatter(1.2, 0.415 ,marker= '*', edgecolor = 'k',color = 'blue', s = 100, label= 'TOI 700d')
axes[2,1].scatter(9.8, 0.415 ,marker= '*', edgecolor = 'k',color = 'blue', s = 100, label= 'TOI 700d')

#1.2389021700321832  ,1.06
axes[1,0].scatter(1.2,0.22,marker= '^', edgecolor = 'k',color = 'gold',s = 100, label= 'Kepler 1649c')
axes[1,0].scatter(9.8,0.22,marker= '^', edgecolor = 'k',color = 'gold',s = 100, label= 'Kepler 1649c')
axes[1,1].scatter(1.2,0.22,marker= '^', edgecolor = 'k',color = 'gold',s = 100, label= 'Kepler 1649c')
axes[1,1].scatter(9.8,0.22,marker= '^', edgecolor = 'k',color = 'gold',s = 100, label= 'Kepler 1649c')


water = [1,2,3,4,5,6,7,8,9,10]
axes[0,1].set_title('AtmEsc+Stellar+Flare', fontsize = 16)
axes[0,0].set_title('AtmEsc+Stellar', fontsize = 16)
fig.tight_layout(pad = 10)
fig.subplots_adjust(right = 1.0, left = 0.055, bottom = 0.06, top = 0.91, wspace = 0.03, hspace =0.2 )
cbar_ax = fig.add_axes([1.01, 0.049, 0.03, 0.861])
fig.colorbar(imfwater, cax=cbar_ax, orientation = 'vertical', ticks =v)
cbar_ax.set_ylabel('Surface water escaped (TO)', fontsize = 16)
plt.xticks(ticks=water)

for t in cbar_ax.axes.get_yticklabels():
     t.set_fontsize(14)

for ax in axes.flatten():
    for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(14)

axes[4,0].xaxis.set_major_locator(MaxNLocator(10)) 
axes[0,0].yaxis.set_major_locator(MaxNLocator(4)) 

# Save figure
if (sys.argv[1] == 'pdf'):
    fig.savefig('DoNotLossInHZ.pdf', bbox_inches="tight", dpi=300)
if (sys.argv[1] == 'png'):
    fig.savefig('DoNotLossInHZ.png', bbox_inches="tight", dpi=250)     
