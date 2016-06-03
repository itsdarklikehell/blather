#!/bin/bash
#
# This script will crawl weather.com link
# and provide you with very basic weather information
# for the next 3-4 hrs.
# You have to modify LINK variable to get information
# for your city/zip.
#


CURL="/usr/bin/curl -s"
LINK="https://weather.com/weather/hourbyhour/l/NLXX0012:1:NL"
NEXTHR=$(date +%I%M --date="next hour" )
THIRDHR=$(date +%I%M --date="2 hour" )
FOURHR=$(date +%I%M --date="3 hour" )


GETHOUR() {
TIME="$1"
MINUTES=$(echo ${TIME} | sed -e 's/^..//')     # get minutes of given time
HOURS=$(echo ${TIME} | sed 's/\(.*\)../\1/')    # get hrs of given time
HALFHOUR=$(echo "${HOURS}30")
if [ "${TIME}" -lt "${HALFHOUR}" ]; then
   if [ "${HOURS}" -lt "10" ]; then
    HOUR=`echo ${TIME} |  sed 's/\(.*\)../\1/' | sed -e 's/^.//'`
   elif [ "${HOURS}" -ge "10" ]; then
# at this point we might have hrs between 10-12 in first half
    HOUR=`echo ${TIME} | sed 's/\(.*\)../\1/'`
   elif [ "${HOURS}" -eq "12" ]; then
    HOUR="12"
   fi
elif [ "${TIME}" -ge "${HALFHOUR}" ]; then
   if [ "${HOURS}" -eq "12" ]; then
    HOUR="1"
   elif [ "${HOURS}" -lt "09" ]; then
    HOUR=`echo ${TIME} | sed -e 's/^.//' | sed 's/\(.*\)../\1/'`
   elif [ "${HOURS}" -eq "09" ]; then
    HOUR="10"
   elif [ "${HOURS}" -ge "10" ] && [ "${HOURS}" -lt "12" ]; then
# at this point we might have hrs between 10-12 in second half
    HOUR=`echo ${TIME} | sed 's/\(.*\)../\1/'`
   fi
fi
}

WEATHERARRAY=($(${CURL} ${LINK} | sed -n "/Updated:/,/<\/dl>/p" | sed "s/<[^>]*>//g" | sed '/^$/d' | grep -v "`date +%a`" | grep -v "`date +%b`" | sed -e '1,2d' | sed -e 's/&//' ) )

GETHOUR "${NEXTHR}"
WEATHERARRAY_NEXTHR=($(${CURL} ${LINK} | sed -n "/<h3 class=\"wx-time\">`echo "${HOUR}"`<span class=\"wx-meridian\">/,/<\/dl>/p" | sed "s/<[^>]*>//g" | sed '/^$/d' | grep -v "`date +%a`" | grep -v "`date +%b`" | sed -e 's/&//'))
GETHOUR "${THIRDHR}"
WEATHERARRAY_3HR=($(${CURL} ${LINK} | sed -n "/<h3 class=\"wx-time\">`echo "${HOUR}"`<span class=\"wx-meridian\">/,/<\/dl>/p" | sed "s/<[^>]*>//g" | sed '/^$/d' | grep -v "`date +%a`" | grep -v "`date +%b`" | sed -e 's/&//' ))
GETHOUR "${FOURHR}"
WEATHERARRAY_4HR=($(${CURL} ${LINK} | sed -n "/<h3 class=\"wx-time\">`echo "${HOUR}"`<span class=\"wx-meridian\">/,/<\/dl>/p" | sed "s/<[^>]*>//g" | sed '/^$/d' | grep -v "`date +%a`" | grep -v "`date +%b`" | sed -e 's/&//'))


echo -e "Temperature for `echo ${WEATHERARRAY[@]:0:2}` : `echo ${WEATHERARRAY[@]:2:1}` and outside should be: `echo ${WEATHERARRAY[@]:3:1}` - `echo ${WEATHERARRAY[@]:4:7}`"
echo -e "Temperature for `echo ${WEATHERARRAY_NEXTHR[@]:0:2}` : `echo ${WEATHERARRAY_NEXTHR[@]:2:1}` and outside should be: `echo ${WEATHERARRAY_NEXTHR[@]:3:1}` - `echo ${WEATHERARRAY_NEXTHR[@]:4:7}`"
echo -e "Temperature for `echo ${WEATHERARRAY_3HR[@]:0:2}` : `echo ${WEATHERARRAY_3HR[@]:2:1}` and outside should be: `echo ${WEATHERARRAY_3HR[@]:3:1}` - `echo ${WEATHERARRAY_3HR[@]:4:7}`"
echo -e "Temperature for `echo ${WEATHERARRAY_4HR[@]:0:2}` : `echo ${WEATHERARRAY_4HR[@]:2:1}` and should be: `echo ${WEATHERARRAY_4HR[@]:3:1}` - `echo ${WEATHERARRAY_4HR[@]:4:7}`"
