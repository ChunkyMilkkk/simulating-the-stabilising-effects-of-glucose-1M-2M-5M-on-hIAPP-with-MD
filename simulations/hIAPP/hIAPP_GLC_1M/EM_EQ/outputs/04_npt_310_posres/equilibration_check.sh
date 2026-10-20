#!/usr/bin/env bash

# Execute in 04_npt_310_posres directory after equilibration

set -Eeuo pipefail

trap 'echo "Error near line $LINENO"' ERR

RUN_DIR="${1:-04_npt_310_posres}"
DEFFNM="${2:-$(basename "$RUN_DIR")}"
OUTDIR="${3:-equil_analysis}"

mkdir -p "$OUTDIR"

GMX="${GMX:-gmx}"

TPR="${DEFFNM}.tpr"
EDR="${DEFFNM}.edr"
XTC="${DEFFNM}.xtc"

energy_one () {
    local term="$1"
    local stem="$2"

    printf "%s\n0\n" "$term" | $GMX energy \
        -f "$EDR" \
        -o "${OUTDIR}/${stem}.xvg" \
        -xvg none
}

energy_one "Temperature" "temperature"
energy_one "Pressure" "pressure"
energy_one "Density" "density"
energy_one "Volume" "volume"
energy_one "Potential" "potential_energy"

printf "Box-X\nBox-Y\nBox-Z\n0\n" | $GMX energy \
    -f "$EDR" \
    -o "${OUTDIR}/box_dimensions.xvg" \
    -xvg none

printf "Protein\nSystem\n" | $GMX trjconv \
    -s "$TPR" \
    -f "$XTC" \
    -o "${OUTDIR}/${DEFFNM}_center.xtc" \
    -pbc mol \
    -center

printf "Backbone\nProtein\n" | $GMX trjconv \
    -s "$TPR" \
    -f "${OUTDIR}/${DEFFNM}_center.xtc" \
    -o "${OUTDIR}/${DEFFNM}_protein_fit.xtc" \
    -fit rot+trans

printf "Backbone\nBackbone\n" | $GMX rms \
    -s "$TPR" \
    -f "${OUTDIR}/${DEFFNM}_protein_fit.xtc" \
    -o "${OUTDIR}/backbone_rmsd.xvg" \
    -tu ns \
    -xvg none

printf "Protein\n" | $GMX gyrate \
    -s "$TPR" \
    -f "${OUTDIR}/${DEFFNM}_protein_fit.xtc" \
    -o "${OUTDIR}/radius_gyration.xvg" \
    -xvg none
