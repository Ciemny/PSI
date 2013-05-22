class Checker:
    class Result:
        def __init__(self, title, color):
            self.title = title
            self.color = color

        endColor = '\033[0m'

        def __str__(self):
            return self.color + self.title + self.endColor

    OK = Result("OK", "\033[92m")
    ANS = Result("ANS", "\033[91m")
    RTE = Result("RTE", "\033[91m")

    class Test:
        def __init__(self, testingFun, arguments, out, description):
            self.testingFun = testingFun
            self.arguments = arguments
            self.out = out
            self.description = description

        def evaluate(self, toTest):
            try:
                if self.testingFun(toTest, self.arguments) == self.out:
                    return Checker.OK
                else:
                    return Checker.ANS
            except Exception:
                return Checker.RTE

    def __init__(self):
        self.testList = []

    def addTest(self, testingFun, arguments, out, description):
        self.testList.append(self.Test(testingFun, arguments, out, description))

    def doTesting(self, toTest):
        for i in range(len(self.testList)):
            print(str(i) + "\t" + str(self.testList[i].evaluate(toTest)) + "\t" + self.testList[i].description)
