import solution
from checker import Checker

def checkingScript(fun, args):
    return fun(args[0], args[1])


def main():
    checker = Checker()
    checker.addTest(checkingScript, [2, 2], 4, "2 + 2")
    checker.addTest(checkingScript, [81534425235, 43434241523463424], 81534425235+43434241523463424, "81534425235 + 43434241523463424")
    checker.addTest(checkingScript, ['ala ', 'ma kota'], 'ala ma kota', "dwa stringi")
    checker.addTest(checkingScript, [3.14, 2.71], 3.14 + 2.71, "3.14 + 2.71")
    checker.doTesting(solution.add)

if __name__ == '__main__':
    main()
