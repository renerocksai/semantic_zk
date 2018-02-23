#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert a Zettelkasten into a Setevi HTML page """

import os
import sys
from libzk2setevi.zk2setevi import Zk2Setevi


def is_valid_file(parser, arg):
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The path %s does not exist!" % arg)
    else:
        return arg


def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("input_folder",
                        type=lambda x: is_valid_file(parser, x),
                        help="Input: your Zettelkasten folder",
                        )

    parser.add_argument("output_folder",
                        type=lambda x: is_valid_file(parser, x),
                        help="Output: Folder to write output HTML to",
                        )

    parser.add_argument("-b", "--bibfile",
                        dest="bibfile",
                        type=lambda x: is_valid_file(parser, x),
                        help=".bib file to use for citations if none is in your Zettelkasten folder",
                        metavar="FILE")

    parser.add_argument("-e", '--extension',
                        dest="extension",
                        default='.md',
                        type=str,
                        help="extension of your markdown files")

    parser.add_argument("-l", '--linkstyle',
                        dest="linkstyle",
                        default='double',
                        choices=['single', 'double', '§'],
                        type=str,
                        help="link style: double=[[link]], single=[link], §=§link")

    parser.add_argument("-p", '--parser',
                        dest="parser",
                        default='mmd',
                        type=str,
                        help="markdown parser: mmd=internal Multimarkdown, pandoc=pandoc, native=native")

    parser.add_argument("-w", '--max-img-width',
                        dest="max_img_width",
                        default=320,
                        type=int,
                        help="maximum width of images")
    return parser


if __name__ == "__main__":
    argparser = get_parser()
    if len(sys.argv) == 1:
        argparser.print_help()
        sys.exit()
    args = get_parser().parse_args()

    # try to find out our home
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    converter = Zk2Setevi(home=bundle_dir, folder=args.input_folder, out_folder=args.output_folder,
                          bibfile=args.bibfile, extension=args.extension,
                          linkstyle=args.linkstyle, parser=args.parser,
                          max_img_width=args.max_img_width)
    converter.create_html()

