import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import os
import matplotlib.cm as cm

OneDrivePath = "/mnt/c/Users/20064950/OneDrive - Curtin/IAPP/"
path = os.path.join(OneDrivePath, "hIAPP/glycerol/125/analysis/metagui/outputs/")
save_path = os.path.join(OneDrivePath + "hIAPP/glycerol/125/analysis/free_energy_surface/")

# Create the 'metagui' directory if it does not exist
os.makedirs(save_path, exist_ok=True)

fe = open(path + 'MICROSTATES','r')
fedf = pd.read_csv(fe,header=None,delim_whitespace=True,usecols=[0,1,2,3,4])
fedf.columns=['id','size','alpha','beta','FE']
fedf = fedf.loc[fedf.FE <80]
fedf = fedf.sort_values(by=['alpha','beta']).reset_index(drop=True)
fedf['eFE'] = [math.exp(-1*x/310) for x in fedf.FE]
fedf['alpha']= fedf.alpha.round(2)
fedf['beta'] = fedf.beta.round(2)
fedf.to_csv('fedf11.csv', index=False)

lbl = open(path + 'LABELS','r')
lbldf = pd.read_csv(lbl,header=None,delim_whitespace=True,usecols=[0,1,2,3,4,5])
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
plt.title('hIAPP', fontsize=28)
# Save the figure
plt.savefig(save_path + 'GLL125_H_D6_C1000_T1000ns.png', dpi=400, metadata=None, pad_inches=0, facecolor='white', edgecolor='white')

# Show the plot
plt.show()
