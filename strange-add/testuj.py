import solution
from checker import Checker

def checkStr(fun, args):
    return str(solution.strange_number(args))

def checkAdd(fun, args):
    A = solution.strange_number(args[0])
    B = solution.strange_number(args[1])
    return str(A+B)

def checkPositive(fun, args):
    A = solution.strange_number(args)
    return A[1]

def checkNegative(fun, args):
    A = solution.strange_number(args)
    return A[-1]


def main():
    checker = Checker()
    checker.addTest(checkStr, 253, "253", "str(strange_number(253))")
    checker.addTest(checkAdd, [12, 28], "1228", "str(A+B)")
    checker.addTest(checkPositive, 5, 5, "A[1]")
    checker.addTest(checkNegative, 10, -10 , "A[-1")
    checker.doTesting(solution.strange_number)

if __name__ == '__main__':
    main()
