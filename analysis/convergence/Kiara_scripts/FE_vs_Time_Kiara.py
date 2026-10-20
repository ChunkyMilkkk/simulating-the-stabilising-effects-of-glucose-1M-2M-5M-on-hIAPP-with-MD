import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from numpy import trapz
from matplotlib.pyplot import figure

# Define all the paths in a dictionary
oneDrivePath = "/mnt/c/Users/20064950/OneDrive - Curtin/"
osmolyte_paths = {
    "Glucose 125 mM": os.path.join(oneDrivePath + "IAPP/hIAPP/glucose/125/analysis/sum_hills2/"),
    "Glucose 250 mM": os.path.join(oneDrivePath + "IAPP/hIAPP_osmolytes/glucose/Run7/250/sum_hills/"),
    "Glucose 500 mM": os.path.join(oneDrivePath + "IAPP/hIAPP_osmolytes/glucose/Run7/500/sum_hills/"),
    "Glycerol 125 mM": os.path.join(oneDrivePath + "IAPP/hIAPP_osmolytes/glycerol/Run5/125/sum_hills/"),
    "Glycerol 250 mM": os.path.join(oneDrivePath + "IAPP/hIAPP_osmolytes/glycerol/Run11/250/sum_hills/"),
    "Glycerol 500 mM": os.path.join(oneDrivePath + "IAPP/hIAPP_osmolytes/glycerol/Run6/500/sum_hills/"),
    "Sorbitol 125 mM": os.path.join(oneDrivePath + "IAPP/hIAPP_osmolytes/sorbitol/Run10/125/sum_hills/"),
    "Sorbitol 250 mM": os.path.join(oneDrivePath + "IAPP/hIAPP_osmolytes/sorbitol/Run7/250/sum_hills/"),
    "Sorbitol 500 mM": os.path.join(oneDrivePath + "IAPP/hIAPP_osmolytes/sorbitol/Run/500/sum_hills/")
}
save_path = os.path.join(oneDrivePath + "IAPP/hIAPP/paper/")

# Function to load FES files
def load_fes_files(path1):
    os.chdir(path1)
    print(f"Current working directory: {os.getcwd()}")

    # Load and sort the FES files
    FES_0_LIST = sorted(glob.glob('r0-fes-*.dat'), key=lambda x: int(x.split('-')[-1].split('.')[0]))
    FES_1_LIST = sorted(glob.glob('r1-fes-*.dat'), key=lambda x: int(x.split('-')[-1].split('.')[0]))
    FES_2a_LIST = sorted(glob.glob('r2-a-fes-*.dat'), key=lambda x: int(x.split('-')[-1].split('.')[0]))
    FES_2b_LIST = sorted(glob.glob('r2-b-fes-*.dat'), key=lambda x: int(x.split('-')[-1].split('.')[0]))

    return FES_0_LIST, FES_1_LIST, FES_2a_LIST, FES_2b_LIST


# Function to calculate area under the curve
def areaUnderCurve(file):
    with open(file, "r") as f:
        filedf = pd.read_table(f, header=None, comment='#', sep=r'\s+', usecols=range(2))
        filedf.columns = ['cv', 'fe']
        aot = trapz(filedf['fe'], filedf['cv'])
    return aot


