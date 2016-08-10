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

# mecab
if type "crf_learn" > /dev/null;
then
  echo "CRF++ exists"
else
  git clone https://github.com/taku910/crfpp.git $MODELDIR/crfpp
  cd  $MODELDIR/crfpp
  ./autogen.sh
  sed -i '/#include "winmain.h"/d' crf_test.cpp
  sed -i '/#include "winmain.h"/d' crf_learn.cpp
  make
  sudo make install
  sudo ldconfig
fi

if type "mecab" > /dev/null;
then
  echo "mecab source exists"
else
  git clone https://github.com/taku910/mecab.git $MODELDIR/mecab
  cd  $MODELDIR/mecab/mecab
  ./autogen.sh
  make
  sudo make install
  cd $MODELDIR/mecab/mecab-ipadic
  ./configure --with-charset=utf8
  make
  sudo make install
  sudo ldconfig
fi

# cabocha
if type "cabocha" > /dev/null;
then
  echo "cabocha source exists."
else
  git clone https://github.com/taku910/cabocha.git $MODELDIR/cabocha
  cd $MODELDIR/cabocha
  ./autogen.sh --with-charset=utf8
  make
  sudo make install
fi

# juman
JUMAN="http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/juman/juman-7.01.tar.bz2&name=juman-7.01.tar.bz2"
if type "juman" > /dev/null;
then
  echo "juman source exists."
else
  wget -P $MODELDIR $JUMAN
  cd $MODELDIR
  tar jxvf juman-7.01.tar.bz2
  cd $MODELDIR/juman-7.01
  ./configure
  make
  sudo make install
fi

# knp
KNP="http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/knp-4.16.tar.bz2&name=knp-4.16.tar.bz2"
if type "knp" > /dev/null;
then
  echo "KNP exists."
else
  wget -P $MODELDIR $KNP
  cd $MODELDIR
  tar jxvf knp-4.16.tar.bz2
  cd knp-4.16
  ./configure
  make
  sudo make install
fi

# syntaxnet
BAZEL="https://github.com/bazelbuild/bazel/releases/download/0.2.2b/bazel_0.2.2b-jdk7-linux-x86_64.deb"
if type "bazel" > /dev/null;
then
  echo "bazel exists."
else
  wget -P $MODELDIR $BAZEL
  cd $MODELDIR
  sudo dpkg -i bazel_0.2.2b-jdk7-linux-x86_64.deb
  sudo apt-get -y -q install swig
fi

SYNTAXNET="https://github.com/tensorflow/models.git"
if [ -d $MODELDIR/syntaxnet ];
then
  echo "syntaxnet exists."
else
  git clone --recursive $SYNTAXNET $MODELDIR/syntaxnet
  cd $MODELDIR/syntaxnet/syntaxnet/tensorflow
  ./configure
  cd ..
  bazel test syntexnet/... util/utf8/...
fi

cd $WORKDIR
