#!/bin/bash 
PAGE="";
while [ -n "$1" ]
do
case "$1" in 
-a) PAGE=$2;;
esac
shift
done
echo -en "page $PAGE\xff\xff\xff" > /dev/ttyMOD3
exit 0