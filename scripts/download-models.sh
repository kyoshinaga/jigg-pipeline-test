#!/bin/sh

WORKDIR=`dirname $0`/..
MODELDIR=$WORKDIR/models

# stanford corenlp
CORENLP="http://nlp.stanford.edu/software/stanford-english-corenlp-2016-01-10-models.jar"
if [ -e $MODELDIR/stanford-english-corenlp-2016-01-10-models.jar ];
then
  echo "Stanford CoreNLP models exist."
else
  wget $CORENLP -P $MODELDIR
  jar xvf $MODELDIR/stanford-english-corenlp-2016-01-10-models.jar
  rm -rf META-INF/
fi

# berkeleyparser
BERKELEYPARSER="https://github.com/slavpetrov/berkeleyparser/raw/master/eng_sm6.gr"
if [ -e $MODELDIR/eng_sm6.gr ];
then
  echo "BerkeleyParser grammar file exists."
else
  wget $BERKELEYPARSER -P $MODELDIR
fi

cd $WORKDIR
