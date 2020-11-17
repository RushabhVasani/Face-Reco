#!/bin/bash

FILE=/usr/share/pam-configs/Facerec
SUDO=/etc/pam.d/sudo
TEXT='auth      sufficient   pam_python.so /lib/Auth/Facerec/pam.py'

function facerec(){
if [ "$1" = "new" ]; then
    sudo python3 /usr/lib/Auth/Facerec/add_new.py


elif [ "$1" = "enable" ]; then
    if grep -q $TEXT $SUDO;then
      echo "alred"
    else
      sudo echo $TEXT >> $SUDO
      echo "done"
    fi
    echo "Enabling facerec... Done"


elif [ "$1" = "disable" ]; then
    if grep -q $TEXT $SUDO;then
      sed -i $TEXT $SUDO
    else
      echo "NotE"
    fi
    echo "Disabling facerec... Done"


elif [ "$1" = "remove" ]; then
    if test -f "$FILE"; then
        sudo rm /usr/share/pam-configs/Facerec
    fi
    echo "Removing CLI... Done"
    sudo python3 /usr/lib/Auth/Facerec/remove_cli.py
    sudo chattr -R -i /usr/lib/Auth/
    sudo rm -r /usr/lib/Auth

    sudo rm /usr/share/bash-completion/completions/facerec
    echo "Removing facerec file system... Done"

    echo "Resetting pam-auth... Done"
    sudo pam-auth-update --package
    echo "facerec has been removed completely!"


elif [ "$1" = "--help" ]; then
    python3 /usr/lib/Auth/Facerec/cli_info.py


elif [ "$1" = "--version" ]; then
    python3 /usr/lib/Auth/Facerec/_version.py

fi
}

