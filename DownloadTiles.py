#!/usr/bin/env python
import os
import time

mapname = "submarine-cable-map-2013"
ext = "png"

def generateMakefile():
	z = 6
	allList = []
	for x in range(64):
		os.system('mkdir -p ' + str(x))
		for y in range(60 / 4):
			y = y * 4;
			download1 = ('http://a.tiles.telegeography.com/maps/'+ mapname +'/' + str(z) + '/' + str(x) + '/' + str(y    ) + '.' + ext + ' > ' + str(x) + '/' + str(y    ) + '.png') 
			download2 = ('http://b.tiles.telegeography.com/maps/'+ mapname +'/' + str(z) + '/' + str(x) + '/' + str(y + 1) + '.' + ext + ' > ' + str(x) + '/' + str(y + 1) + '.png')
			download3 = ('http://c.tiles.telegeography.com/maps/'+ mapname +'/' + str(z) + '/' + str(x) + '/' + str(y + 2) + '.' + ext + ' > ' + str(x) + '/' + str(y + 2) + '.png')
			download4 = ('http://d.tiles.telegeography.com/maps/'+ mapname +'/' + str(z) + '/' + str(x) + '/' + str(y + 3) + '.' + ext + ' > ' + str(x) + '/' + str(y + 3) + '.png')
 
			downloadCmd = 'wget --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" -O - '

			print str(x) + '_' + str(y) + ':'
			print "\t" + downloadCmd + download1
			print str(x) + '_' + str(y + 1) + ':'
			print "\t" + downloadCmd + download2
			print str(x) + '_' + str(y + 2) + ':'
			print "\t" + downloadCmd + download3
			print str(x) + '_' + str(y + 3) + ':'
			print "\t" + downloadCmd + download4

			allList.append(str(x) + '_' + str(y))
			allList.append(str(x) + '_' + str(y+1))
			allList.append(str(x) + '_' + str(y+2))
			allList.append(str(x) + '_' + str(y+3))


			y = y / 4
	ret = ''
	for i in allList:
		ret += i + " "

	print 'all: \t ' + ret

if __name__ == '__main__':
	generateMakefile()
