from main import *
from math import factorial

def main():
    def test(n):
        return getFactorial(n) == factorial(n)

    d = {}
    d['test 1'] = 0
    d['test 2'] = 1
    d['test 3'] = 2
    d['test 4'] = 3
    d['test 5'] = 4
    d['test 6'] = 9

    for k in d:
        print(k + " " + ("passed" if test(d[k]) else "failed"))

main()