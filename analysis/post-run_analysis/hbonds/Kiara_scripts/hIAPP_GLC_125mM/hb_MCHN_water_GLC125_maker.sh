#!/bin/bash

declare -a glucose=("GLC_125")

declare -A convergence=(
    ["GLC_125"]="1000000"
)

declare -a hIAPP_MainchainNH_index=("45")

output_file="hb_MCNH_water_GLC125_hIAPP.sh"
output_dir="/mnt/c/Users/20064950/OneDrive - Curtin/IAPP/hIAPP/glucose/125/analysis/hbond"
xvg_output_dir="/scratch/pawsey0110/kiara/hIAPP/hbond/glucose/125/mainchain/MCNH_water"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!hIAPP_MainchainNH_index[@]}"; do
      water=16
      mainchainH=${hIAPP_MainchainNH_index[$i]}
      xvg_file="hb_MCNH_water_GLC125_hIAPP_rep${j}.xvg"
       echo "echo '${water} ${mainchainH}' | gmx_mpi hbond -f ${GLC}_hIAPP${j}.xtc -s ${GLC}_hIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
       echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."
