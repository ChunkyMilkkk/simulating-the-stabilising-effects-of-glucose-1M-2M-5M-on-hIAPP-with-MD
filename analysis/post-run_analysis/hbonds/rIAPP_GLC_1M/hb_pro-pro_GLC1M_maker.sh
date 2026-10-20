#!/bin/bash

declare -a glucose=("GLC_1M")

declare -A convergence=(
    ["GLC_1M"]="600000"
)

declare -a rIAPP_Protein_index=("1")

output_file="hb_pro_pro_GLC1M_rIAPP.sh"
output_dir="/scratch/pawsey0110/kbruckner/first_runs/rIAPP_GLC_1M/hbond/inputs"
xvg_output_dir="/scratch/pawsey0110/kbruckner/first_runs/rIAPP_GLC_1M/hbond/outputs/protein/pro_pro"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!rIAPP_Protein_index[@]}"; do
      protein=${rIAPP_Protein_index[$i]}
      xvg_file="rIAPP_GLC1M_hb_pro_pro_rep${j}.xvg"
       echo "echo '${protein} ${protein}' | gmx_mpi hbond -f ${GLC}_rIAPP${j}.xtc -s ${GLC}_rIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
       echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."
