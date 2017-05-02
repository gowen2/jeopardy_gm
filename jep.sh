#!/bin/bash

#This script should ALWAYS be in same directory as jeopardy.py

#Gets full path of this bash script (jep.sh)
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

#Gets full path of jeopardy.py script
PYPATH="${SCRIPTPATH}/jeopardy.py"

#Runs jeopardy.py script
python3 "$PYPATH"