# Function to process each osmolyte path
def process_path(path_name, path1):
    print(f"Processing {path_name}")

    # Load the files
    FES_0_LIST, FES_1_LIST, FES_2a_LIST, FES_2b_LIST = load_fes_files(path1)

    # Calculate and store the area under the curve
    v0a = []
    v1b = []
    v2a = []
    v2b = []

    for i in range(0, len(FES_0_LIST)):
        aotr0a1 = areaUnderCurve(FES_0_LIST[i])
        roundAotr0a1 = (round(aotr0a1, 2))
        v0a.append(roundAotr0a1)
    for i in range(len(FES_1_LIST)):
        aotr0a2 = areaUnderCurve(FES_1_LIST[i])
        roundAotr0a2 = (round(aotr0a2, 2))
        v1b.append(roundAotr0a2)
    for i in range(0, len(FES_2a_LIST)):
        aotr1b1 = areaUnderCurve(FES_2a_LIST[i])
        roundAotr1b1 = (round(aotr1b1, 2))
        v2a.append(roundAotr1b1)
    for i in range(len(FES_2b_LIST)):
        aotr1b2 = areaUnderCurve(FES_2b_LIST[i])
        roundAotr1b2 = (round(aotr1b2, 2))
        v2b.append(roundAotr1b2)

    # Plot the results
    figure(num=None, figsize=(16, 10))
    plt.rcParams["font.family"] = "Times New Roman"
    plt.plot(v0a, label='Rep 0', linewidth=2)
    plt.plot(v1b, label='Rep 1', linewidth=2)
    plt.plot(v2a, label='Rep 2 (alpha)', linewidth=2)
    plt.plot(v2b, label='Rep 2 (beta)', linewidth=2)
    plt.xlabel('x10 ns', fontsize=20)
    plt.ylabel('VUC (FE)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(loc='upper right', prop={'size': 16})
    plt.title(f'{path_name} VUC Plot')
    plt.savefig(f'{save_path}{path_name}_VUC.jpg', dpi=250, bbox_inches='tight', pad_inches=0.5)
    plt.show()

    d0a = np.diff(v0a)
    d1b = np.diff(v1b)
    d2a = np.diff(v2a)
    d2b = np.diff(v2b)

    figure(num=None, figsize=(16, 10))
    plt.rcParams["font.family"] = "Times New Roman"
    plt.plot(d0a, label='Rep 0', linewidth=2)
    plt.plot(d1b, label='Rep 1', linewidth=2)
    plt.plot(d2a, label='Rep 2 (alpha)', linewidth=2)
    plt.plot(d2b, label='Rep 2 (beta)', linewidth=2)
    plt.xlabel('x10 ns', fontsize=20)
    plt.ylabel('Diff VUC (FE)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(loc='lower right', prop={'size': 16})
    plt.title(f'{path_name} Difference in VUC Plot', fontsize=21)
    plt.savefig(f'{save_path}{path_name}_DVUC.jpg', dpi=250, bbox_inches='tight', pad_inches=0.5)
    plt.show()

    # Shorten the lists for scatter plot - sumhills numbering output of... found on as the name of output files from sumshills
    FES_0_LIST = FES_0_LIST[137:137]
    FES_1_LIST = FES_1_LIST[137:137]
    FES_2a_LIST = FES_2a_LIST[137:137]
    FES_2b_LIST = FES_2b_LIST[137:137]


    # Scatter plots for each FES list
    a = range(len(FES_0_LIST))
    colors = cm.rainbow(np.linspace(0, 1, len(FES_0_LIST)))

    # Plot for FES_0_LIST
    plt.figure(figsize=(16, 10))
    plt.rcParams["font.family"] = "Times New Roman"
    for i, c in zip(a, colors):
        file = open(FES_0_LIST[i], "r")
        filedf0 = pd.read_table(file, header=None, comment='#', sep=r'\s+', usecols=range(2))
        filedf0.columns = ['cv', 'fe']
        plt.scatter(filedf0['cv'], filedf0['fe'], s=1, color=c, label=f'{i+137}')
        plt.title(f'{path_name} Rep0 alpha', fontsize=21)
        plt.xlabel('CV', fontsize=20)
        plt.ylabel('FE', fontsize=20)
        plt.xticks(fontsize=19)
        plt.yticks(fontsize=19)
        plt.legend(loc='lower right', scatterpoints=1, fontsize=12, markerscale=4, title="Time (x10 ns)", title_fontsize=13)
        plt.savefig(f'{save_path}{path_name}_rep0.jpg', dpi=250, bbox_inches='tight', pad_inches=0.5)
    plt.show()

    # Repeat for FES_1_LIST, FES_2a_LIST, and FES_2b_LIST (use same structure)
    plt.figure(figsize=(16, 10))
    plt.rcParams["font.family"] = "Times New Roman"
    for i, c in zip(a, colors):
        file = open(FES_1_LIST[i], "r")
        filedf1 = pd.read_table(file, header=None, comment='#', sep=r'\s+', usecols=range(2))
        filedf1.columns = ['cv', 'fe']
        plt.scatter(filedf1['cv'], filedf1['fe'], s=1, color=c, label=f'{i+137}')
        plt.title(f'{path_name} Rep1 beta', fontsize=21)
        plt.xlabel('CV', fontsize=20)
        plt.ylabel('FE', fontsize=20)
        plt.xticks(fontsize=19)
        plt.yticks(fontsize=19)
        plt.legend(loc='lower right', scatterpoints=1, fontsize=12, markerscale=4, title="Time (x10 ns)", title_fontsize=13)
        plt.savefig(f'{save_path}{path_name}_rep1.jpg', dpi=250, bbox_inches='tight', pad_inches=0.5)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.rcParams["font.family"] = "Times New Roman"
    for i, c in zip(a, colors):
        file = open(FES_2a_LIST[i], "r")
        filedf2 = pd.read_table(file, header=None, comment='#', sep=r'\s+', usecols=range(2))
        filedf2.columns = ['cv', 'fe']
        plt.scatter(filedf2['cv'], filedf2['fe'], s=1, color=c, label=f'{i+137}')
        plt.title(f'{path_name} Rep2 alpha', fontsize=21)
        plt.xlabel('CV', fontsize=20)
        plt.ylabel('FE', fontsize=20)
        plt.xticks(fontsize=19)
        plt.yticks(fontsize=19)
        plt.legend(loc='lower right', scatterpoints=1, fontsize=12, markerscale=4, title="Time (x10 ns)", title_fontsize=13)
        plt.savefig(f'{save_path}{path_name}_rep2a.jpg', dpi=250, bbox_inches='tight', pad_inches=0.5)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.rcParams["font.family"] = "Times New Roman"
    for i, c in zip(a, colors):
        file = open(FES_2b_LIST[i], "r")
        filedf3 = pd.read_table(file, header=None, comment='#', sep=r'\s+', usecols=range(2))
        filedf3.columns = ['cv', 'fe']
        plt.scatter(filedf3['cv'], filedf3['fe'], s=1, color=c, label=f'{i+137}')
        plt.title(f'{path_name} Rep2 beta', fontsize=21)
        plt.xlabel('CV', fontsize=20)
        plt.ylabel('FE', fontsize=20)
        plt.xticks(fontsize=19)
        plt.yticks(fontsize=19)
        plt.legend(loc='lower right', scatterpoints=1, fontsize=12, markerscale=4, title="Time (x10 ns)", title_fontsize=13)
        plt.savefig(f'{save_path}{path_name}_rep2b.jpg', dpi=250, bbox_inches='tight', pad_inches=0.5)
    plt.show()

# Loop through all osmolyte paths and process them
for name, path in osmolyte_paths.items():
    process_path(name, path)
