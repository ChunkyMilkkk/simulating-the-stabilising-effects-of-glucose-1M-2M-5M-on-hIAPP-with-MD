#!/bin/bash

declare -a resname=("SC_LYS_1" "SC_ASN_3" "SC_THR_4" "SC_THR_6" "SC_THR_9" "SC_GLN_10" "SC_ARG_11" "SC_ASN_14" "SC_ARG_18" "SC_SER_19" "SC_SER_20" "SC_ASN_21" "SC_ASN_22" "SC_GLY_24" "SC_THR_30" "SC_ASN_31" "SC_GLY_33" "SC_SER_34" "SC_ASN_35" "SC_THR_36" "SC_TYR_37")
declare -a glucose=("GLC_125")

declare -A convergence=(
    ["GLC_125"]="1260000"
)

declare -a Residue_SideChains_index=("21" "22" "23" "24" "25" "26" "27" "28" "29" "30" "31" "32" "33" "34" "35" "36" "37" "38" "39" "40" "41")

output_file="hb_sc_osmo_GLC125_rIAPP.sh"
output_dir="/mnt/c/Users/20064950/OneDrive - Curtin/IAPP/rIAPP/glucose/125/analysis/hbond"
xvg_output_dir="/scratch/pawsey0110/kiara/rIAPP/hbond/glucose/125/protein/sc_osmo"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!Residue_SideChains_index[@]}"; do
      osmo=12
      ResSideChain=${Residue_SideChains_index[$i]}
      res=${resname[$i]}
      xvg_file="rIAPP_GLC125_${res}_osmo_rep${j}.xvg"
      echo "echo '${osmo} ${ResSideChain}' | gmx_mpi hbond -f ${GLC}_rIAPP${j}.xtc -s ${GLC}_rIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
      echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."
