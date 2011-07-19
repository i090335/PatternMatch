# -*- coding: utf-8 -*-
'''
    assignment1.no2
    created by 25090335 Kohki Miki on 2011/07/19
'''
from pattern.model import Pattern
from pattern import patterns

if __name__ == '__main__':
    pattern = patterns[2]
    count = 0
    p = 0
    for i in xrange(100):
        handmade = pattern.generate_handmade(p/25.0)
        if pattern in handmade.nearest_pattern(patterns):
            count += 1
    print count