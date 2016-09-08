#!/usr/bin/env python
# coding=utf-8

l = 15
a = [[0 for j in range(l)] for i in range(l)]
# for i in a:
#     print i
# print

for i in range(l-4):
    for j in range(l):
        for k in range(5):
            a[i+k][j]+=1
for i in range(l-4):
    for j in range(l):
        for k in range(5):
            a[j][i+k]+=1

for i in a:
    print i
