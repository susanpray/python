#!/bin/bash
scport=$1
dstport=$2

if [ $# -lt 2 ]
then
	echo "please using ./flow_search.sh [scport] [dstport]"
else
	./flow_search.sh $scport $dstport > es_getlast.log
	grep source es_getlast.log | awk -F '{' '{print$2}'|awk -F '}' '{print$1}' > pkt_info.log
fi
