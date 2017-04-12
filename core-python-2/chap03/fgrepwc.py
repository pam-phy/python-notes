#!/usr/bin/env python

"fgrepwc.py -- searches for string in text file"

import sys
import string

# print usage and exit
def usage():
    print "usage:  fgrepwc [ -i ] string file"
    sys.exit(1)

# does all the work
def filefind(word, filename):

    # reset word count
    count = 0

    # can we open file? if so, return file handle
    try:
        fh = open(filename, 'r')

    # if not, exit
    except:
        print filename, ":", sys.exc_value[1]
        sys.exit(1)

    # read all file lines into list and close
    allLines = fh.readlines()
    fh.close()

    # iterate over al lines of file
    for eachLine in allLines:

	# search each line for the word
        if string.find(eachLine, word) > -1:
            count = count + 1
            print eachLine,

    # when complete, display line count
    print count

# validate arguments and call filefind()
def checkargs():

    # check args; 'argv' comes from 'sys' module
    argc = len(sys.argv)
    if argc != 3:
        usage()

    # call fgrepwc.fileind() with args
    filefind(sys.argv[1], sys.argv[2])

# execute as application
if __name__ == '__main__': 
    checkargs()
