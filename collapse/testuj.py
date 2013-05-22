import solution
from checker import Checker


def add(a):
    return a+"abc"


def reverse(s):
    return s[::-1]


def checkingScript(fun, args):
    return fun(args[0], args[1])(args[2])


def main():
    checker = Checker()
    checker.addTest(checkingScript, [add, add, ""], "abcabc", "+= 'abc', += 'abc'")
    checker.addTest(checkingScript, [add, reverse, "xyz"], "zyxabc", "+= 'abc', reverse(x)")
    checker.addTest(checkingScript, [reverse, add, "xyz"], "cbazyx", "reverse(x), += 'abc'")
    checker.addTest(checkingScript, [reverse, reverse, "xyz"], "xyz", "reverse(x), reverse(x)")
    checker.doTesting(solution.collapse)

if __name__ == '__main__':
    main()
