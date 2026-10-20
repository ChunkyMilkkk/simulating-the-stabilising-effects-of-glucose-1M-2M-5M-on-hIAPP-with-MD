import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import os
import matplotlib.cm as cm

def create_plot(IAPP, conc, converged_time):

    OneDrivePath = f"/mnt/c/Users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/simulations/{IAPP}/{IAPP}_GLC_{conc}/analysis/"
    path = os.path.join(OneDrivePath, "metagui/outputs/")
    save_path = os.path.join(OneDrivePath + "fes_plot/")

        # Create the 'metagui' directory if it does not exist
    os.makedirs(save_path, exist_ok=True)

    fe = open(path + 'MICROSTATES','r')
    fedf = pd.read_csv(fe,header=None,sep=r'\s+',usecols=[0,1,2,3,4])
    fedf.columns=['id','size','alpha','beta','FE']
    fedf = fedf.loc[fedf.FE <80]
    fedf = fedf.sort_values(by=['alpha','beta']).reset_index(drop=True)
    fedf['eFE'] = [math.exp(-1*x/310) for x in fedf.FE]
    fedf['alpha']= fedf.alpha.round(2)
    fedf['beta'] = fedf.beta.round(2)
    fedf.to_csv(save_path + 'fedf11.csv', index=False)

    lbl = open(path + 'LABELS','r')
    lbldf = pd.read_csv(lbl,header=None,sep=r'\s+',usecols=[0,1,2,3,4,5])
    lbldf.columns=['time','id','repNo','repID','alpha','beta']
    lbldf['alpha'] = lbldf.alpha.round(2)
    lbldf['beta']  = lbldf.beta.round(2)
    ############################################################################
    feAllTraj = pd.DataFrame()
    feAllTraj_merge = pd.merge(fedf,lbldf,on=['id'])
    feAllTraj_merge.columns = ['id','size','alphaFE','betaFE','FE','eFE','time','repNo','repID','alpha','beta']
    feAllTraj_merge = feAllTraj_merge.sort_values(by=['id']).reset_index(drop=True)
    feAllTraj_merge  = feAllTraj_merge.loc[feAllTraj_merge.FE < 80]
    ############################################################################

    # Create the figure
    figure = plt.figure(figsize = (20,13))
    plt.rcParams["font.family"] = "Times New Roman"

    # Assuming feAllTraj is already defined with alpha, beta, and FE attributes
    x = feAllTraj_merge.alpha
    y = feAllTraj_merge.beta
    c = feAllTraj_merge.FE

    # Use a hexbin plot instead of scatter plot
    im = plt.hexbin(x, y, C=c, gridsize=50, cmap=cm.plasma, linewidths=0.2)

    # Create the colorbar with proper scaling
    cbar = plt.colorbar(im)
    tick_font_size = 17
    cbar.ax.tick_params(labelsize=tick_font_size)
    cbar.set_label(label='FE (kJ/mol)', size=17)

    # Adjust tick sizes
    tick_font_size = 17
    cbar.ax.tick_params(labelsize=tick_font_size)
    cbar.set_label(label='FE (kJ/mol)', size=17)

    # Set limits and labels
    plt.xlim(0, 21)
    plt.ylim(0, 10)  # Set the upper limit of y-axis to 8

    # Set x and y ticks with the specified intervals
    plt.xticks(np.arange(0, 21, 5), fontsize=17)
    plt.yticks(np.arange(0, 10.5, 2), fontsize=17)  # Set y-axis ticks from 0 to 8

    # Set x and y axis labels
    plt.xlabel('Alpha-RMSD', fontsize=20)
    plt.ylabel('Anti-para Beta-RMSD', fontsize=20)
    plt.title(f'{IAPP} - Glucose {conc[0]} M', fontsize=28)
    # Save the figure
    plt.savefig(save_path + f'{IAPP}_GLC_{conc}_D4_C1000_T{converged_time}.png', dpi=400, metadata=None, pad_inches=0, facecolor='white', edgecolor='white')

    # Show the plot
    plt.show()

concentrations = ["1M","2M","5M"]
IAPP = ["hIAPP","rIAPP"]

convergence_times = {
    "hIAPP Glucose 1 M": "1275ns",
    "hIAPP Glucose 2 M": "600s",
    "hIAPP Glucose 5 M": "300ns",
    "rIAPP Glucose 1 M": "600ns",
    "rIAPP Glucose 2 M": "800ns",
    "rIAPP Glucose 5 M": "550ns"
}

for name, time in convergence_times.items():
    name_list = name.split()
    IAPP = name_list[0]
    conc = name_list[2] + name_list[3] # Joins concentration values with concentration units, as the function is formatted with this assumption
    create_plot(IAPP, conc, time)

