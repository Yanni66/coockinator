#!/bin/bash 
TEXT="";
UNIT="";
while [ -n "$1" ]
do
case "$1" in 
-a) UNIT=$2;;
-b) TEXT=$2;;
esac
shift
done
echo -en "$UNIT.val=$TEXT\xff\xff\xff" > /dev/ttyMOD3
exit 0