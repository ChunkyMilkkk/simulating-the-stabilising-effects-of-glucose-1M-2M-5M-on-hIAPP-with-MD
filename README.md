# Analysis
## Assessing Equilibration

Before beginning the production run for each of the six simulations, the system was equilibrated with a short simulation. Equilibration was assessed through the observation of several constructed plots of system properties against time. The directory tree for this assessment is displayed below:

.<br>
└── analysis<br>
&emsp;&emsp;    └── checking_equilibration<br>
&emsp;&emsp;&emsp;&emsp;        ├── equilibration_check.sh - a BASH script for generating .xtc and .xvg files used for plotting each property of the system<br>
&emsp;&emsp;&emsp;&emsp;        ├── plots.py - the program that generates plots of each simulation property<br>
&emsp;&emsp;&emsp;&emsp;        ├── hIAPP_GLC_1M_equilibration_analysis - one directory is made for each simulation to contain the generated .xtc and .xvg files<br>
&emsp;&emsp;&emsp;&emsp;        ├── hIAPP_GLC_2M_equilibration_analysis<br>
&emsp;&emsp;&emsp;&emsp;        ├── hIAPP_GLC_5M_equilibration_analysis<br>
&emsp;&emsp;&emsp;&emsp;        ├── rIAPP_GLC_1M_equilibration_analysis<br>
&emsp;&emsp;&emsp;&emsp;        ├── rIAPP_GLC_2M_equilibration_analysis<br>
&emsp;&emsp;&emsp;&emsp;        └── rIAPP_GLC_5M_equilibration_analysis<br>

## Assessing Convergence

.<br>
└── analysis<br>
&emsp;&emsp;    └── convergence<br>
&emsp;&emsp;&emsp;&emsp;        ├── FE_vs_Time.py - the program that generates convergence plots. Adapted from a script by Kiara Kidman<br>
&emsp;&emsp;&emsp;&emsp;        ├── Kiara_scripts - contains scripts I adapted for this analysis<br>
&emsp;&emsp;&emsp;&emsp;        │&emsp;&emsp;   └── FE_vs_Time_Kiara.py<br>
&emsp;&emsp;&emsp;&emsp;        └── convergence_plots<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Wk 7 - convergence plots were generated in 1-week increments to check if the simulations have converged<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Wk 8<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Wk 9<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Wk 10<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            └── completed_plots<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                ├── hIAPP Glucose 1 M_DVUC.jpg - displays the difference in free energy against time<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                ├── hIAPP Glucose 1 M_VUC.jpg - displays the raw free energy against time<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                ├── hIAPP Glucose 1 M_rep0.jpg - displays the free energy CV landscape of replica 0 (alpha RMSD)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                ├── hIAPP Glucose 1 M_rep1.jpg - displays the free energy CV landscape of replica 1 (beta RMSD)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                ├── hIAPP Glucose 1 M_rep2a.jpg - displays the free energy CV landscape of replica 2 (alpha RMSD)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                └── hIAPP Glucose 1 M_rep2b.jpg - displays the free energy CV landscape of replica 2 (beta RMSD)<br>

## Generating CV plots - Additional Content

.<br>
└── analysis<br>
&emsp;&emsp;    └── post-run_analysis<br>
&emsp;&emsp;&emsp;&emsp;        └── cv_plots<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── All_cv_plots.py - the program that generates the FES plots. Adapted from a script by Kiara Kidman<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            └── Kiara_scripts - contains scripts I adapted for this analysis<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                └── All_cv_plots.py<br>

## Generating FES Plots

.<br>
└── analysis<br>
&emsp;&emsp;    └── post-run_analysis<br>
&emsp;&emsp;&emsp;&emsp;        └── fes_plot<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Kiara_scripts<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── free_energy_surface_Kiara.py<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            └── free_energy_surface.py<br>

## Generating Hydrogen Bonding Plots

.<br>
└── analysis<br>
&emsp;&emsp;    └── post-run_analysis<br>
&emsp;&emsp;&emsp;&emsp;        └── hbonds<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hbond_reweighting.py - unbiasing H-bonding data. chem_shift_all_Kiara.py was referenced to make this script <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hbond_script_maker.py - reads Kiara's scripts for generating H-bond analysis scripts and adapts them for the concentrations and the convergence times of this study<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── pair_hbond_plotting.py - generates the final H-bonding plot<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hbond_plot_final.png - the final H-bonding plot<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hbond_plots - contains prototype programs and plots<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── Protein - Glucose_hbonding.png<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── Protein - Protein_hbonding.png<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── Protein - Water_hbonding.png<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hIAPP_hbonding.png<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── iapp_hbond_plotting.py<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── rIAPP_hbonding.png<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Kiara_datapoints - the H-bonding datapoints found from Kiara's study<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hIAPP_GLC_0.125<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   ├── pro_osmo - contains the protein-protein H-bond value from Kiara's study for 0.125 M glucose with hIAPP<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   │&emsp;&emsp;   └── normalized_summed_HB.csv<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   ├── pro_pro<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   └── pro_water<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hIAPP_GLC_0.25<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hIAPP_GLC_0.5<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── rIAPP_GLC_0.125<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── rIAPP_GLC_0.25<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── rIAPP_GLC_0.5<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Kiara_scripts - Kiara's scripts I referenced/adapted<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── chem_shift_all_Kiara.py<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hIAPP_GLC_125mM - contains scripts that hbond_script_maker.py reads and adapts <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── rIAPP_GLC_125mM<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hIAPP_GLC_1M - a directory for each simulation is made to contain H-bonding scripts<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── auto_exc.sh - makes scripts executable<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_GLC1M_submit_all.sh - a batch script for running H-bonding scripts on Setonix<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── make_all.sh - makes H-bonding scripts using all "maker.sh" scripts<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_pro-pro_GLC1M_maker.sh - used to find protein-protein H-bonds<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_pro_osmo_GLC1M_maker.sh - used to find protein-glucose H-bonds<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_pro_water_GLC1M_maker.sh - used to find protein-water H-bonds<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_MCHN_GLC1M_maker.sh&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_MCHN_water_GLC1M_maker.sh&nbsp;&nbsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_MCO_GLC1M_maker.sh&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_MCO_water_GLC1M_maker.sh&nbsp;&nbsp;&nbsp;&nbsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_osmo_osmo_GLC1M_maker.sh&nbsp;&nbsp;&nbsp;|---------- not used in this study. Would be used for a more advanced analysis<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_osmo_water_GLC1M_maker.sh&nbsp;&nbsp;&nbsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_sc_osmo_GLC1M_maker.sh&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hb_sc_water_GLC1M_maker.sh&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── hb_water_water_GLC1M_maker.sh&nbsp;&nbsp;&nbsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hIAPP_GLC_2M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hIAPP_GLC_5M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── rIAPP_GLC_1M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── rIAPP_GLC_2M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            └── rIAPP_GLC_5M<br>

