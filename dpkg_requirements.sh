#!/bin/sh
DEPS = "python3-pip python3-opencv python3-setuptools python-execnet cmake libatlas-base-dev build-essential"
apt-get update
apt-get install -y $DEPS
#etc.