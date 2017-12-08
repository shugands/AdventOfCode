import sys

def process(registers, reg, oper, amt, condReg, condCheck, condVal):
    condRegVal = registers[condReg]
    checkResult = False
    if condCheck == "==":
        checkResult = condRegVal == condVal
    elif condCheck == "!=":
        checkResult = condRegVal != condVal
    elif condCheck == ">":
        checkResult = condRegVal > condVal
    elif condCheck == "<":
        checkResult = condRegVal < condVal
    elif condCheck == ">=":
        checkResult = condRegVal >= condVal
    elif condCheck == "<=":
        checkResult = condRegVal <= condVal
    else:
        print("Unexpected check: " + condCheck)
    
    if checkResult:
        if oper == "inc":
            registers[reg] += amt
        elif oper == "dec":
            registers[reg] -= amt
        else:
            print("Unexpected operation: " + oper)

def main():
    path = "2017/08/day8.txt"

    registers = {}
    absMax = -1*sys.maxsize
    with open(path, 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            args = line.split(" ")
            reg = args[0]
            oper = args[1]
            amt = int(args[2])
            condReg = args[4]
            condCheck = args[5]
            condVal = int(args[6])
            if not reg in registers:
                registers[reg] = 0
            if not condReg in registers:
                registers[condReg] = 0
            process(registers, reg, oper, amt, condReg, condCheck, condVal)
            thisMax = max(registers.values())
            if thisMax > absMax:
                absMax = thisMax

    maxVal = max(registers.values())
    #maxVal = -1*sys.maxsize
    #for reg, val in registers.items():
    #    if val > maxVal:
    #        maxVal = val
    print("Final Max Register Value: " + str(maxVal))
    print("Abs Max Register Value: " + str(absMax))

if __name__ == "__main__":
    main()