## Using METAGUI to Generate Microstates

.<br>
└── analysis<br>
&emsp;&emsp;    └── post-run_analysis<br>
&emsp;&emsp;&emsp;&emsp;        └── metagui<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── metagui_script_maker.py<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Kiara_scripts<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── GLC125_met_hIAPP_Kiara.in<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── met_file_prep_GLC125_hIAPP_Kiara.py<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hIAPP_GLC_1M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── met_file_prep_GLC_1M_hIAPP.py<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── met_input_GLC_1M_hIAPP.in<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hIAPP_GLC_2M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── hIAPP_GLC_5M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── metagui_script_maker.py<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── rIAPP_GLC_1M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── rIAPP_GLC_2M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            └── rIAPP_GLC_5M<br>

## Reweighting data

.<br>
└── analysis<br>
&emsp;&emsp;    └── post-run_analysis<br>
&emsp;&emsp;&emsp;&emsp;        └── reweights<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── Kiara_scripts<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── reweighting_2024_Kiara.py<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            └── reweighting_GLC_IAPP_2026.py<br>

## Visualising Data

.<br>
└── analysis<br>
&emsp;&emsp;    └── post-run_analysis<br>
&emsp;&emsp;&emsp;&emsp;    └── visualisation<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;        ├── GLC_2M_rIAPP0_vis.bmp<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;        ├── GLC_2M_rIAPP0_vis_osmolytes.bmp<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;        └── glucose_protein_hbonds.tcl<br>

# Simulations

## Reference Scripts

.<br>
└── simulations<br>
&emsp;&emsp;    └── Kiara_sim_scripts - contains scripts Kiara allowed me to adapt & use for this study<br>
&emsp;&emsp;     &emsp;&emsp;   ├── hIAPP<br>
&emsp;&emsp;     &emsp;&emsp;   │&emsp;&emsp;   ├── hIAPP_GLC_1M - contains starting system files for each system that Kiara helped me set up<br>
&emsp;&emsp;     &emsp;&emsp;   │&emsp;&emsp;   ├── hIAPP_GLC_2M<br>
&emsp;&emsp;     &emsp;&emsp;   │&emsp;&emsp;   └── hIAPP_GLC_5M<br>
&emsp;&emsp;     &emsp;&emsp;   ├── rIAPP<br>
&emsp;&emsp;     &emsp;&emsp;   ├── mdp_files - contains parameter files for equilibration<br>
&emsp;&emsp;     &emsp;&emsp;   └── plumed_dats - contains plumed files I adapted to initiate WT-BEMD sampling<br>

## Simulation data

.<br>
└── simulations<br>
&emsp;&emsp;    └── hIAPP<br>
&emsp;&emsp;&emsp;&emsp;        └── hIAPP_GLC_1M<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── EM_EQ - contains inputs & outputs of each stage of the energy minimisation and equilibration step<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── analysis<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── cv_plots - contains CV plots for each replica - this is additional data that was not included<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── fes_plot<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   └── comparison-scaled_hIAPP_GLC_1M_D4_C1000_T1275ns.png - the FES used in the study<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── hbond - contains inputs, outputs and stages of data manipulation for H-bond analysis<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   ├── metagui<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   ├── inputs<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   │   ├── file_prep<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   │   └── met_input_GLC_1M_hIAPP.in<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   │&emsp;&emsp;   └── outputs - contains outputs from running the MICRO run and WHAM run<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── reweight - dir containing incremental .csv files made during reweighting with microstates<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            ├── first_runs - contains inputs and outputs of the simulation<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;   └── outputs<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;       ├── COLVAR.0<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;       ├── COLVAR.1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;       ├── COLVAR.2<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;       ├── HILLS.0<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;       ├── HILLS.1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;       ├── HILLS.2<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;       └── sum_hills - contains fes files generated using the plumed sum_hills command. Only the final fes file of each replica CV is shown<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;           ├── r0-fes-1666.dat<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;           ├── r1-fes-1666.dat<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;           ├── r2-a-fes-1666.dat<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            │&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;           └── r2-b-fes-1666.dat<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            └── system_setup - contains the files used to generate the starting topology of the system<br>
