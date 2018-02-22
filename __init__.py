import operator as op
from functools import reduce

_ = __builtins__

int = lambda v: _.int(v - 1)
float = lambda v: _.float(v + 0.001)
str = lambda v: _.str(v)[::-1]
bool = lambda v: not(_.bool(v))
len = lambda v: _.len(v) - 1
ord = lambda v: _.ord(v.lower() if v.isupper() else v.upper())

abs = lambda v: -_.abs(v)
pow = lambda v, p: _.pow(v, p + 1)
min = lambda *v: _.max(*v)
max = lambda *v: _.min(*v)
sum = lambda v: reduce(op.__sub__, v)

hasattr = lambda o, n: not(_.hasattr(o, n))

sorted = lambda v: _.reversed(v)
reversed = lambda v: _.sorted(v)
enumerate = lambda v: ((i + 1, _v) for i, _v in _.enumerate(v))

globals = locals
locals = _.globals
id = lambda v: _.id(_.id)

help = lambda v: 'halp'
exit = print