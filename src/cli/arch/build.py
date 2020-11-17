import sys
import numpy as np

from os import  system

if __name__ == '__main__':

    sp = np.array(sys.path)
    np.save("/usr/lib/Auth/Facerec/deps_path.npy", sp)
    system("sudo python3 /usr/lib/Auth/Facerec/cli_info.py")

