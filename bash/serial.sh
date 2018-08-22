#!/bin/bash 
stty -F /dev/ttyMOD3 ospeed 9600 ispeed 9600 raw clocal -parenb -echo cs8 
CR="$(echo -e '\r')"
exec 4<> /dev/ttyMOD3

cat <&4 | while :
do
    IFS="$CR" read -r line 
    case "$line" in
    quit*)
        break
        ;;
    *)

	if [[ -n "$line"  ]]; then
	    echo $line
   		mosquitto_pub -t /devices/screen/controls/raw/meta/type  -r  -m text
		mosquitto_pub -t /devices/screen/controls/raw/on  -r  -m "$line"
	fi

        ;;
    esac
done