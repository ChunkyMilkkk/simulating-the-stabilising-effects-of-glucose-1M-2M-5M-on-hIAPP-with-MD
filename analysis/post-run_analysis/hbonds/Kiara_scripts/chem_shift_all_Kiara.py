import os
import pandas as pd
import csv

# Define base paths
oneDrivePath = "/mnt/c/Users/20064950/OneDrive - Curtin/IAPP/rIAPP/"
analysisPath = "analysis/chem_shift/"
molecules = {"glucose": "GLC", "glycerol": "GLL", "sorbitol": "SOR"}
concentrations = ["125", "250", "500"]

# Start times for each path
start_times = {
    "GLC125": 1260000, "GLC250": 1300000, "GLC500": 810000,
    "GLL125": 1000000, "GLL250": 1240000, "GLL500": 1120000,
    "SOR125": 810000, "SOR250": 1000000, "SOR500": 780000
}

# Generate paths and corresponding start times
osmolyte_paths = {}
for molecule_name, molecule_short_name in molecules.items():
    for concentration in concentrations:
        folder_path = f"{molecule_name}/{concentration}/{analysisPath}"
        osmolyte_path = os.path.join(oneDrivePath, folder_path)
        dic_ref = f"{molecule_short_name}{concentration}"
        osmolyte_paths[dic_ref] = {
            "path": osmolyte_path,
            "start_time": start_times[dic_ref],
            "shiftx2_files": [f"{osmolyte_path}CA_{dic_ref}_rIAPP_{rep}__CA.dat" for rep in range(3)],
            "weights_file": f"{osmolyte_path}../reweight/combined_df_rIAPP.csv",
            "total_summed_weights_file": f"{osmolyte_path}../reweight/total_summed_weights.csv",
            "save_path": osmolyte_path
        }

# Residue names
residue_names = ['LYS_1', 'CYS_2', 'ASN_3', 'THR_4', 'ALA_5', 'THR_6', 'CYS_7', 'ALA_8', 'THR_9', 'GLN_10', 'ARG_11',
                 'LEU_12', 'ALA_13', 'ASN_14', 'PHE_15', 'LEU_16', 'VAL_17', 'ARG_18', 'SER_19', 'SER_20', 'ASN_21',
                 'ASN_22', 'LEU_23', 'GLY_24', 'PRO_25', 'VAL_26', 'LEU_27', 'PRO_28', 'PRO_29', 'THR_30', 'ASN_31',
                 'VAL_32', 'GLY_33', 'SER_34', 'ASN_35', 'THR_36', 'TYR_37']

# Time increment per frame
time_increment = 20


# Convert SHIFTX2 output to CSV
def convert_to_csv(input_txt_file, output_csv_file):
    with open(input_txt_file, 'r') as input_file:
        with open(output_csv_file, 'w', newline='') as output_csv:
            csv_writer = csv.writer(output_csv)
            for line in input_file:
                if line.startswith('#'):  # Skip comment lines
                    continue
                values = line.split()  # Split on spaces
                csv_writer.writerow(values)
    print(f"File successfully converted to CSV format: {output_csv_file}")


# Function to merge, reweight, and return the DataFrame
def reweight_and_save(dfr, weights_column, weights_df, save_output_file):
    aligned_df = pd.merge(dfr, weights_df[['time', weights_column]], on='time', how='inner')
    result_df = aligned_df.iloc[:, 1:-1].multiply(aligned_df[weights_column], axis=0)
    total_row = result_df.sum()
    result_df.loc['Total'] = total_row
    result_df.to_csv(save_output_file, index=False)
    print(f"Reweighted data saved to: {save_output_file}")
    return result_df


