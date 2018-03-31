#!/bin/bash

blatherdir=/home/pi/blather/config
sentences=$blatherdir/sentences.corpus
sourcefile=$blatherdir/commands.conf
langdir=$blatherdir/language
tempfile=$blatherdir/url.txt
lmtoolurl=http://www.speech.cs.cmu.edu/cgi-bin/tools/lmtool/run

cd $blatherdir

sed -f - $sourcefile > $sentences <<EOFcommands
  /^$/d
  /^#/d
  s/\:.*$//
EOFcommands

echo "uploading corpus file and finding the resulting dictionary and language model files" | $VOICE
curl -L -F corpus=@"$sentences" -F formtype=simple $lmtoolurl \
  |grep -A 1 "base name" |grep http \
  | sed -e 's/^.*\="//' | sed -e 's/\.tgz.*$//' | sed -e 's/TAR//' > $tempfile

echo "download the dictionary and language model files" | $VOICE
curl -C - -O $(cat $tempfile).dic
curl -C - -O $(cat $tempfile).lm

echo "moving them to the right name and place" | $VOICE
mv *.dic $langdir/dic
mv *.lm $langdir/lm
echo "finishing update and removing temporary files" | $VOICE
rm $tempfile
echo "all done" | $VOICE
echo "hello master" | $VOICE
