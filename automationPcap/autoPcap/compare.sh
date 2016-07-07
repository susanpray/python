#!/bin/bash
path="/root/git/testing/automationPcap/autoPcap"
SendPkt=`cat $path/pkginfo_total.log|grep SendPkt|awk -F ': ' '{print $2}'`
SendLen=`cat $path/pkginfo_total.log|grep SendLen|awk -F ': ' '{print $2}'`
RecPkt=`cat $path/pkginfo_total.log|grep RecPkt|awk -F ': ' '{print $2}'`
Reclen=`cat $path/pkginfo_total.log|grep Reclen|awk -F ': ' '{print $2}'`

SendPkt_ES=`cat $path/ES/pkt_info.log|awk -F ',' '{print$1}'|awk -F ':' '{print$2}'`
SendLen_ES=`cat $path/ES/pkt_info.log|awk -F ',' '{print$4}'|awk -F ':' '{print$2}'`
RecPkt_ES=`cat $path/ES/pkt_info.log|awk -F ',' '{print$3}'|awk -F ':' '{print$2}'`
Reclen_ES=`cat $path/ES/pkt_info.log|awk -F ',' '{print$2}'|awk -F ':' '{print$2}'`

echo "=================================================================="
compare()
{
if [ $2 -eq $3 ]; then
	echo "$1 [$2] is equal to $4[$3]-------PASS"
else
	echo "$1 [$2] is not equal to $4[$3]--------FAIL"
fi
}


compare "SendPkt" $SendPkt $SendPkt_ES "SendPkt_ES"
compare "SendLen" $SendLen $SendLen_ES "SendLen_ES"
compare "RecPkt" $RecPkt $RecPkt_ES "RecPkt_ES"
compare "Reclen" $Reclen $Reclen_ES "Reclen_ES"

echo "=================================================================="