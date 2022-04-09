#!/usr/bin/env python

def generateMakefile():
	z = 6
	vList = []
	print('default: horizontal\n\n')

	for x in range(64):
		print('v_'+str(x).zfill(2)+':')
		print("\t convert out/" + str(x).zfill(2) + '/*.png -append out/' + str(x).zfill(2) + '.png')
		vList.append('v_'+str(x).zfill(2))

	v = ''
	for i in vList:
		v += i + " "

	print('vertical: ' + v)

	print('horizontal: vertical')
	print("\tconvert out/*.png +append out/composite.png")

if __name__ == '__main__':
	generateMakefile()
