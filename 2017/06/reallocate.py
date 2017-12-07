import argparse

def reallocate(banks):
    cache = max(banks)
    index = banks.index(cache)
    banks[index] = 0
    length = len(banks)
    while cache > 0:
        index += 1
        index = index % length
        banks[index] += 1
        cache -= 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    path = args.path

    banks = []
    with open(path, 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            for block in line.split("\t"):
                banks.append(int(block))

    steps = 0
    seen = set()
    t = tuple(banks)
    while not t in seen:
        if steps >= 1000000:
            print("Too many steps!")
            break
        seen.add(t)
        reallocate(banks)
        t = tuple(banks)
        steps += 1
    print("Steps: " + str(steps))

if __name__ == "__main__":
    main()