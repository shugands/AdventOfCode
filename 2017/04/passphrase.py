import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    path = args.path

    sum = 0
    with open(path, 'r') as f:
        for line in f:
            if checkPassphrase(line):
                sum += 1
    print("Valid: " + str(sum))

if __name__ == "__main__":
    main()