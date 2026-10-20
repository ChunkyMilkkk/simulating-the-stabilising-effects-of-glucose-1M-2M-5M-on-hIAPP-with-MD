#!/bin/bash

declare -a glucose=("GLC_2M")

declare -A convergence=(
    ["GLC_2M"]="800000"
)

declare -a rIAPP_Protein_index=("1")
declare -a osmo_index=("12")

output_file="hb_pro_osmo_GLC2M_rIAPP.sh"
output_dir="/scratch/pawsey0110/kbruckner/first_runs/rIAPP_GLC_2M/hbond/inputs"
xvg_output_dir="/scratch/pawsey0110/kbruckner/first_runs/rIAPP_GLC_2M/hbond/outputs/protein/pro_osmo"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!rIAPP_Protein_index[@]}"; do
      protein=${rIAPP_Protein_index[$i]}
      osmolyte=${osmo_index[$i]}
      xvg_file="rIAPP_GLC2M_hb_pro_osmo_rep${j}.xvg"
       echo "echo '${rIAPP_Protein_index} ${osmolyte}' | gmx_mpi hbond -f ${GLC}_rIAPP${j}.xtc -s ${GLC}_rIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
       echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."
