
from getFaces import (face_distance,
 getFaces,
 isfile,
 join,
 listdir,
 np,
)

import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
src_dir = os.path.dirname(current_dir)
main_dir = os.path.dirname(src_dir)
sys.path.insert(0, main_dir) 
from config import PATH

def load_npy(file):
    return list(np.load(file))

def authenticate():

    path = path.join(PATH, 'roots/')
    roots = [(path+f) for f in listdir(path) if isfile(join(path, f))] 
    if not roots:
        return False
    roots = list(map(load_npy, roots))
    face_codes = getFaces()

    if not face_codes:
        return False

    for code in face_codes:
        distances = np.array(face_distance(roots, code))
        matches = distances < 0.4
        if matches.any():
            return True
    return False

