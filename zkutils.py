import re


class ZkConstants:
    """
    Some constants used over and over
    """
    Link_Prefix = '['
    Link_Prefix_Len = len(Link_Prefix)
    Link_Postfix = ']'

    # characters at which a #tag is cut off (#tag, -> #tag)
    Tag_Stops = '.,\/!$%\^&\*;\{\}[]\'"=`~()<>\\'

    # search for tags in files
    RE_TAGS = r"(?<=\s|^)(?<!`)(#+([^#\s.,\/!$%\^&\*;{}\[\]'\"=`~()<>”\\]" \
                                                             r"|:[a-zA-Z0-9])+)"
    # Same RE just for ST python's re module
    ## un-require line-start, sublimetext python's RE doesn't like it
    RE_TAGS_PY = r"(?<=\s)(?<!`)(#+([^#\s.,\/!$%\^&\*;{}\[\]'\"=`~()<>”\\]" \
                                                             r"|:[a-zA-Z0-9])+)"

    # match note links in text
    ## adapted from ST3 plugin to include closing ]]
    Link_Matcher = re.compile('(\[+)([0-9.]{12,18})([^]]*\]+)|(§)([0-9.]{12,18})')

    # image links with attributes
    RE_IMG_LINKS = '(!\[)(.*)(\])(\()(.*)(\))(\{)(.*)(\})'

    # TOC markers
    TOC_HDR = '<!-- table of contents (auto) -->'
    TOC_END = '<!-- (end of auto-toc) -->'



