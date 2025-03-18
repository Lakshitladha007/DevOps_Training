#!/bin/bash
 
THRESHOLD=80
 
USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
 
if [ "$USAGE" -gt "$THRESHOLD" ];
then
    MESSAGE="Warning: Disk usage has exceeded ${THRESHOLD}% (Current: ${USAGE}% on $(hostname))"
   
    echo "$MESSAGE" | mail -s "Disk Space Alert on $(hostname)" lakshitladha@gmail.com
fi