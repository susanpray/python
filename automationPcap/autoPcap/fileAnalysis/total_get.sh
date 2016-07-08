#!/bin/bash
#path="/root/git/testing/automationPcap/autoPcap/fileAnalysis"


if [ $# -lt 1 ]
then
	echo "please using ./total_get.sh [pcapfile]"
else
	#cd $path
	python -u file_analysis_susan.py $1 > /tmp/11.log
	tail -11 /tmp/11.log|grep -E 'SendPkt|SendLen|RecPkt|Reclen' > pkginfo_local.log
	
fi
