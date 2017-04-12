#!/usr/bin/env python
'''
$Id: fgrepwc.py,v 1.3 1999/09/08 02:23:51 wesc Exp wesc $

fgrepwc.py - searches for string in text file

    This module will output all lines of given file containing given string,
    including total number of matching lines.  This module can be imported,
    or executed standalone with the following usage syntax:

    Usage:  fgrepwc.py word filename

Exercises:

    3-10) add case-insensitive search

    3-11) change "line count" to "word count...," i.e., check if word
        appears more than once in line and truly count how many times
        a word shows up in a text file
'''

import sys        # system module
import string        # string utility module

#
# usage() -- prints usage and exits
#
def usage():
    print "usage:  fgrepwc [ -i ] string file"
    sys.exit(1)


#
# filefind() -- searches for 'word' within file 'filename'
#
def filefind(word, filename):

    # reset word count
    count = 0

    # see if we can open the file
    try:
        file_handle = open(filename, 'r')
    except:
        print filename, ":", sys.exc_value[1]
        sys.exit(1)

    # read in all lines and close file
    lines = file_handle.readlines()
    file_handle.close()

    # for each line, check for the word
    for i in lines:
        if string.find(i, word) > -1:
            count = count + 1
            print i,

    # output line count
    print count


#
# main() -- used only when module is executed
#
def main():

    # check command-line arguments
    argc = len(sys.argv)
    if argc != 3:
        usage()

    # call fgrepwc.filefind() with cmd-line arguments
    filefind(sys.argv[1], sys.argv[2])


# executes only if not imported
if __name__ == '__main__': 
    main()
