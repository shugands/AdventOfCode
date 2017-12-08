import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    path = args.path

    data = {}
    first = ""
    with open(path, 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            pieces = list(filter(None, re.split(",| ", line)))
            name = pieces[0]
            if first == "":
                first = name
            parents = []
            if len(pieces) > 2:
                parents = pieces[3:]
            for p in parents:
                data[p] = name
    current = first
    steps = 0
    while current in data and steps < 1000000:
        steps += 1
        current = data[current]

    print("Bottom: " + current)

if __name__ == "__main__":
    main()