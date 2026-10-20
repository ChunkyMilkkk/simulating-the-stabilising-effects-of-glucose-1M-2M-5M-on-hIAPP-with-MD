#
# Variables that require changing:
#   the updated out_file path
#   the updated xvg_out_file path
#   the points of convergence
#
import os

def read_file(name):
    file = open(name)
    line = file.readline()
    contents = []
    while line:
        contents.append(line)
        line = file.readline()
    file.close()
    return contents

def make_script(concentrations, IAPP, name):
    contents = read_file(f"hIAPP_GLC_1M/{name}")
    for i in IAPP:
        for c in concentrations:
            if i == "hIAPP" and c == "1M":
                print("Processing input")
            else:
                newname = name.replace("1M", c)
                newname = newname.replace("hIAPP", i)
                with open(f"hIAPP_GLC_1M/{script}", "r") as infile, open(i + "_GLC_" + c + f"/{newname}", "w") as outfile:
                    for line in infile:
                        # Replace the value on the current line and write it
                        updated_line = line.replace("1M", c)
                        updated_line = updated_line.replace("hIAPP", i)
                        outfile.write(updated_line)

## Defining variables

concentrations = ["1M", "2M", "5M"]

IAPP = ["hIAPP", "rIAPP"]

dirs = ["hIAPP_GLC_1M", "hIAPP_GLC_2M", "hIAPP_GLC_5M", "rIAPP_GLC_1M", "rIAPP_GLC_2M", "rIAPP_GLC_5M"]

script_names = ["met_file_prep_GLC_1M_hIAPP.py", "met_input_GLC_1M_hIAPP.in"]

## Beginning code

for d in dirs:
    os.makedirs(d, exist_ok=True)

for name in script_names:
    make_script(concentrations, IAPP, name)