# Process each path
for osmolyte_key, osmolyte_info in osmolyte_paths.items():
    print(f"Processing: {osmolyte_key}")

    # Convert and load SHIFTX2 files
    shiftx2_dfs = []
    for rep_idx, shiftx2_file in enumerate(osmolyte_info["shiftx2_files"]):
        csv_file = os.path.join(osmolyte_info["save_path"], f'shiftx2_rep{rep_idx}.csv')
        convert_to_csv(shiftx2_file, csv_file)
        df = pd.read_csv(csv_file, header=None, names=residue_names)
        df['time'] = osmolyte_info["start_time"] + (df.index * time_increment)
        shiftx2_dfs.append(df[['time'] + df.columns[:-1].tolist()])

    # Load weights and reweight for each replica
    df_weights = pd.read_csv(osmolyte_info["weights_file"])
    reweighted_dfs = []
    for rep_idx, df_rep in enumerate(shiftx2_dfs):
        output_file = os.path.join(osmolyte_info["save_path"], f'resultR{rep_idx}_shiftx2.csv')
        reweighted_df = reweight_and_save(df_rep, f'Rep{rep_idx}_weights', df_weights, output_file)
        reweighted_dfs.append(reweighted_df.loc['Total'])

    # Sum the "Total" rows across replicas
    summed_total = sum(reweighted_dfs)
    print("Summed total row across replicas:", summed_total)

    # Normalize summed total
    total_summed_weights = pd.read_csv(osmolyte_info["total_summed_weights_file"]).iloc[0, 0]
    normalized_summed_total = summed_total / total_summed_weights
    normalized_total_df = pd.DataFrame([normalized_summed_total], columns=residue_names)
    normalized_output = os.path.join(osmolyte_info["save_path"], 'normalized_summed_total_shiftx2.csv')
    normalized_total_df.to_csv(normalized_output, index=False)
    print(f"Normalized summed total saved to: {normalized_output}")

    # Apply correction
    correction_factors_B = {'A': -0.16, 'C': -0.01, 'D': 0.05, 'E': -0.01, 'F': -0.02, 'G': 0.13, 'H': -0.04, 'I': -0.27,
                            'K': -0.15, 'L': -0.20, 'M': -0.10, 'N': 0.05, 'P': -2.25, 'Q': 0.00, 'R': -0.13, 'S': -0.02, 'T': -0.09,
                            'V': -0.24, 'W': 0.24, 'Y': 0.00}
    correction_factors_C = {'A': -0.08, 'C': 0.09, 'D': 0.09, 'E': -0.04, 'F': -0.30, 'G': 0.01, 'H': -0.07, 'I': -0.22,
                            'K': -0.08, 'L': -0.14, 'M': -0.04, 'N': 0.16, 'P': -0.07, 'Q': 0.00, 'R': -0.06, 'S': 0.02, 'T': -0.05,
                            'V': -0.21, 'W': -0.23, 'Y': -0.34}
    # rIAPP residue sequence
    sequence = ['K', 'C', 'N', 'T', 'A', 'T', 'C', 'A', 'T', 'Q', 'R', 'L', 'A', 'N', 'F', 'L', 'V', 'R', 'S', 'S',
                'N', 'N', 'L', 'G', 'P', 'V', 'L', 'P', 'P', 'T', 'N', 'V', 'G', 'S', 'N', 'T', 'Y']


    def apply_correction(df_row, seq, corrections_B, corrections_C):
        corrected_row = []
        for res_idx, residue in enumerate(df_row.index):
            prev_residue = seq[res_idx - 1] if res_idx > 0 else None
            next_residue = seq[res_idx + 1] if res_idx < len(seq) - 1 else None
            correction_B = corrections_B.get(next_residue, 0) if next_residue else 0
            correction_C = corrections_C.get(prev_residue, 0) if prev_residue else 0
            corrected_shift = df_row[residue] + correction_B + correction_C
            corrected_row.append(corrected_shift)
        return corrected_row


    df = pd.read_csv(normalized_output)
    corrected_values = df.apply(lambda row: apply_correction(row, sequence, correction_factors_B, correction_factors_C),
                                axis=1)
    corrected_df = pd.DataFrame(corrected_values.tolist(), columns=sequence)
    corrected_output = os.path.join
