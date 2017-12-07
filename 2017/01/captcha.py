import argparse
import requests

def calcSum(captcha):
    sum = 0;
    first = int(captcha[0])
    last = '';
    lastmatched = False
    for c in captcha:
        i = int(c)
        lastmatched = False
        if (i == last):
            sum += i
            lastmatched = True
        last = i
    if first == last and not lastmatched:
        sum += first
    return sum

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("captcha")
    args = parser.parse_args()

    captcha = args.captcha
    print("Input: " + captcha)
    print("Output: " + str(calcSum(captcha)))

if __name__ == "__main__":
    main()
