#!/bin/bash

declare -a resname=("SC_LYS_1" "SC_ASN_3" "SC_THR_4" "SC_THR_6" "SC_THR_9" "SC_GLN_10" "SC_ARG_11" "SC_ASN_14" "SC_HIS_18" "SC_SER_19" "SC_SER_20" "SC_ASN_21" "SC_ASN_22" "SC_GLY_24" "SC_ALA_25" "SC_SER_28" "SC_SER_29" "SC_THR_30" "SC_ASN_31" "SC_GLY_33" "SC_SER_34" "SC_ASN_35" "SC_THR_36" "SC_TYR_37")
declare -a glucose=("GLC_1M")

declare -A convergence=(
    ["GLC_1M"]="1200000"
)

declare -a Residue_SideChains_index=("21" "22" "23" "24" "25" "26" "27" "28" "29" "30" "31" "32" "33" "34" "35" "36" "37" "38" "39" "40" "41" "42" "43")

output_file="hb_sc_water_GLC1M_hIAPP.sh"
output_dir="/scratch/pawsey0110/kbruckner/first_runs/hIAPP_GLC_1M/hbonds/inputs"
xvg_output_dir="/scratch/pawsey0110/kbruckner/first_runs/hIAPP_GLC_1M/hbonds/outputs/protein/sc_water"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!Residue_SideChains_index[@]}"; do
      water=16
      ResSideChain=${Residue_SideChains_index[$i]}
      res=${resname[$i]}
      xvg_file="hIAPP_GLC1M_${res}_water_rep${j}.xvg"
      echo "echo '${water} ${ResSideChain}' | gmx_mpi hbond -f ${GLC}_hIAPP${j}.xtc -s ${GLC}_hIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
      echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."
