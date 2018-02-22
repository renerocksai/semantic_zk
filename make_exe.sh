#!/usr/bin/env bash

pyinstaller --add-binary=/Users/rs/anaconda3/lib/python3.6/site-packages/pymmd/files/libMultiMarkdown.dylib:. \
            --add-data=data/setevi-template.html:data -F zk2setevi.py
