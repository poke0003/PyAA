from cTerritory import Territory as T

def createMap():
    Map = {}

    with open('MapConfig.txt') as myFile:
        lines = myFile.readlines()
        for line in lines:
            args = line.split('|')
            tempTerr = T(args[0], args[1], bool(int(args[2])), int(args[3]), args[4])
            Map[tempTerr.name] = tempTerr
    return Map

if __name__ == '__main__':
    for key, item in createMap().items():
        print(f'{key}: {item}')
