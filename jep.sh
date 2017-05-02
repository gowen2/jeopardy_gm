#!/bin/bash

#This script should ALWAYS be in same directory as jeopardy.py

#Gets full path of this bash script (jep.sh)
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
PYPATH="${SCRIPTPATH}/jeopardy.py"
python "$PYPATH"
