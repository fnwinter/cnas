#!/bin/bash
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
pushd $SCRIPT_DIR

echo "# update code"
git pull origin main

echo "# set venv"
python3 -m pip install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r cnas/requirements.txt

echo "# run cherrynas"
pushd cnas
flask --app cnas run
popd

popd
