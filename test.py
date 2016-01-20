#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "hello,    world!     "

print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

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


