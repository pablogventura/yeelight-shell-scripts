#!/usr/bin/env bash

redshift -p &> redshift_out
string=$(cat redshift_out | grep color)
temp=$(echo $string | tr -d -c 0-9)
bright=$(python -c "print(round($temp*0.02-30))")
#echo $temp
temp=$(python -c "print(min((max((round($temp-500)),4000)),5900))")  #adjust constants for your preference
#echo $temp
$( dirname $0 )/yeelight-colortemp.sh 0 $temp
$( dirname $0 )/yeelight-brightness.sh 0 100