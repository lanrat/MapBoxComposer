#!/usr/bin/env python
import os
import FixFilenames

def stichVertical():

    for x in range(64):
        print "Folder: " + str(x)
        os.system('convert ' + str(x) + '/*.png -append ' + str(x) + '.png')

def stichHorizontal():
    print "Root folder"
    FixFilenames.fixTopLevel()
    os.system('convert *.png +append composite.png')

if __name__ == '__main__':
    stichVertical()
    stichHorizontal()
