import argparse
import math

def calcPath(position):
    if position == 0:
        return 0
    if position == 1:
        return 0

    print("Position: " + str(position))
    size = math.ceil(math.sqrt(position))
    if size % 2 == 0:
        size += 1
    print("\tSize: " + str(size))
    radius = (size - 1) / 2
    print("\tRadius: " + str(radius))
    max = size*size
    print("\tMax: " + str(max))
    extDist = max - position
    sidePos = int(abs((extDist % (size-1)) - radius))
    print("\tPos: " + str(sidePos))
    return int(radius + sidePos)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("position")
    args = parser.parse_args()
    position = int(args.position)
    #for test in range(26):
    #    print(str(calcPath(test)))
    print(calcPath(position))

if __name__ == "__main__":
    main()