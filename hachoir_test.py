__author__ = 'Boot'


import hachoir_parser
from hachoir_core.cmd_line import unicodeFilename
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset
from hachoir_core.field import GenericFieldSet






def print_metadata(metadata):
    text = metadata.exportPlaintext()
    charset = getTerminalCharset()
    for line in text:
     pass #   print makePrintable(line, charset)

    # from http://stackoverflow.com/questions/14546533/hachoir-retrieving-data-from-a-group
    # See what keys you can extract
    for k,v in metadata._Metadata__data.iteritems():
        if v.values:
            print v.key, v.values[0].value

#print type(p)
def print_recursively(fields):
    f = fields.iteritems()
    for k,v in f:
        print "%s=%s" % (k, v)
        if isinstance(v, GenericFieldSet):
            print_recursively(v._fields)


def main(filename = "default_64.png"):
    filename, realname = unicodeFilename(filename), filename

    p = hachoir_parser.createParser(filename, realname)
    metadata = extractMetadata(p)
    print_metadata(metadata)

    fields = p._fields
    print_recursively(fields)


if __name__ == "__main__":
    main()