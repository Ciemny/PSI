import solution
from checker import Checker

def checkingScript(klasa, args):

    @solution.FunctionCounter.decore
    def fun1():
        return 1

    @solution.FunctionCounter.decore
    def fun2(x, y):
        return x + y

    @solution.FunctionCounter.decore
    def fun3(x):
        return x

    def fun4():
        return 1


    if fun1() != 1:
        raise RuntimeError

    if fun2(3, 4) != 7:
        raise RuntimeError
    if fun2(1, 1) != 2:
        raise RuntimeError

    if fun3(1) != 1:
        raise RuntimeError
    if fun3(2) != 2:
        raise RuntimeError
    if fun3(3) != 3:
        raise RuntimeError
    if fun3(4) != 4:
        raise RuntimeError


    return [solution.FunctionCounter.count("fun1"), solution.FunctionCounter.count("fun2"), solution.FunctionCounter.count("fun3"), solution.FunctionCounter.count("fun4")]

def main():
    checker = Checker()
    checker.addTest(checkingScript, [2, 2], [1, 2, 4, 0], "4 funkcje, szczegóły w testuj.py")
    checker.doTesting(solution.FunctionCounter)

if __name__ == '__main__':
    main()
