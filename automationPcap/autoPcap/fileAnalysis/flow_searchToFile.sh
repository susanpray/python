#!/bin/bash
scport=$1
dstport=$2
networkIP=$3
#path="/root/git/testing/automationPcap/autoPcap"

if [ $# -lt 2 ]
then
	echo "please using ./flow_search.sh [scport] [dstport] [networkIP]"
else
	./flow_search.sh $scport $dstport $networkIP> /tmp/es_getlast.log
	grep source /tmp/es_getlast.log | awk -F '{' '{print$2}'|awk -F '}' '{print$1}' > pkginfo_ES.log
fi
