import os
from collections import defaultdict as dd
os.chdir(r'C:\Users\Gabriel\Desktop')
lines = open('.\Advent.txt').read().splitlines()
dMap = dd(tuple)
count = 0

def returnpos(line):
    posx, posy = map(int, line.split('position=<')[1].strip(' ').rsplit('> ')[0].split(', '))
    velx, vely = map(int, line.split('velocity=<')[1].strip(' ').strip('>').split(', '))
    return [[posx,posy], [velx,vely]]


def getMax(array, xmax = -1e10, ymax = -1e10, xmin = 1e10, ymin = 1e10):
    for pos, vel in array:
        xmax = max(xmax, pos[0])
        xmin = min(xmin,pos[0])
        ymax = max(ymax,pos[1])
        ymin = min(ymin,pos[1])
    return xmax, xmin, ymax, ymin


def filldots(dMap):
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            dMap[x,y] = '.'


def printMap(dMap):
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax + 1):
            print(dMap.setdefault((x,y),'.'), end = '')
        print('')


test = [returnpos(line) for line in lines]
xmax, xmin, ymax, ymin = getMax(test)
#filldots(dMap)


def placeCoords():
    for i in test:
        coordtoplace = tuple([i[0][0], i[0][1]])
        dMap.setdefault(coordtoplace,'#')


placeCoords()
#printMap(dMap)


def MoveCoordinates():
    global count
    for i in test:
        i[0] = [i[0][0] + i[1][0], i[0][1] + i[1][1]]
    count += 1


def runRoutine():
    global dMap#, xmax, xmin, ymax, ymin
    MoveCoordinates()
    #xmax = xmin = ymax = ymin = 0
    xmax, xmin, ymax, ymin = getMax(test)
    del dMap
    dMap = dd(tuple)
    placeCoords()
    return xmax, xmin, ymax, ymin

def runRoutine2():
    global dMap#, xmax, xmin, ymax, ymin
    MoveCoordinates()
    #xmax = xmin = ymax = ymin = 0
    xmax, xmin, ymax, ymin = getMax(test)
    del dMap
    dMap = dd(tuple)
    placeCoords()
    printMap(dMap)
    return xmax, xmin, ymax, ymin

while (ymax-ymin) > 19 and (xmax-xmin)>60:
    xmax, xmin, ymax, ymin = runRoutine()
    #print('y difference is', ymax-ymin, 'and x difference is',xmax-xmin)

def printMap(dMap):
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax + 1):
            print(dMap.setdefault((x,y),'.'), end = '')
        print('')

runRoutine2()
print('Ran for ', count,'seconds')
