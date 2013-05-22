import solution
from checker import Checker

def checkingScript(fun, args):
    return fun(args)


def main():
    checker = Checker()
    checker.addTest(checkingScript, 0, [], "0")
    checker.addTest(checkingScript, 1, [0], "1")
    checker.addTest(checkingScript, 2, [0, 2], "2")
    checker.addTest(checkingScript, 5, [0, 2, 4, 6, 8], "5")
    checker.doTesting(solution.parzyste)

if __name__ == '__main__':
    main()
