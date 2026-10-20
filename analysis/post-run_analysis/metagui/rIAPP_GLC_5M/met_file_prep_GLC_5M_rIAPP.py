import pandas as pd
import os

OneDrivePath = "/mnt/c/Users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/simulations/rIAPP/rIAPP_GLC_5M/"
path = os.path.join(OneDrivePath, "first_runs/outputs/")
save_path = os.path.join(OneDrivePath, "analysis/metagui/inputs/file_prep/")

# Create the 'metagui' directory if it does not exist
os.makedirs(save_path, exist_ok=True)

# Process COLVAR.0 file
file0 = open(path + 'COLVAR.0', 'r')
f0Cdf = pd.read_csv(file0, header=None, comment='#', sep=r'\s+', usecols=[0, 1, 2, 3])
f0Cdf.columns = ['time', 'alpha', 'beta', 'bias']
f0Cdf['time'] = f0Cdf['time'].round(0)
f0Cdf1 = f0Cdf.drop_duplicates(subset="time", keep="last", inplace=False)
f0Cdf2 = pd.concat([f0Cdf1[::20]], axis=0)
f0Cdf2 = f0Cdf2.reset_index()
f0Cdf3 = pd.concat([f0Cdf2['time'], f0Cdf2['alpha'], f0Cdf2['beta'], f0Cdf2['bias']], axis=1)
f0Cdf3.to_csv(os.path.join(save_path + "ogCOLVAR.0"), header=False, index=False, sep=" ")

# Process COLVAR.1 file
file1 = open(path + 'COLVAR.1', 'r')
f1Cdf = pd.read_csv(file1, header=None, comment='#', sep=r'\s+', usecols=[0, 1, 2, 3])
f1Cdf.columns = ['time', 'alpha', 'beta', 'bias']
f1Cdf['time'] = f1Cdf['time'].round(0)
f1Cdf1 = f1Cdf.drop_duplicates(subset="time", keep="last", inplace=False)
f1Cdf2 = pd.concat([f1Cdf1[::20]], axis=0)
f1Cdf2 = f1Cdf2.reset_index()
f1Cdf3 = pd.concat([f1Cdf2['time'], f1Cdf2['alpha'], f1Cdf2['beta'], f1Cdf2['bias']], axis=1)
f1Cdf3.to_csv(os.path.join(save_path + "ogCOLVAR.1"), header=False, index=False, sep=" ")

# Process COLVAR.2 file
file2 = open(path + 'COLVAR.2', 'r')
f2Cdf = pd.read_csv(file2, header=None, comment='#', sep=r'\s+', usecols=[0, 1, 2, 3])
f2Cdf.columns = ['time', 'alpha', 'beta', 'bias']
f2Cdf['time'] = f2Cdf['time'].round(0)
f2Cdf1 = f2Cdf.drop_duplicates(subset="time", keep="last", inplace=False)
f2Cdf2 = pd.concat([f2Cdf1[::20]], axis=0)
f2Cdf2 = f2Cdf2.reset_index()
f2Cdf3 = pd.concat([f2Cdf2['time'], f2Cdf2['alpha'], f2Cdf2['beta'], f2Cdf2['bias']], axis=1)
f2Cdf3.to_csv(os.path.join(save_path + "ogCOLVAR.2"), header=False, index=False, sep=" ")

# Process HILLS.0 file
file0 = open(path + 'HILLS.0', 'r')
f0Hdf = pd.read_csv(file0, header=None, comment='#', sep=r'\s+', usecols=[0, 1, 2, 3, 4])
f0Hdf.columns = ['time', 'alpha', 'sigma_alpha', 'height', 'biasf']
f0Hdf['time'] = f0Hdf['time'].round(0)
f0Hdf1 = f0Hdf.drop_duplicates(subset="time", keep="last", inplace=False)
f0Hdf1.to_csv(os.path.join(save_path + "ogHILLS.0"), header=False, index=False, sep=" ")

