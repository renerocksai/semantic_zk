# 201802241943 Full list of options
tags = #commandline #usage #features

The full list of available options is displayed on the usage screen:

```bash
usage: zk2setevi    [-h] [-b FILE] [-e EXTENSION] [-l {single,double,§}]
                    [-p PARSER] [-u BASEURL] [--from FROM] [--to TO]
                    [--only-tags ONLY_TAGLIST] [--never-tags NEVER_TAGLIST]
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
  -u BASEURL, --url BASEURL
                        Remote URL the HTML should be built for (default: )
  --from FROM           (optionally abbreviated) timestamp from: include only
                        notes that are not younger than FROM (default:
                        19000101)
  --to TO               (optionally abbreviated) timestamp to: include only
                        notes that are not older than TO (default: 22001231)
  --only-tags ONLY_TAGLIST
                        only include notes tagged with tags from ONLY_TAGLIST
                        (default: )
  --never-tags NEVER_TAGLIST
                        never include notes tagged with tags from ONLY_TAGLIST
                        (default: )
```

### Example:

```bash
docs_zk docs --only-tags='#setevi #zettelkasten' --never-tags=#start \
             --from 20180224 --to=20180225 
```

* convert the `docs_zk` folder
* write output to the `docs` folder
* only consider notes tagged with either `#setevi` or `#zettelkasten`
* never consider notes tagged with `#start`
* only consider notes from 2018-02-24 to 2018-02-25 (incl.)

