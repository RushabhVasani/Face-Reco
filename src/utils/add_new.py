from os import system
import config

import getFaces

CRED = '\33[91m'
CGRN = '\33[42m'
CEND = '\33[0m'

if __name__ == '__main__':
    path = config.PATH + 'roots/'
    system(f"sudo chattr -R -i {path}")
    system(f"sudo chmod -R ugo+rw {path}")
    for i in range(10):
        
        try:
            getFaces.getFaces(training=True, model_n=i)
        except:
            system(f"sudo chmod -R ugo-w {path}")
            system(f"sudo chattr -R +i {path}")
            print("\n" + CRED + "Process ended before Completion due to an error!" + CEND)
            print(f"{i} out of 10 were models trained succesfully.")
            exit()

    system(f"sudo chmod -R ugo-w {path}")
    system(f"sudo chattr -R +i {path}")
    print("\n\nModel Training: Successful")
