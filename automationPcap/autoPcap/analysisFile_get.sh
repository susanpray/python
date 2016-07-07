#!/bin/bash
if [ $# -lt 2 ]
then
	echo "please using ./analysisFile_get.sh [port] [pcapfile]"
else
	python -u capture_last.py $1 $2 > capture_analysisToFile.log
fi
