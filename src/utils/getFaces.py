import sys
import numpy as np

import config

deps_path = list(np.load(config.PATH + 'deps_path.npy'))
sys.path = deps_path + [path for path in sys.path if path not in deps_path]

from os import listdir, system
from os.path import isfile, join

from cv2 import VideoCapture, destroyAllWindows, imshow, resize, waitKey
from face_recognition import face_encodings, face_locations, face_distance

CRED = '\033[91m'
CEND = '\033[0m'
CSEL = '\33[7m'

def getFaces(training=False, model_n=0):

    path = config.PATH + 'roots/'
    if training:
        if not model_n:
            print("\nFacerec will store 10 different models of your face to master your face.")
            print("Try to give a slightly different pose and distance from the camera each time [Smiling, Normal, etc.].")
        print(f"\nmodel: {model_n+1}")
        print("\nThere shold be exactly one person in frount of the camera!")
        print(CSEL + "Press [ENTER] to proceed: " + CEND, end="")
        input()
    saved=False
    cap = VideoCapture(0)
    loop_count = 0
    while not saved:
        loop_count += 1
        _, img = cap.read()
        img = img[:, :, ::-1]

        rgb_small_frame = resize(img, (0, 0), fx=0.25, fy=0.25)
        face_locs = face_locations(rgb_small_frame)
        face_code = face_encodings(rgb_small_frame, face_locs)

        if len(face_locs) == 1:
            if not training:
                return face_code
            try:
                root_models = [f for f in listdir(path) if isfile(join(path, f))]
                a = len(root_models)
            except:
                a = 0
            face_code = np.array(face_code[0])
            np.save(f"{path}root-{a}.npy", face_code)
            saved = True

        else:
            if training:
                imshow("Image", img)

            if len(face_code) > 1:
                if not training:
                    return face_code
                cap.release()
                destroyAllWindows()
                raise Exception(CRED + "facerec found more than one faces!" + CEND)
            else:
                if loop_count > 200:
                    cap.release()
                    destroyAllWindows()
                    raise Exception(CRED + "facerec couldn't detect any face!" + CEND)

        if waitKey(1) & 0xFF == ord('q'):
            cap.release()
            destroyAllWindows()    

    cap.release()
    destroyAllWindows()
