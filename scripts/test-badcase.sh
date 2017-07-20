#! /bin/bash 
###########################################
# Test
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
CHOP_LOG_LVL=DEBUG
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
source ~/venv-py3/bin/activate
python chop/test.py ChopTest.test_basecase
