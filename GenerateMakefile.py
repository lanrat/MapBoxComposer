#!/usr/bin/env python3

urlbase = "https://tiles.telegeography.com/maps/"
mapName = "submarine-cable-map-2024"
ext = "png"

out = "out/"+mapName

# max is non-inclusuve (uses python range())
# check urls in browser to get range
# url: z/x/y.png
x_min = 0
#x_min = 9 # 9 padding
x_max = 64
#x_max = 55

y_max = 64

z = 6

def generateDownloadMakefile():
	allList = []

	downloadCmd='curl --fail --silent --show-error --create-dirs -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"'

	for x in range(x_min, x_max):
		for y in range(y_max):
			folder=out+'/' + str(x).zfill(2)+'/'
			file=folder+str(y    ).zfill(2) + '.'+ext
			download = (urlbase + mapName +'/' + str(z) + '/' + str(x) + '/' + str(y    ) + '.' + ext)

			print(file + ':')
			print("\t" + downloadCmd + " -o $@ " + download)

			allList.append(file)

	ret = ' '.join(allList)
	print('download: ' + ret+"\n")


def generateStitchMakefile():
	vList = []

	for x in range(x_min, x_max):
		file=out+'/' + str(x).zfill(2) + '.png'
		deps=' '.join([out+'/'+str(x).zfill(2)+'/'+str(y).zfill(2)+'.png' for y in range(y_max)])
		print(file+': '+deps)
		print("\t convert $^ -append $@")
		vList.append(file)
	
	v = " ".join(vList)
	print('vertical: ' + v)

	hfile=out+"/"+mapName+".png"
	
	print('horizontal: '+hfile)
	print(hfile+': '+v)
	print("\tconvert $^ +append $@")

	print('stitch: vertical horizontal')


if __name__ == '__main__':
	print('.PHONY: all download stitch vertical horizontal')
	print('default: all')
	print('all: download stitch\n')
	generateDownloadMakefile()
	generateStitchMakefile()
