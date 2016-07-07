#!/bin/bash
scport=$1
dstport=$2
path="/root/git/testing/automationPcap/autoPcap"

if [ $# -lt 2 ]
then
	echo "please using ./flow_search.sh [scport] [dstport]"
else
	$path/ES/flow_search.sh $scport $dstport > $path/ES/es_getlast.log
	grep source $path/ES/es_getlast.log | awk -F '{' '{print$2}'|awk -F '}' '{print$1}' > $path/ES/pkt_info.log
fi
