import os
import pandas as pd
import math

def reweight(conc, IAPP, converged_time):
    OnedrivePath = "/mnt/c/Users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/simulations/"
    path = os.path.join(OnedrivePath + f"{IAPP}/{IAPP}_GLC_{conc}/analysis/metagui/outputs/")
    save_path = os.path.join(OnedrivePath + f"{IAPP}/{IAPP}_GLC_{conc}/analysis/reweight/outputs/")
    os.makedirs(save_path, exist_ok=True)
    os.chdir(path)
    print(save_path)


    ########################################################################################################################

    # Opens the MICROSTATES file and reads its content into a DataFrame (fedf)
    fe = open(path + "MICROSTATES", 'r')
    fedf = pd.read_csv(fe, header=None, sep=r'\s+', usecols=[0, 1, 2, 3, 4])
    fedf.columns = ['id', 'size', 'alpha', 'beta', 'FE']

    # Opens the LABELS file and reads its content into another DataFrame (lbldf)
    lbl = open(path + "LABELS", 'r')
    lbldf = pd.read_csv(lbl, header=None, sep=r'\s+', usecols=[0, 1, 2, 3])
    lbldf.columns = ['time', 'id', 'repNo', 'repID']
    feALLTraj = pd.merge(fedf, lbldf, on='id') ## merges id column and provides a column corresponding to each column in each dataframe

    # Merges the two DataFrames (fedf and lbldf) based on the 'id' column. This combines information from both files for each microstate (id)
    # Merged DataFrame (feALLTraj) is sorted based on 'repID' and 'time' columns, and the index is reset.
    # A new column, 'eFE', is added, which calculates the exponential of the negative free energy (FE)
    # divided by 310 for each row. This likely represents a Boltzmann factor calculation, as 310 could be related to the temperature (in Kelvin).
    feALLTraj = feALLTraj.sort_values(by=['repID', 'time']).reset_index(drop=True) # sorts rows according to repID, then time, then resets row index values to match newly sorted structure. Without resetting the index, the rows could not be called easily in order.
    feALLTraj['eFE'] = [math.exp(-1*x/310) for x in feALLTraj.FE] # eFE = 'exponential free energy'. creates a new column by using "FE" column values in specified calculations

    # Split the merged DataFrame into three separate DataFrames based on the replica number (repNo)
    feALLTrajR0 = feALLTraj.loc[feALLTraj.repNo == 0]
    feALLTrajR1 = feALLTraj.loc[feALLTraj.repNo == 1]
    feALLTrajR2 = feALLTraj.loc[feALLTraj.repNo == 2]

    # Filter each DataFrame (feALLTrajR0, feALLTrajR1, feALLTrajR2) to include only rows where 'time' is greater than or equal to 1000000.
    convBias0 = feALLTrajR0.loc[feALLTrajR0.time >= converged_time].reset_index(drop=True)
    convBias1 = feALLTrajR1.loc[feALLTrajR1.time >= converged_time].reset_index(drop=True)
    convBias2 = feALLTrajR2.loc[feALLTrajR2.time >= converged_time].reset_index(drop=True)

    # Save the filtered DataFrames as CSV files
    convBias0.to_csv(save_path + "convBias0.csv", index=False) # index=False ensures the row of index values is not printed to the csv file
    convBias1.to_csv(save_path + "convBias1.csv", index=False)
    convBias2.to_csv(save_path + "convBias2.csv", index=False)

    # Create and save the combined DataFrame
    combined_df = pd.DataFrame({
        'time': convBias0['time'], # defines first column as "time" with values from convBias0 "time" column
        'Rep0_weights': convBias0['eFE'],
        'Rep1_weights': convBias1['eFE'],
        'Rep2_weights': convBias2['eFE']
    })

    combined_df.to_csv(save_path + "combined_df_hIAPP.csv", index=False)
    print(combined_df.head())

    combined_file = open(save_path + "combined_df_hIAPP.csv", 'r')
    CF = pd.read_csv(combined_file) # CF = Converged free energies
    CF['Sum_Weights'] = CF['Rep0_weights'] + CF['Rep1_weights'] + CF['Rep2_weights'] # adds a column for the sum of weights at each timestep
    total_row = CF.sum() # the sum of each column
    CF.loc['Total'] = total_row # adds a row which contains the sum of each column
    CF.to_csv(save_path + "combined_df_SUMs.csv", index=False)

    ########################################################################################################################
    # Additional code to sum weights across replicas and save

    # Define paths
    weights_file = os.path.join(save_path + "combined_df_hIAPP.csv")
    output_file = save_path + 'summed_weights.csv'
    final_output_file = save_path + 'total_summed_weights.csv'

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

reweight("1M", "hIAPP", 1275000)

reweight("2M", "hIAPP", 600000)

reweight("5M", "hIAPP", 300000)

reweight("1M", "rIAPP", 600000)

reweight("2M", "rIAPP", 800000)

reweight("5M", "rIAPP", 550000)

