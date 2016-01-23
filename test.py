#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "##########################"
print "utf-8 test:"
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print "##########################"
print "print test:"
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
