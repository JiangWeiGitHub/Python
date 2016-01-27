#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "##########################"
print "utf-8 test:"
print "print \'\\xe4\\xb8\\xad\\xe6\\x96\\x87\\'.decode(\'utf-8\')"
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print "##########################"
print "print test:"
print "print \"Your Score is: %03d, %s!\" % (99,\'Tom\')"
print "Your Score is: %03d, %s!" % (99,'Tom')

print "##########################"
print "list test:"
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

print "##########################"
print "range test:"
sum = 0
for x in range(101):
    sum = sum + x
print sum

print "##########################"
print "dict test:"
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Bob']

print "##########################"
print "function test:"
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print "origin: -10"
result = my_abs(-10)
print "now: %d\n"%result

print "recursion test:"
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print "parameter: 5"
print "result: %d"%fact(5)

print "##########################"
print "slice test:"
print "origin: 'Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'"
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print "print 1~3"
print L[0:3]

print "##########################"
print "iteration test:"
print "origin: (1, 1), (2, 4), (3, 9)"
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x,y

print "##########################"
print "List Comprehensions test:"
print "goal: [1x1, 2x2, 3x3, ..., 10x10]"
print "method: [x * x for x in range(1, 11)]"
test = [x * x for x in range(1, 11)]
print test

print "##########################"
print "Generator test:"
print "method: (x * x for x in range(1, 11))"
test = (x * x for x in range(1, 11))
for n in test:
    print n

print "Yield test:"
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
test = fib(10)
print "print method 1:"
for n in range(10):
    print test.next()

print "print method 2:"
for n in fib(10):
    print n

print "##########################"
print "Higher-order function test:"
def add(x, y, f):
    return f(x) + f(y)
aaa = 10
bbb = 20
def ccc(tmp):
    return tmp*tmp
ddd = add(aaa,bbb,ccc)
print "function: def add(x, y, f):"
print "    return f(x) + f(y)"
print "parameters: aaa,bbb,ccc"
print "aaa = 10, bbb = 20, ccc = "
print "def ccc(tmp):"
print "    return tmp*tmp"
print "result: "
print ddd

print "##########################"
print "map test:"
print "function:"
print "def f(x):"
print "    return x * x"
print "map method:"
print "map(f,[1,2,3,4,5,6,7,8,9])"
print "result:"
def f(x):
    return x * x
result = map(f,[1,2,3,4,5,6,7,8,9])
print result

print "##########################"
print "reduce test:"
print "function:"
print "def add(x, y):"
print "    return x + y"
print "reduce method:"
print "reduce(add, [1, 3, 5, 7, 9])"
print "result:"
def add(x, y):
    return x + y
result = reduce(add, [1, 3, 5, 7, 9])
print result

print "##########################"
print "map & reduce test:"
print "def str2int(s):"
print "    def fn(x, y):"
print "        return x * 10 + y"
print "    def char2num(s):"
print "        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]"
print "    return reduce(fn, map(char2num, s))"
print "method: str2int('5211314')"
print "result:"
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
result = str2int('5211314')
print result

print "##########################"
print "filter test:"
print "def is_odd(n):"
print "    return n % 2 == 1"
def is_odd(n):
    return n % 2 == 1
print "filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])"
result = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print "result:"
print result

print "##########################"
print "sorted test:"
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
result = sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
print result









