#!/usr/bin/env bash

VERSION=$(python bundle_version.py --version)
PREFIX=$(python bundle_version.py --prefix)

DEBUG=

$DEBUG rm -fr build/

# cx_Freeze approach
$DEBUG python build_macos_zk2setevi.py build 2>&1  |tee build-zk2setevi-${PREFIX}-${VERSION}.log
$DEBUG python build_macos_semantic_zk.py bdist_mac 2>&1  |tee build-semantic_zk-${PREFIX}-${VERSION}.log
$DEBUG cp -v Info.plist build/semantic_zk-${VERSION}.app/Contents/

# command line tool
ORIG_DIR=$(echo build/exe.macos*)
DEPLOY_DIR=build/semantic_zk-${PREFIX}-${VERSION}-macOS
DEST=${DEPLOY_DIR}/commandline

mkdir -p ${DEPLOY_DIR}
mv ${ORIG_DIR} ${DEPLOY_DIR}
mv ${DEPLOY_DIR}/$(basename ${ORIG_DIR}) ${DEST}

# GUI
mv -v build/build/semantic_zk-${VERSION}.app ${DEPLOY_DIR}/


# pyinstaller doesn't work with PyQt5 on macOS

##pyinstaller $1 --add-binary=/Users/rs/anaconda3/lib/python3.6/site-packages/pymmd/files/libMultiMarkdown.dylib:. \
##            --add-data=data/setevi-template.html:data -F zk2setevi.py
#
#echo
#echo " ----------------------- "
#echo
#
#rm -fr tmp
#mkdir tmp
#
#
## --windowed
#pyinstaller $1  --runtime-tmpdir ./tmp --add-binary=/Users/rs/anaconda3/lib/python3.6/site-packages/pymmd/files/libMultiMarkdown.dylib:. \
#            --add-data=data/setevi-template.html:data  -F semantic_zk.py
## rm -fr tmp
