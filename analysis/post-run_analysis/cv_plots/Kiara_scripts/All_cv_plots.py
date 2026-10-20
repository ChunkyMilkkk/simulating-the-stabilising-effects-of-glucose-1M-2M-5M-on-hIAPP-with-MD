import os
import pandas as pd
import matplotlib.pyplot as plt

# Input and output paths
input_path = "/mnt/e/Honours_2024/hIAPP/Glucose/250/Simulation"
output_path = "/mnt/e/Honours_2024/hIAPP/Glucose/250/Analysis/cv_plots"

# Create output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# File list and corresponding plot colours
colvar_files = ["COLVAR.0", "COLVAR.1", "COLVAR.2"]
plot_colours = ["mediumblue", "darkgreen", "crimson"]

# Loop through each COLVAR file
for colvar_file, colour in zip(colvar_files, plot_colours):
    full_path = os.path.join(input_path, colvar_file)

    # Read the data, skipping any comment lines
    data = pd.read_csv(full_path, delim_whitespace=True, comment="#", header=None)

    # Extract alpha and beta
    alpha = data[1]
    beta = data[2]

    # Plot
    plt.figure(figsize=(10, 8))
    plt.scatter(alpha, beta, s=30, c=colour, alpha=0.7)
    plt.xlabel("Alpha RMSD", fontsize=14)
    plt.ylabel("Beta RMSD", fontsize=14)
    plt.title(f"Glucose 250 mM - Alpha & Beta RMSD - {colvar_file}", fontsize=18)
    plt.grid(True)

    # Save plot
    save_name = f"{colvar_file}_alpha_vs_beta.png"
    save_path = os.path.join(output_path, save_name)
    plt.savefig(save_path, dpi=350)

    # Show the plot (optional for PyCharm)
    plt.show()

print("All COLVAR plots saved successfully.")
