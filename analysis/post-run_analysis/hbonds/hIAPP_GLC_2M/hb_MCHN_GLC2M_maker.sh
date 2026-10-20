#!/bin/bash

declare -a glucose=("GLC_2M")

declare -A convergence=(
    ["GLC_2M"]="600000"
)

declare -a hIAPP_MainchainNH_index=("45")
declare -a Osmolyte_GLC2M_index=("12")

output_file="hb_MCNH_GLC2M_hIAPP.sh"
output_dir="/scratch/pawsey0110/kbruckner/first_runs/hIAPP_GLC_2M/hbonds/inputs"
xvg_output_dir="/scratch/pawsey0110/kbruckner/first_runs/hIAPP_GLC_2M/hbonds/outputs/mainchain/MCNH_GLC2M"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!hIAPP_MainchainNH_index[@]}"; do
      osmolyte=${Osmolyte_GLC2M_index[$i]}
      mainchainH=${hIAPP_MainchainNH_index[$i]}
      xvg_file="hb_MCNH_GLC2M_hIAPP_rep${j}.xvg"
       echo "echo '${osmolyte} ${mainchainH}' | gmx_mpi hbond -f ${GLC}_hIAPP${j}.xtc -s ${GLC}_hIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
       echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."