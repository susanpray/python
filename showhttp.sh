#!/bin/bash
echo `netstat -nat | grep -i "80" | wc -l`
