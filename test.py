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
