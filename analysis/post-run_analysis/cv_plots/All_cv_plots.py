import os
import pandas as pd
import matplotlib.pyplot as plt

def create_plot(c, i):
    
    input_path = f"/mnt/c/Users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/simulations/{i}/{i}_GLC_{c}/first_runs/outputs/"
    output_path = f"/mnt/c/Users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/simulations/{i}/{i}_GLC_{c}/analysis/cv_plots/"
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # File list and corresponding plot colours
    colvar_files = ["COLVAR.0", "COLVAR.1", "COLVAR.2"]
    plot_colours = ["mediumblue", "darkgreen", "crimson"]

    # Loop through each COLVAR file
    for colvar_file, colour in zip(colvar_files, plot_colours):
        full_path = os.path.join(input_path, colvar_file)

        # Read the data, skipping any comment lines
        data = pd.read_csv(full_path, sep=r'\s+', comment="#", header=None)

        # Extract alpha and beta
        alpha = data[1]
        beta = data[2]

        # Plot
        plt.figure(figsize=(10, 8))
        plt.scatter(alpha, beta, s=30, c=colour, alpha=0.7)
        plt.xlabel("Alpha RMSD", fontsize=14)
        plt.ylabel("Beta RMSD", fontsize=14)
        plt.title(f"{i} Glucose {c[0]} M - Alpha & Beta RMSD - {colvar_file}", fontsize=18)
        plt.grid(True)

        # Save plot
        save_name = f"{colvar_file}_alpha_vs_beta.png"
        save_path = os.path.join(output_path, save_name)
        plt.savefig(save_path, dpi=350)

        # Show the plot (optional for PyCharm)
        plt.show()

    print("All COLVAR plots saved successfully.")

## Code

concentrations = ["1M", "2M", "5M"]

IAPP = ["hIAPP", "rIAPP"]

# Input and output paths
for i in IAPP:
    for c in concentrations:
        create_plot(c, i)
