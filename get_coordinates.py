import argparse
from pathlib import Path
import numpy as np
from xml2dict import xml2dict


units = {'Hartree': 0.52917721090380, 'bohr': 5.29177210903e-11 / 1e-10}


def main(path):

    data_dict = xml2dict(path)

    coef= units[data_dict['@Units'].split()[0]]

    atoms = ""

    for item in data_dict['output']['atomic_structure']['atomic_positions']['atom']:
         atoms += item['@name'] + " " + " ".join(str(x * units['bohr']) for x in item['$'])+ "\n"

    print(atoms)

    return atoms


if __name__=='__main__':

    import os

    #var=$(python3 get_cell.py /Users/mykhailoklymenko/data-file-schema.xml)

    # parser = argparse.ArgumentParser()
    # parser.add_argument("path")
    # args = parser.parse_args()
    # path = Path(args.path)
    #
    # if not path.exists():
    #     print("The target directory doesn't exist")
    #     raise SystemExit(1)

    path = os.path.expanduser('~/biphenelene_x_2.xml')
    cell = main(path)
