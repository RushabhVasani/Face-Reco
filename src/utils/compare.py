from getFaces import (face_distance,
 getFaces,
 isfile,
 join,
 listdir,
 np,
)

import config

def load_npy(file):
    return list(np.load(file))

def authenticate():

    path = config.PATH + 'roots/'
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
