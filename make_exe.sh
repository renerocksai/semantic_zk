#!/usr/bin/env bash

VERSION=$(python bundle_version.py --version)
PREFIX=$(python bundle_version.py --prefix)

python bundle_version.py --init
DEPLOY_BASE=$(python bundle_version.py --deploy-dir)

# cx_Freeze approach

# command line tool
rm -fr build/
python build_macos_zk2setevi.py build 2>&1  |tee build-zk2setevi-${PREFIX}-${VERSION}.log

ORIG_DIR=$(echo build/exe.macos*)
DEPLOY_DIR=${DEPLOY_BASE}/semantic_zk-${PREFIX}-${VERSION}-macOS
DEST=${DEPLOY_DIR}/commandline

mkdir -p ${DEPLOY_DIR}
mv ${ORIG_DIR} ${DEPLOY_DIR}
mv ${DEPLOY_DIR}/$(basename ${ORIG_DIR}) ${DEST}

# GUI
rm -fr build/
python build_macos_semantic_zk.py bdist_mac 2>&1  |tee build-semantic_zk-${PREFIX}-${VERSION}.log
cp -v Info.plist build/semantic_zk-${VERSION}.app/Contents/
mv -v build/semantic_zk-${VERSION}.app ${DEPLOY_DIR}/
rm -fr build/

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
