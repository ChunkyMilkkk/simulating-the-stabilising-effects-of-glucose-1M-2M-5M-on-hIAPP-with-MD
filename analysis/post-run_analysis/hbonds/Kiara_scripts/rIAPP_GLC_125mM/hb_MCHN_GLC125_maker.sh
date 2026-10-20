#!/bin/bash

declare -a glucose=("GLC_125")

declare -A convergence=(
    ["GLC_125"]="1260000"
)

declare -a rIAPP_MainchainNH_index=("43")
declare -a Osmolyte_GLC125_index=("12")

output_file="hb_MCNH_GLC125_rIAPP.sh"
output_dir="/mnt/c/Users/20064950/OneDrive - Curtin/IAPP/rIAPP/glucose/125/analysis/hbond"
xvg_output_dir="/scratch/pawsey0110/kiara/rIAPP/hbond/glucose/125/mainchain/MCNH_GLC125"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!rIAPP_MainchainNH_index[@]}"; do
      osmolyte=${Osmolyte_GLC125_index[$i]}
      mainchainH=${rIAPP_MainchainNH_index[$i]}
      xvg_file="hb_MCNH_GLC125_rIAPP_rep${j}.xvg"
       echo "echo '${osmolyte} ${mainchainH}' | gmx_mpi hbond -f ${GLC}_rIAPP${j}.xtc -s ${GLC}_rIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
       echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."
