import sys

def checksum(data):
    size = len(data)
    sum = 0
    for row in data:
        min = sys.maxsize
        max = -1*min
        for v in row:
            if v < min:
                min = v
            if v > max:
                max = v
        sum += (max-min)
    return sum

def main():
    path = "2017/02/day2.txt"
    data = []
    with open(path, 'r') as f:
        for line in f:
            row = list(map(int, line.split("\t")))
            data.append(row)
    print("Checksum: " + str(checksum(data)))

if __name__ == "__main__":
    main()