#!/bin/bash

declare -a glucose=("GLC_1M")

declare -A convergence=(
    ["GLC_1M"]="600000"
)

declare -a osmo_index=("12")

output_file="hb_osmo_osmo_GLC1M_rIAPP.sh"
output_dir="/scratch/pawsey0110/kbruckner/first_runs/rIAPP_GLC_1M/hbonds/inputs"
xvg_output_dir="/scratch/pawsey0110/kbruckner/first_runs/rIAPP_GLC_1M/hbonds/outputs/solvent/osmo_osmo"

mkdir -p "$output_dir"
echo "#!/bin/bash" > "$output_dir/$output_file"
echo "mkdir -p $xvg_output_dir" >> "$output_dir/$output_file"

for j in {0..2}; do
  for GLC in "${glucose[@]}"; do
    for i in "${!osmo_index[@]}"; do
      osmo=${osmo_index[$i]}
      xvg_file="rIAPP_GLC1M_hb_osmo_osmo_rep${j}.xvg"
       echo "echo '${osmo} ${osmo}' | gmx_mpi hbond -f ${GLC}_rIAPP${j}.xtc -s ${GLC}_rIAPP${j}.tpr -n index.ndx -a 37 -b ${convergence[$GLC]} -num ${xvg_file}" >> "$output_dir/$output_file"
       echo "mv ${xvg_file} $xvg_output_dir/" >> "$output_dir/$output_file"
    done
  done
done

chmod +x "$output_dir/$output_file"
echo "Script $output_file has been generated and made executable."