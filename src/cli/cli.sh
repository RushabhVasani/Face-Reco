#!/bin/bash

FILE=/usr/share/pam-configs/Facerec

function facerec(){
if [ "$1" = "new" ]; then
    sudo python3 /lib/Auth/Facerec/add_new.py


elif [ "$1" = "enable" ]; then
    sudo cp /lib/Auth/Facerec/Facerec /usr/share/pam-configs/
    sudo pam-auth-update --package
    echo "Enabling facerec... Done"


elif [ "$1" = "disable" ]; then
    if test -f "$FILE"; then
        sudo rm /usr/share/pam-configs/Facerec
    fi
    sudo pam-auth-update --package
    echo "Disabling facerec... Done"


elif [ "$1" = "remove" ]; then
    if test -f "$FILE"; then
        sudo rm /usr/share/pam-configs/Facerec
    fi
    echo "Removing CLI... Done"
    sudo python3 /lib/Auth/Facerec/remove_cli.py
    sudo chattr -R -i /lib/Auth/
    sudo rm -r /lib/Auth

    sudo rm /usr/share/bash-completion/completions/facerec
    echo "Removing facerec file system... Done"

    echo "Resetting pam-auth... Done"
    sudo pam-auth-update --package
    echo "facerec has been removed completely!"


elif [ "$1" = "--help" ]; then
    python3 /lib/Auth/Facerec/cli_info.py


elif [ "$1" = "--version" ]; then
    python3 /lib/Auth/Facerec/_version.py

fi
}

