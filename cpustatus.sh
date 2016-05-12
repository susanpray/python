#!/bin/bash
#a = 'date  +%Y-%m-%d-%H:%M:%S'
top|grep snmpd|echo 'date  +%Y-%m-%d-%H:%M:%S'|awk '{if($10 > 0){print $10}}' >> sss.log

