
def execute(curr, inst):
    val = inst[curr]
    new = curr + val
    inst[curr] += 1
    return new

def main():
    path = "2017/05/day5.txt"

    inst = []
    with open(path, 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            inst.append(int(line))
    
    length = len(inst)
    curr = 0
    steps = 0
    while curr < length:
        if steps >= 1000000:
            print("Too many steps!")
            break
        curr = execute(curr, inst)
        steps += 1
    print("Steps: " + str(steps))

if __name__ == "__main__":
    main()