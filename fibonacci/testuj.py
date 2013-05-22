import solution
from checker import Checker


def checkingScript(fun, N):
    ret = []
    for i in fun(N):
        ret.append(i)


def main():
    checker = Checker()
    checker.addTest(checkingScript, 1, [0], "1")
    checker.addTest(checkingScript, 3, [0, 1, 1], "3")
    checker.addTest(checkingScript, 8, [0, 1, 1, 2, 3, 5, 8, 13], "8")
    checker.doTesting(solution.fib)

if __name__ == '__main__':
    main()
