import os
import pandas as pd
import math

OnedrivePath = "/mnt/c/Users/20064950/OneDrive - Curtin/IAPP/"
path = os.path.join(OnedrivePath + "rIAPP/control/analysis/reweight/")
os.chdir(path)


########################################################################################################################

# Opens the MICROSTATES file and reads its content into a DataFrame (fedf)
fe = open(path + "MICROSTATES", 'r')
fedf = pd.read_csv(fe, header=None, delim_whitespace=True, usecols=[0, 1, 2, 3, 4])
fedf.columns = ['id', 'size', 'alpha', 'beta', 'FE']

# Opens the LABELS file and reads its content into another DataFrame (lbldf)
lbl = open(path + "LABELS", 'r')
lbldf = pd.read_csv(lbl, header=None, delim_whitespace=True, usecols=[0, 1, 2, 3])
lbldf.columns = ['time', 'id', 'repNo', 'repID']
feALLTraj = pd.merge(fedf, lbldf, on='id')

# Merges the two DataFrames (fedf and lbldf) based on the 'id' column. This combines information from both files for each microstate (id)
# Merged DataFrame (feALLTraj) is sorted based on 'repID' and 'time' columns, and the index is reset.
# A new column, 'eFE', is added, which calculates the exponential of the negative free energy (FE)
# divided by 310 for each row. This likely represents a Boltzmann factor calculation, as 310 could be related to the temperature (in Kelvin).
feALLTraj = feALLTraj.sort_values(by=['repID', 'time']).reset_index(drop=True)
feALLTraj['eFE'] = [math.exp(-1*x/310) for x in feALLTraj.FE]

# Split the merged DataFrame into three separate DataFrames based on the replica number (repNo)
feALLTrajR0 = feALLTraj.loc[feALLTraj.repNo == 0]
feALLTrajR1 = feALLTraj.loc[feALLTraj.repNo == 1]
feALLTrajR2 = feALLTraj.loc[feALLTraj.repNo == 2]

# Filter each DataFrame (feALLTrajR0, feALLTrajR1, feALLTrajR2) to include only rows where 'time' is greater than or equal to 500000.
convBias0 = feALLTrajR0.loc[feALLTrajR0.time >= 500000].reset_index(drop=True)
convBias1 = feALLTrajR1.loc[feALLTrajR1.time >= 500000].reset_index(drop=True)
convBias2 = feALLTrajR2.loc[feALLTrajR2.time >= 500000].reset_index(drop=True)

# Save the filtered DataFrames as CSV files
convBias0.to_csv(path + "convBias0.csv", index=False)
convBias1.to_csv(path + "convBias1.csv", index=False)
convBias2.to_csv(path + "convBias2.csv", index=False)

# Create and save the combined DataFrame
combined_df = pd.DataFrame({
    'time': convBias0['time'],
    'Rep0_weights': convBias0['eFE'],
    'Rep1_weights': convBias1['eFE'],
    'Rep2_weights': convBias2['eFE']
})

combined_df.to_csv(path + "combined_df_rIAPP.csv", index=False)
print(combined_df.head())

combined_file = open(path + "combined_df_rIAPP.csv", 'r')
CF = pd.read_csv(combined_file)
CF['Sum_Weights'] = CF['Rep0_weights'] + CF['Rep1_weights'] + CF['Rep2_weights']
total_row = CF.sum()
CF.loc['Total'] = total_row
CF.to_csv(path + "combined_df_SUMs.csv", index=False)

########################################################################################################################
# Additional code to sum weights across replicas and save

# Define paths
weights_file = os.path.join(path + "combined_df_rIAPP.csv")
output_file = path + 'summed_weights.csv'
final_output_file = path + 'total_summed_weights.csv'

# Read the combined weights CSV file
df_weights = pd.read_csv(weights_file)

# Initialize a new DataFrame for the summed results
summed_weights_df = pd.DataFrame()

# Calculate the sum for each weights column and add to the new DataFrame
summed_weights_df['Rep0_weights_sum'] = [df_weights['Rep0_weights'].sum()]
summed_weights_df['Rep1_weights_sum'] = [df_weights['Rep1_weights'].sum()]
summed_weights_df['Rep2_weights_sum'] = [df_weights['Rep2_weights'].sum()]

# Save the summed weights DataFrame to a CSV file
summed_weights_df.to_csv(output_file, index=False)

# Calculate the total sum of all replicas' weights
total_sum = summed_weights_df['Rep0_weights_sum'][0] + summed_weights_df['Rep1_weights_sum'][0] + summed_weights_df['Rep2_weights_sum'][0]

# Create a new DataFrame to store the total sum
total_summed_weights_df = pd.DataFrame({'Total_Summed_Weights': [total_sum]})

# Save the total summed weights DataFrame to a new CSV file
total_summed_weights_df.to_csv(final_output_file, index=False)
