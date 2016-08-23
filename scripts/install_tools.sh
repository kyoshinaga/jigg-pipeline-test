#!/bin/sh

WORKDIR=`dirname $0`/..
JIGGDIR=$WORKDIR/jigg
MODELDIR=$WORKDIR/models

# jigg@tomeken-yoshinaga
if [ -d $JIGGDIR ];
then
  echo "jigg exist."
else
  git clone -b develop https://github.com/tomeken-yoshinaga/jigg.git
  cd $JIGGDIR
  ./bin/sbt assembly
  mv ./target/*.jar bin
  ./script/download_models.sh
  mv ./*.jar bin
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
#BAZEL="https://github.com/bazelbuild/bazel/releases/download/0.2.2b/bazel_0.2.2b-jdk7-linux-x86_64.deb"
#if type "bazel" > /dev/null;
#then
#  echo "bazel exists."
#else
#  wget -P $MODELDIR $BAZEL
#  cd $MODELDIR
#  sudo dpkg -i bazel_0.2.2b-jdk7-linux-x86_64.deb
#  sudo apt-get -y -q install swig
#fi
#
#SYNTAXNET="https://github.com/tensorflow/models.git"
#if [ -d $MODELDIR/syntaxnet ];
#then
#  echo "syntaxnet exists."
#else
#  git clone --recursive $SYNTAXNET $MODELDIR/syntaxnet
#  cd $MODELDIR/syntaxnet/syntaxnet/tensorflow
#  ./configure
#  cd ..
#  bazel test syntaxnet/... util/utf8/...
#fi

cd $WORKDIR
