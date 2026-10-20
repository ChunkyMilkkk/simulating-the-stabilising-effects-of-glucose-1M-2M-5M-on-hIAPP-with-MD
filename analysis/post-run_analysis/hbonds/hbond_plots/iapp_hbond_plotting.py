import matplotlib.pyplot as plt
import os
import numpy as np

# Defining functions:

def plot_hbond(iappDict, iappType, savePath):
    #fig, ax = plt.subplots()#figsize=(8, 5)) # Sets width and height in inches
    figure = plt.figure(figsize = (8,5))
    plt.rcParams["font.family"] = "Times New Roman"
    ## Protein - Protein
    # Extract concentrations
    xvalues = iappDict["concentrations"]
    # Extract average hbond values
    yvalues = iappDict["pro_pro"]

    plt.plot(xvalues, yvalues, label=f"{iappType}: Protein - Protein", color="goldenrod", marker="o")

    ## Protein - Glucose
    # Extract concentrations
    xvalues = iappDict["concentrations"]
    # Extract average hbond values
    yvalues = iappDict["pro_osmo"]

    plt.plot(xvalues, yvalues, label=f"{iappType}: Protein - Glucose", color="mediumseagreen", marker="o")

    ## Protein - Water
    # Extract concentrations
    xvalues = iappDict["concentrations"]
    # Extract average hBond values
    yvalues = iappDict["pro_water"]

    plt.plot(xvalues, yvalues, label=f"{iappType}: Protein - Water", color="mediumturquoise", marker="o")

    plt.xlim(0, 5.5)
    plt.ylim(0, 110)

    # Set x and y ticks with the specified intervals
    plt.xticks(np.arange(0, 5.5, 1), fontsize=12)
    plt.yticks(np.arange(0, 110.5, 10), fontsize=12)

    #plt.title(f"{iappType}", fontname="Times New Roman", fontsize=14)
    plt.xlabel("Glucose Concentration (M)", fontsize=12)
    plt.ylabel("Number of Hydrogen Bonds", fontsize=12)
    plt.legend(ncol = 3, loc='lower center', bbox_to_anchor=(0.5, -0.24))
    plt.grid(True) # Adds a grid background
    plt.subplots_adjust(bottom=0.2)

    # Save and show
    plt.savefig(savePath + f'{iappType}_hbonding.png', dpi=400, metadata=None, pad_inches=1, facecolor='white', edgecolor='white')
    plt.show()



# Defining variables:

#oneDrivePath = "/mnt/c/users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/"
#oneDrivePath = "/Users/kiki/Library/CloudStorage/OneDrive - Curtin/IAPP_Osmolytes_2026/"
oneDrivePath = "./"

osmolyte_paths = {
    "hIAPP Glucose 1 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_1M/analysis/hbond/outputs/"),        # <-- this is the only one currently switched on
    "hIAPP Glucose 2 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_2M/analysis/hbond/outputs/"),
    "hIAPP Glucose 5 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_5M/analysis/hbond/outputs/"),
    "rIAPP Glucose 1 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_1M/analysis/hbond/outputs/"),
    "rIAPP Glucose 2 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_2M/analysis/hbond/outputs/"),
    "rIAPP Glucose 5 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_5M/analysis/hbond/outputs/")
}

savePath = os.path.join(oneDrivePath + "/analysis/post-run_analysis/hbonds/")

analysisIapp = ["hIAPP", "rIAPP"]

analysisPairs = ["pro_pro", "pro_osmo", "pro_water"]

hiappPlot = {
    "concentrations" : [],
    "pro_pro" : [],
    "pro_osmo" : [],
    "pro_water" : []
    }

riappPlot = {
    "concentrations" : [],
    "pro_pro" : [],
    "pro_osmo" : [],
    "pro_water" : []
    }



# Start code:

for name, path in osmolyte_paths.items():
    listName = name.split()
    iappType = listName[0]
    conc = listName[2]
    units = listName[3]

    pairsDict = {}
    for pair in analysisPairs:
        folderPath = f"simulations/{iappType}/{iappType}_GLC_{conc}{units}/analysis/hbond/outputs/{pair}/normalized_summed_HB.csv"
        pairPath = os.path.join(oneDrivePath, folderPath)
        with open(pairPath) as file:
            pairsDict[pair] = float(file.readline().strip())

    if iappType == "hIAPP":
        hiappPlot["concentrations"].append(float(conc))
        hiappPlot["pro_pro"].append(pairsDict.get("pro_pro"))
        hiappPlot["pro_osmo"].append(pairsDict.get("pro_osmo"))
        hiappPlot["pro_water"].append(pairsDict.get("pro_water"))
    elif iappType == "rIAPP":
        riappPlot["concentrations"].append(float(conc))
        riappPlot["pro_pro"].append(pairsDict.get("pro_pro"))
        riappPlot["pro_osmo"].append(pairsDict.get("pro_osmo"))
        riappPlot["pro_water"].append(pairsDict.get("pro_water"))

plot_hbond(hiappPlot, "hIAPP", savePath)
plot_hbond(riappPlot, "rIAPP", savePath)
