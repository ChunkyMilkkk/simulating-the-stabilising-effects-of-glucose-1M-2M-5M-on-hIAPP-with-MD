#
# Created:  23/7/26
# Purpose:  For generating plots of various system properties against time to check if equilibration was successful.
#
#           Properties:             Expected plot:
#           Temperature             Stable.
#           Pressure                Stable.
#           Density                 Rises or falls early, then stable.
#           Volume                  Reaches a plateau.
#           Potential energy        Sharp initial decrease followed by stable plot.
#           Protein RMSD            --
#           Radius of gyration      --
#
# Usage:    Execute this program in the directory containing the "equil_analysis" directory made using the bash script "equilibration_analysis". If you rename the "equil_analysis" directory, use that name as the first arguement in the command line to begin this program (eg: python3 plots.py hIAPP_GLC_1M_equilibration_analysis).
#

import matplotlib.pyplot as plt
import sys

def read_this(fileName):
    if len(sys.argv)>1:
        path = f"{sys.argv[1]}/" + fileName
    else:
        path = "equil_analysis/" + fileName
    file=open(path, 'r')
    line=file.readline()
    contents=[]
    while line:
        line=line.strip()
        linelist=line.split()
        linelist=[float(i.strip()) for i in linelist]
        contents.append(linelist)
        line=file.readline()
    file.close()
    return contents

def plot_this(fileName, ylabel):
    tempFile=read_this(fileName)

    xdata=[]
    ydata=[]
    xsmall=[]
    ysmall=[]

    for i in range(len(tempFile)):
        xdata.append(tempFile[i][0])
        ydata.append(tempFile[i][1])
        if i<500:
            xsmall.append(tempFile[i][0])
            ysmall.append(tempFile[i][1])

    plt.plot(xdata, ydata)
    plt.xlabel("Time (ns)")
    plt.ylabel(ylabel)
    plt.show()

    plt.plot(xsmall, ysmall)
    plt.xlabel("Time (ns)")
    plt.ylabel(ylabel)
    plt.show()

# Temperature vs time

plot_this("temperature.xvg", "Temperature (K)")

# Pressure vs time

plot_this("pressure.xvg", "Pressure (bar)")

# Density vs time

plot_this("density.xvg", "Density")

# Volume vs time/Box-X, Box-Y, Box-Z vs time

plot_this("volume.xvg", "Volume")

# Potential energy vs time

plot_this("potential_energy.xvg", "Potential energy")

# Protein RMSD vs time

plot_this("backbone_rmsd.xvg", "RMSD")

# Radius of gyration vs time

plot_this("radius_gyration.xvg", "Radius of gyration")
