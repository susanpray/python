
==============192.168.24.106========================
####create pcap and analysis pcap to [capture_analysisToFile.log]

./analysisFile_get.sh 25 smtp8888


####send smtp mail

 python smtp_send.py
 

####get the finnal send and receive pkgs to [cat /root/git/testing/automationPcap/autoPcap/pkginfo_total.log]

 ./pkginfo_get.sh
 

####put the pcap to the send traffic machine

 scp pcap/smtp8888.pcap 192.168.24.82:/root
 ./send_pcap.sh smtp8888.pcap 10 em2 1 (send it in traffic machine 192.168.24.82)
 

####get the ES send and receive pkgs info to [cat /root/git/testing/automationPcap/autoPcap/ES/pkt_info.log]

/root/git/testing/automationPcap/autoPcap/ES/flow_searchToFile.sh 37376 25


####compare the original [pkginfo_total.log] with the ES [pkt_info.log]

/root/git/testing/automationPcap/autoPcap/compare.sh 








