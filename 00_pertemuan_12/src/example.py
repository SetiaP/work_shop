$ ipython --pylab

Python 2.7.4 (default, Apr 19 2013, 18:28:01)
Type "copyright", "credits" or "license" for more information.

IPython 0.13.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

Welcome to pylab, a matplotlib-based Python environment [backend: Agg].
For more information, type 'help(pylab)'.

In [1]: from scipy import special, optimize

In [2]: f = lambda x: -special.jv(3, x)

In [3]: sol = optimize.minimize(f, 1.0)

In [4]: x = linspace(0, 10, 5000)

In [5]: x
Out[5]:
array([  0.00000000e+00,   2.00040008e-03,   4.00080016e-03, ...,
         9.99599920e+00,   9.99799960e+00,   1.00000000e+01])

In [6]: plot(x, special.jv(3, x), '-', sol.x, -sol.fun, 'o')

In [7]: savefig('plot.png', dpi=96)