# Process HILLS.1 file
file1 = open(path + 'HILLS.1', 'r')
f1Hdf = pd.read_csv(file1, header=None, comment='#', sep=r'\s+', usecols=[0, 1, 2, 3, 4])
f1Hdf.columns = ['time', 'beta', 'sigma_beta', 'height', 'biasf']
f1Hdf['time'] = f0Hdf['time'].round(0)
f1Hdf1 = f1Hdf.drop_duplicates(subset="time", keep="last", inplace=False)
f1Hdf1.to_csv(os.path.join(save_path, "ogHILLS.1"), header=False, index=False, sep=" ")

# Process HILLS.2 file
file2 = open(path + 'HILLS.2', 'r')
f2Hdf = pd.read_csv(file2, header=None, comment='#', sep=r'\s+', usecols=[0, 1, 2, 3, 4, 5, 6])
f2Hdf.columns = ['time', 'alpha', 'beta', 'sigma_alpha', 'sigma_beta', 'height', 'biasf']
f2Hdf['time'] = f0Hdf['time'].round(0)
f2Hdf1 = f2Hdf.drop_duplicates(subset="time", keep="last", inplace=False)
f2Hdf1.to_csv(os.path.join(save_path, "ogHILLS.2"), header=False, index=False, sep=" ")

# Add COLVAR Headers
colvar0_header = "#! FIELDS time alpha beta be.bias uwall.bias Iwall.bias\n#! ACTIVE 1 1 A"
colvar1_header = "#! FIELDS time alpha beta be.bias uwall.bias Iwall.bias\n#! ACTIVE 1 2 B"
colvar2_header = "#! FIELDS time alpha beta be.bias uwall.bias Iwall.bias\n#! ACTIVE 2 1 2 C"

# Add headers to ogCOLVAR.0
with open(save_path + "ogCOLVAR.0", 'r') as file:
    C0_content = file.read()
final_C0 = colvar0_header + "\n" + C0_content
with open(save_path + "ogCOLVAR.0", 'w') as file:
    file.write(final_C0)

# Add headers to ogCOLVAR.1
with open(save_path + "ogCOLVAR.1", 'r') as file:
    C1_content = file.read()
final_C1 = colvar1_header + "\n" + C1_content
with open(save_path + "ogCOLVAR.1", 'w') as file:
    file.write(final_C1)

# Add headers to ogCOLVAR.2
with open(save_path + "ogCOLVAR.2", 'r') as file:
    C2_content = file.read()
final_C2 = colvar2_header + "\n" + C2_content
with open(save_path + "ogCOLVAR.2", 'w') as file:
    file.write(final_C2)

# Add HILLS Headers
hills0_header = "#! ACTIVE 1 1 A\n#! FIELDS time alpha beta be.bias uwall.bias Iwall.bias\n#! SET multivariate false"
hills1_header = "#! ACTIVE 1 2 B\n#! FIELDS time alpha beta be.bias uwall.bias Iwall.bias\n#! SET multivariate false"
hills2_header = "#! ACTIVE 2 1 2 C\n#! FIELDS time alpha beta be.bias uwall.bias Iwall.bias\n#! SET multivariate false"

# Add headers to ogHILLS.0
with open(save_path + "ogHILLS.0", 'r') as file:
    H0_content = file.read()
final_H0 = hills0_header + "\n" + H0_content
with open(save_path + "ogHILLS.0", 'w') as file:
    file.write(final_H0)

# Add headers to ogHILLS.1
with open(save_path + "ogHILLS.1", 'r') as file:
    H1_content = file.read()
final_H1 = hills1_header + "\n" + H1_content
with open(save_path + "ogHILLS.1", 'w') as file:
    file.write(final_H1)

# Add headers to ogHILLS.2
with open(save_path + "ogHILLS.2", 'r') as file:
    H2_content = file.read()
final_H2 = hills2_header + "\n" + H2_content
with open(save_path + "ogHILLS.2", 'w') as file:
    file.write(final_H2)
