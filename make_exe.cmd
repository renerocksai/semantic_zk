set PATH=%PATH%;C:\Users\rene.schallner\AppData\Local\Continuum\anaconda3\bin
set PATH=%PATH%;C:\Users\rene.schallner\AppData\Local\Continuum\anaconda3\Scripts

rd dist /S /Q
rd build /S /Q
pyinstaller  --add-binary /Users/rene.schallner/AppData/Local/Continuum/anaconda3/Lib/site-packages/pymmd/files/libMultiMarkdown.dll;. --add-data data/setevi-template.html;data -F zk2setevi.py
pyinstaller  --windowed --add-binary /Users/rene.schallner/AppData/Local/Continuum/anaconda3/Lib/site-packages/pymmd/files/libMultiMarkdown.dll;. --add-data data/setevi-template.html;data -F semantic_zk.py

python bundle_version.py --rename-dist