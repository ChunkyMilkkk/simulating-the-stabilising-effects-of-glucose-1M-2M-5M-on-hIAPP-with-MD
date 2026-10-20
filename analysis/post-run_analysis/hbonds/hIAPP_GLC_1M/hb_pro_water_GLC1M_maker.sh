#!/bin/bash

declare -a glucose=("GLC_1M")

declare -A convergence=(
    ["GLC_1M"]="1275000"
)

declare -a hIAPP_Protein_index=("1")
declare -a water_index=("16")

output_file="hb_pro_water_GLC1M_hIAPP.sh"
output_dir="/scratch/pawsey0110/kbruckner/first_runs/hIAPP_GLC_1M/hbond/inputs"
xvg_output_dir="/scratch/pawsey0110/kbruckner/first_runs/hIAPP_GLC_1M/hbond/outputs/protein/pro_water"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!hIAPP_Protein_index[@]}"; do
      protein=${hIAPP_Protein_index[$i]}
      water=${water_index[$i]}
      xvg_file="hIAPP_GLC1M_hb_pro_water_rep${j}.xvg"
       echo "echo '${protein} ${water}' | gmx_mpi hbond -f ${GLC}_hIAPP${j}.xtc -s ${GLC}_hIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
       echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."
