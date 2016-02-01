#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ""
print "##########################"
print "utf-8 test:"
print "print \'\\xe4\\xb8\\xad\\xe6\\x96\\x87\\'.decode(\'utf-8\')"
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print ""
print "##########################"
print "print test:"
print "print \"Your Score is: %03d, %s!\" % (99,\'Tom\')"
print "Your Score is: %03d, %s!" % (99,'Tom')

print ""
print "##########################"
print "list test:"
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

print ""
print "##########################"
print "range test:"
sum = 0
for x in range(101):
    sum = sum + x
print sum

print ""
print "##########################"
print "dict test:"
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Bob']

print ""
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

print ""
print "recursion test:"
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print "parameter: 5"
print "result: %d"%fact(5)

print ""
print "##########################"
print "slice test:"
print "origin: 'Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'"
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print "print 1~3"
print L[0:3]

print ""
print "##########################"
print "iteration test:"
print "origin: (1, 1), (2, 4), (3, 9)"
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x,y

print ""
print "##########################"
print "List Comprehensions test:"
print "goal: [1x1, 2x2, 3x3, ..., 10x10]"
print "method: [x * x for x in range(1, 11)]"
test = [x * x for x in range(1, 11)]
print test

print ""
print "##########################"
print "Generator test:"
print "method: (x * x for x in range(1, 11))"
test = (x * x for x in range(1, 11))
for n in test:
    print n

print ""
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

print ""
print "print method 2:"
for n in fib(10):
    print n

print ""
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

print ""
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

print ""
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

print ""
print "##########################"
print "map & reduce test:"
print "def str2int(s):"
print "    def fn(x, y):"
print "        return x * 10 + y"
print "    def char2num(s):"
print "        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]"
print "    return reduce(fn, map(char2num, s))"
print "str2int('5211314')"
print "result:"
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
result = str2int('5211314')
print result

print ""
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

print ""
print "##########################"
print "sorted test:"
print "def cmp_ignore_case(s1, s2):"
print "    u1 = s1.upper()"
print "    u2 = s2.upper()"
print "    if u1 < u2:"
print "        return -1"
print "    if u1 > u2:"
print "        return 1"
print "    return 0"
print "sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)"
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
result = sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
print "result:"
print result

print ""
print "##########################"
print "return function test:"
print "def lazy_sum(*args):"
print "    def sum():"
print "        ax = 0"
print "        for n in args:"
print "            ax = ax + n"
print "        return ax"
print "    return sum"
print "f = lazy_sum(1, 3, 5, 7, 9)"

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print ""
print "result: f()"
print f()

print ""
print "def count():"
print "    fs = []"
print "    for i in range(1, 4):"
print "        def f(j):"
print "            def g():"
print "                return j*j"
print "            return g"
print "        fs.append(f(i))"
print "    return fs"
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
print ""
print "f1, f2, f3 = count()"
f1, f2, f3 = count()
print ""
print "result: f1()"
print f1()
print "result: f2()"
print f2()
print "result: f3()"
print f3()

print ""
print "##########################"
print "lambda test:"
print "map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])"
print "result:"
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print ""
print "f = lambda x: x * x"
print "result: f(5) =",
f = lambda x: x * x
print f(5)

print ""
print "##########################"
print "decorator test:"

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            func(*args, **kw)
            print '%s end' % (text)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2016-02-01'

print now()







