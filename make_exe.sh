#!/usr/bin/env bash

# cx_Freeze approach
python setup.py bdist_mac 2>&1  |tee build.log


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
