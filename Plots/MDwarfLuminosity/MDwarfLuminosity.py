"""
This script produces the Figures 2 from Amaral+2021, the
Stellar luminosity evolution of M dwarf stars between 0.2 and 0.6 Msun,
 using VPLANET's STELLAR and FLARE modules.

Laura N. R. do Amaral, Universidad Nacional Autónoma de México, 2021
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
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
mpl.rcParams['figure.figsize'] = (11,11)
mpl.rcParams['font.size'] = 15.0


mpl.rcParams['xtick.minor.size'] = 5
#mpl.rcParams['xtick.minor.width'] = 1
mpl.rcParams['ytick.minor.size'] = 5
#mpl.rcParams['ytick.minor.width'] = 1

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['xtick.bottom'] = True
mpl.rcParams['ytick.right'] = True

# Run the simulations
dir_path = os.path.dirname(os.path.realpath(__file__))
dirs = ["LumEvol_flare_FFD", "LumEvol_Stellar"]

# Return to top-level directory
os.chdir(dir_path)

# Load data
flare = vpl.GetOutput("./LumEvolFlareFFD")
stellar = vpl.GetOutput("./LumEvolStellar")


### First figure: Comparative atmospheric escape ###

# Plot
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, figsize=(10,11))
fig.subplots_adjust(right = 1.0, left = 0.05, bottom = 0.05, top = 0.91, wspace = 0.03, hspace =0.2 )

time02s = stellar.sstar_02.Age
time03s = stellar.sstar_03.Age
time04s = stellar.sstar_04.Age
time05s = stellar.sstar_05.Age
time06s = stellar.sstar_06.Age


time02f = flare.fstar_02.Age
time03f = flare.fstar_03.Age
time04f = flare.fstar_04.Age
time05f = flare.fstar_05.Age
time06f = flare.fstar_06.Age

import seaborn as sns
cmap = sns.color_palette("inferno", n_colors=5)


## Upper left: Luminosity ##
axes[0,0].plot(time02s, stellar.sstar_02.Luminosity,color = cmap[0], alpha = 0.3, lw = 6)
axes[0,0].plot(time03s, stellar.sstar_03.Luminosity, color = cmap[1], alpha = 0.3, lw = 6)
axes[0,0].plot(time04s, stellar.sstar_04.Luminosity, color = cmap[2], alpha = 0.3, lw = 6)
axes[0,0].plot(time05s, stellar.sstar_05.Luminosity, color = cmap[3], alpha = 0.3, lw = 6)
axes[0,0].plot(time06s, stellar.sstar_06.Luminosity, color = cmap[4], alpha = 0.3, lw = 6)

#axes[0,0].plot(time02f, flare.fstar_02.Luminosity, '--',color = cmap[0], alpha = 0.8)
#axes[0,0].plot(time03f, flare.fstar_03.Luminosity, '--',color = cmap[1], alpha = 0.8)
#axes[0,0].plot(time04f, flare.fstar_04.Luminosity, '--',color = cmap[2], alpha = 0.8)
#axes[0,0].plot(time05f, flare.fstar_05.Luminosity, '--',color = cmap[3], alpha = 0.8)
#axes[0,0].plot(time06f, flare.fstar_06.Luminosity, '--',color = cmap[4], alpha = 0.8)

axes[0,0].set_xscale('log')
axes[0,0].set_yscale("log")
axes[0,0].set_ylabel(r"Bolometric Luminosity ($L_\odot$)")
axes[0,0].set_title('a',fontsize=30, loc="left")


## Upper right: LXUVStellar ##
axes[0,1].plot(time02s, stellar.sstar_02.LXUVStellar,color = cmap[0], alpha = 0.3, lw = 6, label = r'0.2M$_{\odot}$ STELLAR')
axes[0,1].plot(time03s, stellar.sstar_03.LXUVStellar, color = cmap[1], alpha = 0.3, lw = 6, label = r'0.3M$_{\odot}$ STELLAR')
axes[0,1].plot(time04s, stellar.sstar_04.LXUVStellar, color = cmap[2], alpha = 0.3, lw = 6, label = r'0.4M$_{\odot}$ STELLAR')
axes[0,1].plot(time05s, stellar.sstar_05.LXUVStellar, color = cmap[3], alpha = 0.3, lw = 6, label = r'0.5M$_{\odot}$ STELLAR')
axes[0,1].plot(time06s, stellar.sstar_06.LXUVStellar, color = cmap[4], alpha = 0.3, lw = 6, label = r'0.6M$_{\odot}$ STELLAR')

#axes[0,1].plot(time02f, flare.fstar_02.LXUVStellar, '--',color = cmap[0], alpha = 0.8, label = r'0.2M$_{\odot}$ STELLAR+FLARE')
#axes[0,1].plot(time03f, flare.fstar_03.LXUVStellar, '--',color = cmap[1], alpha = 0.8, label = r'0.3M$_{\odot}$ STELLAR+FLARE')
#axes[0,1].plot(time04f, flare.fstar_04.LXUVStellar, '--',color = cmap[2], alpha = 0.8, label = r'0.4M$_{\odot}$ STELLAR+FLARE')
#axes[0,1].plot(time05f, flare.fstar_05.LXUVStellar, '--',color = cmap[3], alpha = 0.8, label = r'0.5M$_{\odot}$ STELLAR+FLARE')
#axes[0,1].plot(time06f, flare.fstar_06.LXUVStellar, '--',color = cmap[4], alpha = 0.8, label = r'0.6M$_{\odot}$ STELLAR+FLARE')

axes[0,1].legend(loc='lower left', fontsize = 14, ncol=1)
axes[0,1].set_yscale("log")
axes[0,1].set_xscale("log")
axes[0,1].set_ylabel(r"XUV Stellar Luminosity ($L_\odot$)")
axes[0,1].set_title('b',fontsize=30, loc="left")
axes[0,1].set_xlabel('  ')

## Down right: LXUVFlare ##
axes[1,0].plot(time02f, flare.fstar_02.LXUVFlare, '--',color = cmap[0], alpha = 0.8)
axes[1,0].plot(time03f, flare.fstar_03.LXUVFlare, '--',color = cmap[1], alpha = 0.8)
axes[1,0].plot(time04f, flare.fstar_04.LXUVFlare, '--',color = cmap[2], alpha = 0.8)
axes[1,0].plot(time05f, flare.fstar_05.LXUVFlare, '--',color = cmap[3], alpha = 0.8)
axes[1,0].plot(time06f, flare.fstar_06.LXUVFlare, '--',color = cmap[4], alpha = 0.8)

axes[1,0].set_yscale("log")
axes[1,0].set_ylabel(r"XUV Flare Luminosity  ($L_\odot$)")
axes[1,0].set_title('c',fontsize=30, loc="left")
axes[1,0].set_xlabel("Stellar Age (year)")

## Down left:LXUVTot ##
axes[1,1].plot(time02s, stellar.sstar_02.LXUVTot,color = cmap[0], alpha = 0.3, lw = 6)
axes[1,1].plot(time03s, stellar.sstar_03.LXUVTot, color = cmap[1], alpha = 0.3, lw = 6)
axes[1,1].plot(time04s, stellar.sstar_04.LXUVTot, color = cmap[2], alpha = 0.3, lw = 6)
axes[1,1].plot(time05s, stellar.sstar_05.LXUVTot, color = cmap[3], alpha = 0.3, lw = 6)
axes[1,1].plot(time06s, stellar.sstar_06.LXUVTot, color = cmap[4], alpha = 0.3, lw = 6)

axes[1,1].plot(time02f, flare.fstar_02.LXUVTot, '--',color = cmap[0], alpha = 0.8, label = r'0.2M$_{\odot}$ STELLAR+FLARE')
axes[1,1].plot(time03f, flare.fstar_03.LXUVTot, '--',color = cmap[1], alpha = 0.8, label = r'0.3M$_{\odot}$ STELLAR+FLARE')
axes[1,1].plot(time04f, flare.fstar_04.LXUVTot, '--',color = cmap[2], alpha = 0.8, label = r'0.4M$_{\odot}$ STELLAR+FLARE')
axes[1,1].plot(time05f, flare.fstar_05.LXUVTot, '--',color = cmap[3], alpha = 0.8, label = r'0.5M$_{\odot}$ STELLAR+FLARE')
axes[1,1].plot(time06f, flare.fstar_06.LXUVTot, '--',color = cmap[4], alpha = 0.8, label = r'0.6M$_{\odot}$ STELLAR+FLARE')

axes[1,1].legend(loc='lower left', fontsize = 12, ncol=1)
axes[1,1].set_yscale("log")
axes[1,1].set_ylabel(r"XUV Stellar+Flare Luminosity  ($L_\odot$)", fontsize=17)
axes[1,1].set_title('d',fontsize=30, loc="left")
axes[1,1].set_xlabel("Stellar Age (year)")
# Format all axes
for ax in axes.flatten():

    # Format x axis
    ax.set_xlim(time02s[1],time02s.max())
    ax.set_xscale("log")

    # Set rasterization
    ax.set_rasterization_zorder(0)

fig.tight_layout()
fig.subplots_adjust(wspace=0.25)
fig.subplots_adjust(hspace=0.1)


if (sys.argv[1] == 'pdf'):
    fig.savefig('MDwarfLuminosity.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    fig.savefig('MDwarfLuminosity.png', bbox_inches="tight", dpi=600)
