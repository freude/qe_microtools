import argparse
from pathlib import Path
import numpy as np
from xml2dict import xml2dict


units = {'Hartree': 0.52917721090380}


def main(path):

    data_dict = xml2dict(path)

    coef= units[data_dict['@Units'].split()[0]]

    a1 = data_dict['output']['atomic_structure']['cell']['a1']
    a2 = data_dict['output']['atomic_structure']['cell']['a2']
    a3 = data_dict['output']['atomic_structure']['cell']['a3']

    cell = np.vstack((a1, a2, a3)) * coef

    print(str(cell).replace(' [', '').replace('[', '').replace(']', ''))

    return cell


if __name__=='__main__':

    #var=$(python3 get_cell.py /Users/mykhailoklymenko/data-file-schema.xml)

    # parser = argparse.ArgumentParser()
    # parser.add_argument("path")
    # args = parser.parse_args()
    # path = Path(args.path)
    #
    # if not path.exists():
    #     print("The target directory doesn't exist")
    #     raise SystemExit(1)

    import os
    path = os.path.expanduser('~/biphenelene_x_2.xml')
    cell = main(path)
