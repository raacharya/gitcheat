from main import *


def main():
    def test(l):
        return getSum(l) == sum(l)

    d = {}
    d['test 1'] = [1, 2, 3, 4]
    d['test 2'] = [0, 0, 3, 4]
    d['test 3'] = [1, 2, 5, 34]
    d['test 4'] = [-1, -2]
    d['test 5'] = [0]
    d['test 6'] = []

    for k in d:
        print(k + " " + ("passed" if test(d[k]) else "failed"))

main()