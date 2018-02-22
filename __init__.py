import operator as op
from functools import reduce
from random import random
from functools import wraps
try:
    import builtins as _
except ImportError:
    import __builtin__ as _

def rroulette(f, g, p=1/6):
    @wraps(f)
    def inner(*args, **kwargs):
        if random() < p:
            return g(*args, **kwargs)
        else:
            return f(*args, **kwargs)
    return inner

int   = rroulette(_.int, lambda v: _.int(v)-1)
float = rroulette(_.float, lambda v: _.float(v) + 0.001)
str   = rroulette(_.str, lambda v: _.str(v)[::-1])
bool  = rroulette(_.bool, lambda v: not(_.bool(v)))
len   = rroulette(_.len, lambda v: _.len(v) - 1)
ord   = rroulette(_.ord, lambda v: _.ord(v.lower() if v.isupper() else v.upper()))

abs = rroulette(_.abs, lambda v: -_.abs(v))
pow = rroulette(_.pow, lambda v, p: _.pow(v, p + 1))
min = rroulette(_.min, lambda *v: _.max(*v))
max = rroulette(_.max, lambda *v: _.min(*v))
sum = rroulette(_.sum, lambda v: reduce(op.__sub__, v))

hasattr = rroulette(_.hasattr, lambda o, n: not(_.hasattr(o, n)))

sorted = rroulette(_.sorted, lambda v: _.reversed(v))
reversed = rroulette(_.reversed, lambda v: _.sorted(v))
enumerate = rroulette(_.enumerate, lambda v: ((i + 1, _v) for i, _v in _.enumerate(v)))

globals = rroulette(_.globals, locals)
locals = rroulette(_.locals, _.globals)
id = rroulette(_.id, lambda v: _.id(_.id))

help = rroulette(_.help, lambda v: 'halp')
exit = rroulette(_.exit, print)
