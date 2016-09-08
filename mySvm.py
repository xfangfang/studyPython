#!/usr/bin/env python
# coding=utf-8

import math
data = {
"a":[1,0,1,1,0,1,1,0,1,1,0,1],
"as":[1,0,1,1,0,0,1,0,1,0,1,0],
"ad":[1,0,0,1,0,1,1,0,1,1,1,1]
}
def f(x,y):
    return x*y
def d(x):
    return x*x
for i in data:
    for j in data:
        n1 = math.fsum(map(d, data[i]))
        n2 = math.fsum(map(d, data[j]))
        h = math.fsum(map(f, data[i],data[j]))
        q = h/(n1*n2)**0.5
        print math.acos(q)
