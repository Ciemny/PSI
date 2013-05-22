import solution
from checker import Checker

def checkingScript(fun, args):
    return fun(args[0], args[1])


def main():
    checker = Checker()
    checker.addTest(checkingScript, [0, 0], [], "0 x 0")
    checker.addTest(checkingScript, [1, 1], [[1]], "1 x 1")
    checker.addTest(checkingScript, [2, 2], [[1, 2], [2, 4]], "2 x 2")
    checker.addTest(checkingScript, [2, 4], [[1, 2, 3, 4], [2, 4, 6, 8]], "2 x 4")
    checker.addTest(checkingScript, [4, 4], [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]], "4 x 4")
    checker.doTesting(solution.mul_table)

if __name__ == '__main__':
    main()
