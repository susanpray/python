#!/bin/bash
if [ -s capture_analysisToFile.log ]
then
	echo "get the related parameters to file"	
	tail -20 capture_analysisToFile.log |grep -E 'SendPkt|SendLen|RecPkt|Reclen' > pkginfo_total.log
fi

exit
