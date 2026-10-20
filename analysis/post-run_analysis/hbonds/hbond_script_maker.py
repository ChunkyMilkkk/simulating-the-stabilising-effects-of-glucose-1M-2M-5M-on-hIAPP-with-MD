#
# Variables that require changing:
#   the updated out_file path
#   the updated xvg_out_file path
#   the points of convergence
#
import os

## Defining functions

def read_file(name):
    file = open(name)
    line = file.readline()
    contents = []
    while line:
        contents.append(line)
        line = file.readline()
    file.close()
    return contents

def write_file(name, contents):
    newfile = open(name, "w")
    for i in contents:
        newline = i
        newfile.write(newline)
    newfile.close()

def make_script(i, c, name, savePath):

    # Adjust the given script name to match either the hIAPP or rIAPP version - they have significant differences such as specified residues, specified hbond pairs, etc. The default names use hIAPP so this must be altered to rIAPP if generating a rIAPP script.
    name = name.replace("hIAPP", i)
    contents = read_file(f"Kiara_scripts/{i}_GLC_125mM/{name}")

    # Create the name of your new script based on the formatting of the old script name
    # name - name of template script
    # newname - name of your new script being created
    newname = name.replace("125", c)

    # For each line of Kiara's old script, make the following changes
    for l in range(len(contents)):
        
        # If the script makes another script, change the output path
        if "maker" in name:
            contents[l] = contents[l].replace(f"output_dir=\"/mnt/c/Users/20064950/OneDrive - Curtin/IAPP/{i}/glucose/125/analysis/hbond", f"output_dir=\"/scratch/pawsey0110/kbruckner/first_runs/{i}_GLC_{c}/hbond/inputs")
            contents[l] = contents[l].replace(f"/scratch/pawsey0110/kiara/{i}/hbond/glucose/125", f"/scratch/pawsey0110/kbruckner/first_runs/{i}_GLC_{c}/hbond/outputs")

        # Replace the concentration values on the current line and write it
        contents[l] = contents[l].replace("125", c)
        if i == "hIAPP":
            old_t = 1000000                                     # Old hIAPP convergence time in Kiara's script
            if f"[\"GLC_{c}\"]=\"{old_t}\"" in contents[l]:
                if i == "hIAPP" and c == "1M":                  # hIAPP_GLC_1M
                    t = 1275000
                elif i == "hIAPP" and c == "2M":                # hIAPP_GLC_2M
                    t = 600000
                elif i == "hIAPP" and c == "5M":                # hIAPP_GLC_5M
                    t = 300000
                else:
                    print("Note - convergence time not set")
                contents[l] = contents[l].replace(f"[\"GLC_{c}\"]=\"{old_t}\"", f"[\"GLC_{c}\"]=\"{t}\"")
        if i == "rIAPP":
            old_t = 1260000                                     # Old rIAPP convergence time in Kiara's script
            if f"[\"GLC_{c}\"]=\"{old_t}\"" in contents[l]:
                if i == "rIAPP" and c == "1M":                  # rIAPP_GLC_1M
                    t = 600000
                elif i == "rIAPP" and c == "2M":                # rIAPP_GLC_2M
                    t = 800000
                elif i == "rIAPP" and c == "5M":                # rIAPP_GLC_5M
                    t = 550000
                else:
                    print("Note - convergence time not set")
                contents[l] = contents[l].replace(f"[\"GLC_{c}\"]=\"{old_t}\"", f"[\"GLC_{c}\"]=\"{t}\"")
    write_file(savePath + f"/{newname}", contents)

## Defining variables

oneDrivePath = "/mnt/c/users/23143917/OneDrive - Curtin/IAPP_Osmolytes_2026/"

osmolyte_paths = {
    "hIAPP Glucose 1 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_1M/analysis/hbond/inputs/"),
    "hIAPP Glucose 2 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_2M/analysis/hbond/inputs/"),
    "hIAPP Glucose 5 M": os.path.join(oneDrivePath + "simulations/hIAPP/hIAPP_GLC_5M/analysis/hbond/inputs/"),
    "rIAPP Glucose 1 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_1M/analysis/hbond/inputs/"),
    "rIAPP Glucose 2 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_2M/analysis/hbond/inputs/"),
    "rIAPP Glucose 5 M": os.path.join(oneDrivePath + "simulations/rIAPP/rIAPP_GLC_5M/analysis/hbond/inputs/")
}

# As the number of hbonds is so small, broader interactions will be considered. The remaining interactions are commented out.

script_names = [                            # Output paths of each generated script for Kiara's version are described by below comments:
        #"auto_exc.sh",
        "make_all.sh",
        "hb_GLC125_submit_all.sh",
        #"hb_MCHN_GLC125_maker.sh",          # mainchain/MCNH_GLC1M
        #"hb_MCHN_water_GLC125_maker.sh",    # mainchain/MCNH_water
        #"hb_MCO_GLC125_maker.sh",           # mainchain/MCO_GLC1M
        #"hb_MCO_water_GLC125_maker.sh",     # mainchain/MCO_water
        "hb_pro-pro_GLC125_maker.sh",       # protein/pro_pro
        #"hb_sc_osmo_GLC125_maker.sh",       # protein/sc_osmo
        #"hb_sc_water_GLC125_maker.sh",      # protein/sc_water
        #"hb_osmo_osmo_GLC125_maker.sh",     # solvent/osmo_osmo
        #"hb_osmo_water_GLC125_maker.sh",    # solvent/osmo_water
        #"hb_water_water_GLC125_maker.sh",   # solvent/water_water
        "hb_pro_osmo_GLC125_maker.sh",
        "hb_pro_water_GLC125_maker.sh",
]

## Beginning code

for name, path in osmolyte_paths.items():

    # Ensure a directory exists for these scripts
    os.makedirs(path, exist_ok=True)
    
    # Get details from dic key
    name_list = name.split()
    IAPP = name_list[0]
    conc = name_list[2] + name_list[3] # Join the value of the concentration with it's units, as this is how the make_script() function is formatted

    print(f"Processing: IAPP:{IAPP}\t\t\tconc:{conc}")

    # Create scripts
    for scr_name in script_names:
        make_script(IAPP, conc, scr_name, path)

