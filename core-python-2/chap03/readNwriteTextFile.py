#!/usr/bin/env python

'readNwriteTextFile.py -- creat or display text file'

import os

check = raw_input('Do you want to creat a text file (y or n): ')

if check == 'y':
	# get file name
	while True:
		fname = raw_input('Enter file name: ')
		if os.path.exists(fname):
			print "ERROR: '%s' already exists" % fname
		else:
			break

	# get file content (text) lines
	all = []
	print "\nEnter lines ('.' by itself to quit).\n"

	# loop until user terminates input
	while True:
		entry = raw_input('> ')
		if entry == '.':
			break
		else:
			all.append(entry)

	# write lines to file with proper line-ending
	fobj = open(fname, 'w')
	fobj.write('\n'.join(all))
	fobj.close()
	print 'Done!'

check = raw_input('Do you want to display a text file (y or n): ')

if check == 'y':
	# get file name
	fname = raw_input('Enter file name: ')
	print

	# attempt to open file for reading
	try:
		fobj = open(fname, 'r')
	except IOError, e:
		print "*** file open error:", e
	else:
		# display countents to the screen
		for eachLine in fobj:
			print eachLine,
		fobj.close()
