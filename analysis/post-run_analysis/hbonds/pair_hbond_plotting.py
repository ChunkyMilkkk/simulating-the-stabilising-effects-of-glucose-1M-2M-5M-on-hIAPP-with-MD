import matplotlib.pyplot as plt
import os
import numpy as np

# Defining functions:

def plot_hbond(pairDict, pairType, savePath):

    if pairType == "Protein - Protein":
        colourVar = "indianred"
        group = "hIAPP"
    elif pairType == "Protein - Glucose":
        colourVar = "plum"
        group = "glucose"
    elif pairType == "Protein - Water":
        colourVar = "royalblue"
        group = "water"
    
    ## hIAPP
    # Extract concentrations
    xvalues = pairDict["concentrations"]
    # Extract average hbond values
    yvalues = pairDict["hIAPP"]
    print("hIAPP:", xvalues, yvalues)

    #plt.plot(xvalues, yvalues, color=colourVar, marker="+", linestyle = "None")
    plt.plot(xvalues[0:3], yvalues[0:3], color=colourVar, marker="d", linestyle = "None")
    plt.plot(xvalues[3:6], yvalues[3:6], color=colourVar, marker="o", linestyle = "None")
    plt.plot(xvalues, yvalues, label=f"hIAPP - {group}", color=colourVar)

    if pairType == "Protein - Protein":
        group = "rIAPP"
    ## rIAPP
    # Extract concentrations
    xvalues = pairDict["concentrations"]
    # Extract average hbond values
    yvalues = pairDict["rIAPP"]
    print("rIAPP:", xvalues, yvalues)

    #plt.plot(xvalues, yvalues, color=colourVar, marker="+", linestyle = "None")
    plt.plot(xvalues[0:3], yvalues[0:3], color=colourVar, marker="d", linestyle = "None")
    plt.plot(xvalues[3:6], yvalues[3:6], color=colourVar, marker="o", linestyle = "None")
    plt.plot(xvalues, yvalues, label=f"rIAPP - {group}", color=colourVar, linestyle = "--")

def save_plot():
    plt.xlim(0, 5.5)
    plt.ylim(0, 110)

    # Set x and y ticks with the specified intervals
    plt.xticks(np.arange(0, 5.5, 1), fontsize=12)
    plt.yticks(np.arange(0, 110.5, 10), fontsize=12)

    #plt.title(f"The Number of H-Bonds with hIAPP and rIAPP at Different Concentrations of Glucose", fontsize=12)
    plt.xlabel("Glucose Concentration (M)", fontsize=12)
    plt.ylabel("Number of Hydrogen Bonds", fontsize=12)
    plt.legend(ncol = 3, loc='lower center', bbox_to_anchor=(0.5, -0.35))
    plt.grid(True) # Adds a grid background
    plt.subplots_adjust(bottom=0.2)

    # Save and show
    plt.savefig(savePath + f'hbond_plot_final.png', dpi=400, metadata=None, bbox_inches='tight',pad_inches=0.3, facecolor='white', edgecolor='white')
    plt.show()



# Defining variables:

#oneDrivePath = "/mnt/c/users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/"
#oneDrivePath = "/Users/kiki/Library/CloudStorage/OneDrive - Curtin/IAPP_Osmolytes_2026/"
oneDrivePath = "./"

osmolyte_paths = {
    "hIAPP Glucose 0.125 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_1M/analysis/hbond/outputs/"),        # <-- this is the only one currently switched on
    "hIAPP Glucose 0.25 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_2M/analysis/hbond/outputs/"),
    "hIAPP Glucose 0.5 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_5M/analysis/hbond/outputs/"),
    "rIAPP Glucose 0.125 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_1M/analysis/hbond/outputs/"),
    "rIAPP Glucose 0.25 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_2M/analysis/hbond/outputs/"),
    "rIAPP Glucose 0.5 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_5M/analysis/hbond/outputs/"),
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

pro_proPlot = {
    "concentrations" : [],
    "hIAPP" : [],
    "rIAPP" : []
    }

pro_osmoPlot = {
    "concentrations" : [],
    "hIAPP" : [],
    "rIAPP" : []
    }

pro_waterPlot = {
    "concentrations" : [],
    "hIAPP" : [],
    "rIAPP" : []
    }



# Start code:

for name, path in osmolyte_paths.items():
    listName = name.split()
    iappType = listName[0]
    conc = listName[2]
    units = listName[3]

    pairsDict = {}
    print(conc)
    for pair in analysisPairs:
        if float(conc) > 0.5:
            folderPath = f"simulations/{iappType}/{iappType}_GLC_{conc}{units}/analysis/hbond/outputs/{pair}/normalized_summed_HB.csv"
            pairPath = os.path.join(oneDrivePath, folderPath)
            with open(pairPath) as file:
                pairsDict[pair] = float(file.readline().strip())
        else:
            folderPath = f"analysis/post-run_analysis/hbonds/Kiara_datapoints/{iappType}_GLC_{conc}/{pair}/normalized_summed_HB.csv"
            pairPath = os.path.join(oneDrivePath, folderPath)
            with open(pairPath) as file:
                file.readline()
                pairsDict[pair] = float(file.readline().strip())

    if iappType == "hIAPP":
        pro_proPlot["concentrations"].append(float(conc))
        pro_proPlot["hIAPP"].append(pairsDict.get("pro_pro"))
        pro_osmoPlot["concentrations"].append(float(conc))
        pro_osmoPlot["hIAPP"].append(pairsDict.get("pro_osmo"))
        pro_waterPlot["concentrations"].append(float(conc))
        pro_waterPlot["hIAPP"].append(pairsDict.get("pro_water"))
    elif iappType == "rIAPP":
        #pro_proPlot["concentrations"].append(float(conc))
        pro_proPlot["rIAPP"].append(pairsDict.get("pro_pro"))
        #pro_osmoPlot["concentrations"].append(float(conc))
        pro_osmoPlot["rIAPP"].append(pairsDict.get("pro_osmo"))
        #pro_waterPlot["concentrations"].append(float(conc))
        pro_waterPlot["rIAPP"].append(pairsDict.get("pro_water"))

figure = plt.figure(figsize = (8,5))
plt.rcParams["font.family"] = "Times New Roman"

plot_hbond(pro_proPlot, "Protein - Protein", savePath)
plot_hbond(pro_osmoPlot, "Protein - Glucose", savePath)
plot_hbond(pro_waterPlot, "Protein - Water", savePath)
save_plot()
