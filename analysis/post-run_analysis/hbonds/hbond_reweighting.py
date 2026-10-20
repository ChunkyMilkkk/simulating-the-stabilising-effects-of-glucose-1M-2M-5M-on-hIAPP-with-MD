#
# program:  hbond_reweighting.py
# author:   adapted by Kirrily from Kiara
# purpose:  to reweight the hbond data for each simulation according to MICROSTATES found with metagui. This will unbias the simulations.
#
import os
import pandas as pd
import csv



## Defining functions

# Convert XVG output to CSV
def convert_to_csv(input_txt_file, output_csv_file):
    with open(input_txt_file, 'r') as input_file:
        with open(output_csv_file, 'w', newline='') as output_csv:
            
            csv_writer = csv.writer(output_csv)
            csv_writer.writerow(["time", "number"])

            for line in input_file:
                if line.startswith('#'):  # Skip comment lines
                    continue
                if line.startswith("@"):
                    continue

                values = line.split()  # Split on spaces
                values = [values[0], values[1]]
                csv_writer.writerow(values)
    print(f"File successfully converted to CSV format: {output_csv_file}")


# Function to merge, reweight, and return the DataFrame
def reweight_and_save(dfr, weights_df, save_output_file, rep_idx):
    weights_column = f"Rep{rep_idx}_weights"
    aligned_df = pd.merge(dfr, weights_df[['time', weights_column]], on = "time", how='inner')
    result_df = aligned_df["number"].multiply(aligned_df[weights_column], axis=0)
    result_df.to_csv(save_output_file, index=False)
    print(f"Reweighted data saved to: {save_output_file}")
    return result_df


# Function to process each path

def process_path(osmolyte_key, osmolyte_info):

    print(f"Processing: {osmolyte_key}")

    # Convert and load XVG files
    xvg_dfs = []
    for rep_idx, xvg_file in enumerate(osmolyte_info["xvg_files"]):
        csv_file = os.path.join(osmolyte_info["save_path"], f'{osmolyte_info["name"]}_hb_{osmolyte_info["pair"]}_rep{rep_idx}.csv')
        convert_to_csv(xvg_file, csv_file)
        df = pd.read_csv(csv_file)
        xvg_dfs.append(df)

    # Load weights and reweight for each replica
    df_weights = pd.read_csv(osmolyte_info["weights_file"])
    reweighted_dfs = []
    for rep_idx, df_rep in enumerate(xvg_dfs):
        output_path = os.path.join(osmolyte_info["save_path"], f'reweighted_HB_rep{rep_idx}.csv')
        reweighted_df = reweight_and_save(df_rep, df_weights, output_path, rep_idx)
        
        # Find the total for each replica
        total_row = reweighted_df.sum()
        reweighted_df.loc['Total'] = total_row
        reweighted_dfs.append(reweighted_df.loc['Total'])
        output_path = os.path.join(osmolyte_info["save_path"], f'summed_HB_rep{rep_idx}.csv')
        with open(output_path, mode = "w") as file:
            file.write(f"{total_row}")

    # Sum the "Total" rows across replicas
    summed_total = sum(reweighted_dfs)
    print("Summed total row across replicas:", summed_total)
    output_path = os.path.join(osmolyte_info["save_path"], "final_summed_HB.csv")
    with open(output_path, mode = "w") as file:
        file.write(f"{summed_total}")

    # Normalize summed total by dividing by total of each replica's weights. This brings data back in proportion to number of Hbonds
    total_summed_weights = pd.read_csv(osmolyte_info["total_summed_weights_file"]).iloc[0, 0]
    normalized_summed_total = summed_total / total_summed_weights
    normalized_total_df = pd.DataFrame([normalized_summed_total])
    normalized_output = os.path.join(osmolyte_info["save_path"], 'normalized_summed_HB.csv')
    normalized_total_df.to_csv(normalized_output, index=False, header=False)
    print(f"Normalized summed total saved to: {normalized_output}")



## Defining variables

#print("Current working directory:", os.getcwd())
oneDrivePath = "/mnt/c/users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/simulations/"
#oneDrivePath = "/Users/kiki/Library/CloudStorage/OneDrive - Curtin/IAPP_Osmolytes_2026/simulations"
#oneDrivePath = "./simulations"
analysisPath = "analysis/hbond/outputs"

molecules = {"glucose": "GLC"}
IAPP = ["hIAPP", "rIAPP"]
concentrations = ["1M", "2M", "5M"]
interactions = ["pro_pro", "pro_osmo", "pro_water"]

# Start times for each path
start_times = {\
    "hIAPP_GLC1M": 1275000, "hIAPP_GLC2M": 600000, "hIAPP_GLC5M": 300000,
    "rIAPP_GLC1M": 600000, "rIAPP_GLC2M": 800000, "rIAPP_GLC5M": 550000,
}

# Time increment per frame
time_increment = 20



# Begin Code

# Generate paths and corresponding start times
osmolyte_paths = {}
for molecule_name, molecule_short_name in molecules.items():
    for i in IAPP:
        for concentration in concentrations:
            pair = "pro_pro"
            folder_path = f"{i}/{i}_{molecule_short_name}_{concentration}/{analysisPath}/{pair}/"
            osmolyte_path = os.path.join(oneDrivePath, folder_path)
            dic_ref = f"{i}_{molecule_short_name}{concentration}"
            osmolyte_paths[dic_ref] = {
                "name": i + "_" + molecule_short_name + concentration,
                "pair": pair,
                "path": osmolyte_path,
                "start_time": start_times[dic_ref],
                "xvg_files": [f"{osmolyte_path}{dic_ref}_hb_{pair}_rep{rep}.xvg" for rep in range(3)],
                "weights_file": f"{osmolyte_path}../../../reweight/outputs/combined_df_{i}.csv",
                "total_summed_weights_file": f"{osmolyte_path}../../../reweight/outputs/total_summed_weights.csv",
                "save_path": osmolyte_path
            }

for osmolyte_key, osmolyte_info in osmolyte_paths.items():
    process_path(osmolyte_key, osmolyte_info)

print("Done! :D")
