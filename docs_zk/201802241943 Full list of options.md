# 201802241943 Full list of options
tags = #commandline #usage #features

The full list of available options is displayed on the usage screen:

```bash
usage: zk2setevi [-h] [-b FILE] [-e EXTENSION] [-l {single,double,§}]
                 [-p PARSER] [-w MAX_IMG_WIDTH]
                 input_folder output_folder

Convert a Zettelkasten into a Setevi HTML page

positional arguments:
  input_folder          Input: your Zettelkasten folder
  output_folder         Output: Folder to write output HTML to

optional arguments:
  -h, --help            show this help message and exit
  -b FILE, --bibfile FILE
                        .bib file to use for citations if none is in your
                        Zettelkasten folder (default: None)
  -e EXTENSION, --extension EXTENSION
                        extension of your markdown files (default: .md)
  -l {single,double,§}, --linkstyle {single,double,§}
                        link style: double=[[link]], single=[link], §=§link
                        (default: double)
  -p PARSER, --parser PARSER
                        markdown parser: mmd=internal Multimarkdown,
                        pandoc=pandoc, native=native (default: mmd)
```
