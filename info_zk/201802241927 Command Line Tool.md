# 201802241927 Command Line Tool
tags = #commandline #usage #features

The command line tool is named `zk2setevi`.

Due to reasonable defaults, a typical invocation looks like this:

```bash
./zk2setevi /path/to/zettelkasten /path/to/output_directory
```

**Note:** The output directory must already exist.

If you want to use the `pandoc` parser, type

```bash
./zk2setevi /path/to/zettelkasten /path/to/output_directory -p pandoc
```

[[201802241943]] Full list of options

After conversion, just open the generated `out.html` from your *output_directory* in a browser.