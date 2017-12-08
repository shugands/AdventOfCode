
def checkPassphrase(phrase):
    phrase = phrase.replace("\n", "")
    words = phrase.split(" ")
    seen = set()
    for w in words:
        if w in seen:
            return False
        seen.add(w)
    return True

def main():
    path = "2017/04/day4.txt"

    sum = 0
    with open(path, 'r') as f:
        for line in f:
            if checkPassphrase(line):
                sum += 1
    print("Valid: " + str(sum))

if __name__ == "__main__":
    main()