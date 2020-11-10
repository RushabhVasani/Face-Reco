import sys
import numpy as np

from os import listdir, system
from os.path import isfile, join

if __name__ == '__main__':

    sp = np.array(sys.path)
    np.save("/usr/lib/Auth/Facerec/deps_path.npy", sp)

    path = "/etc/pam.d/"
    pamd = [f for f in listdir(path) if isfile(join(path, f))]

    if "common-auth-orig" not in pamd:
        system("sudo cp /etc/pam.d/common-auth /etc/pam.d/common-auth-orig")

    system("sudo python3 /usr/lib/Auth/Facerec/comm_auth_orig.py")
    system("sudo python3 /usr/lib/Auth/Facerec/cli_info.py")

