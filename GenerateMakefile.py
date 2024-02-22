#!/usr/bin/env python3
import os

urlbase = "https://tiles.telegeography.com/maps/"
mapName = "africa-map-2024"
ext = "png"

out = "out/"+mapName

def generateDownloadMakefile():
	z = 6
	allList = []

	for x in range(64):
		os.system('mkdir -p ' + out + '/'+str(x).zfill(2))
		for y in range(int(60 / 4)):
			y = y * 4;
			download1 = (urlbase + mapName +'/' + str(z) + '/' + str(x) + '/' + str(y    ) + '.' + ext + ' > '+out+'/' + str(x).zfill(2) + '/' + str(y    ).zfill(2) + '.png')
			download2 = (urlbase + mapName +'/' + str(z) + '/' + str(x) + '/' + str(y + 1) + '.' + ext + ' > '+out+'/'+ str(x).zfill(2) + '/' + str(y + 1).zfill(2) + '.png')
			download3 = (urlbase + mapName +'/' + str(z) + '/' + str(x) + '/' + str(y + 2) + '.' + ext + ' > '+out+'/' + str(x).zfill(2) + '/' + str(y + 2).zfill(2) + '.png')
			download4 = (urlbase + mapName +'/' + str(z) + '/' + str(x) + '/' + str(y + 3) + '.' + ext + ' > '+out+'/' + str(x).zfill(2) + '/' + str(y + 3).zfill(2) + '.png')

			downloadCmd = 'wget --no-verbose --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" -O - '

			print(str(x) + '_' + str(y) + ':')
			print("\t" + downloadCmd + download1)
			print(str(x) + '_' + str(y + 1) + ':')
			print("\t" + downloadCmd + download2)
			print(str(x) + '_' + str(y + 2) + ':')
			print("\t" + downloadCmd + download3)
			print(str(x) + '_' + str(y + 3) + ':')
			print("\t" + downloadCmd + download4)

			allList.append(str(x) + '_' + str(y))
			allList.append(str(x) + '_' + str(y+1))
			allList.append(str(x) + '_' + str(y+2))
			allList.append(str(x) + '_' + str(y+3))


			y = y / 4
	ret = ''
	for i in allList:
		ret += i + " "

	print('download: \t ' + ret)

def generateStitchMakefile():
	z = 6
	vList = []
	print('stitch: horizontal\n')

	for x in range(64):
		print('v_'+str(x).zfill(2)+':')
		print("\t convert "+out +'/'+ str(x).zfill(2) + '/*.png -append '+out+'/' + str(x).zfill(2) + '.png')
		vList.append('v_'+str(x).zfill(2))

	v = ''
	for i in vList:
		v += i + " "

	print('vertical: ' + v)

	print('horizontal: vertical')
	print("\tconvert "+out+"/*.png +append "+out+"/"+mapName+".png\n")


if __name__ == '__main__':
	print('default: all\n\n')
	print('all: download stitch')
	generateDownloadMakefile()
	generateStitchMakefile()
