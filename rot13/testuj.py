import solution
from checker import Checker

def checkingScript(fun, args):
    return fun(args[0])


def main():
    checker = Checker()
    checker.addTest(checkingScript, 'abc', 'nop', "abc")
    checker.addTest(checkingScript, 'nop', 'abc', "nop")
    checker.addTest(checkingScript, 'xyz', 'klm', "xyz")
    checker.addTest(checkingScript, 'ala ma kota', 'nyn zn xbgn', "ala ma kota")
    checker.addTest(checkingScript, 'a, b, c!', 'n, o, p!', "a, b, c!")
    checker.doTesting(solution.rot13)

if __name__ == '__main__':
    main()
