#!/bin/bash

WORKSHEET_URL=""
NAME=""

read -p "Work schedule URL: " $WORKSHEET_URL
read -p "Name to find: " $NAME

python3 makecfg.py $WORKSHEET_URL $NAME
