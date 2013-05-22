import solution
from checker import Checker


def checkingScript(fun, args):
    return fun(args[0])


def main():
    checker = Checker()
    checker.addTest(checkingScript, [8], 17, "int")
    checker.addTest(checkingScript, [3.14], 3.14/2, "float")
    checker.addTest(checkingScript, ["ala ma kota"], "pomidor", "string")
    checker.addTest(checkingScript, [['a', 'b', 'c']], 3, "lista")
    checker.doTesting(solution.choice)

if __name__ == '__main__':
    main()
