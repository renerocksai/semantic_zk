# 201802241928 Graphical Tool
tags = #graphical #usage #gui

The Graphical tool `semantic_zk` is pretty self-explanatory:

![](img/gui_filters_annotated.png)

The typical workflow is:

* 1: Select Zettelkasten folder
* 2: Select Output folder
* 12: Convert

When the conversion is finished, the generated HTML will be rendered on the right half of the window.

Once you close the program, you can always just open the HTML in a browser from your chosen output folder, to see it again.

The optional steps are:

* 3: Select a `.bib` file if there is none in your Zettelkasten folder or if you want to override it.
* 4: Enter the filename extension of your markdown files if it differs from `.md`, for example `.mdown` or `.txt`.
* 5: Select the link style format that should be used in the HTML output. 
    * Default is `[double` for `[[double bracket links]]` 
    * `single` stands for `[single bracket links]`
    * `§` selects `§201802240300` old school links 
* 6: select a markdown parser. See [above](#about-the-available-parsers) for a comparison:
    * Default is `mmd`, the Multimarkdown parser
    * `pandoc` stands for the Pandoc parser
    * `native` selects the native parser
* 7 : Specify the remote URL if the export is meant to be uploaded to a webserver. This fixes the image links. Leave blank for local use.
* 8 : Specify the (optionally abbreviated) **from** timestamp: include only notes that are not younger than the given timestamp
* 9 : Specify the (optionally abbreviated) **to** timestamp: include only notes that are not older than the given timestamp
* 10: Enter a list of tags in `#tag1 #tag2` format to **only** include notes that are tagged by either of the given tags.
* 11: Enter a list of tags in `#tag1 #tag2` format to **never** include notes that are tagged by either of the given tags.
