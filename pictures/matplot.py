#!/usr/bin/env python
# coding=utf-8


import numpy as np
from matplotlib import pylab, mlab, pyplot
import scipy
import matplotlib.font_manager as fm
import time

x = np.arange(-8, 8, 0.1);
y = np.sin(x)
pyplot.figure(figsize=(8,4))
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.title('sin 函数'.decode('utf-8'))
pyplot.plot(x, y,'r.')
pyplot.plot(x,y,'g')
pyplot.ylim(-2, 2)
pyplot.xlim(-8, 8)
f = pyplot.gcf()
q = pyplot.gca()
print f,q
# pyplot.show()
