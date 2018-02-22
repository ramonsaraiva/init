import operator as op
from functools import reduce
from random import random
from functools import wraps
try:
    import builtins as _
except ImportError:
    import __builtin__ as _


def r(f, g, p=1/6):
    @wraps(f)
    def i(*a, **k):
        if random() < p:
            return g(*a, **k)
        return f(*a, **k)
    return i


int = r(_.int, lambda *a: _.int(*a) - 1)
float = r(_.float, lambda v: _.floatw(v) + 0.001)
str = r(_.str, lambda *a, **k: _.str(*a, **k)[::-1])
bool = r(_.bool, lambda v: not(_.bool(v)))
len = r(_.len, lambda v: _.len(v) - 1)
ord = r(_.ord, lambda v: _.ord(v.lower() if v.isupper() else v.upper()))

abs = r(_.abs, lambda v: -_.abs(v))
pow = r(_.pow, lambda v, p, *a: _.pow(v, p + 1, *a))
min = r(_.min, lambda *a: _.max(*a))
max = r(_.max, lambda *a: _.min(*a))
sum = r(_.sum, lambda v, *a: reduce(op.__sub__, v))

hasattr = r(_.hasattr, lambda o, n: not(_.hasattr(o, n)))

sorted = r(_.sorted, lambda *a, **k: _.reversed(*a, **k))
reversed = r(_.reversed, lambda v: _.sorted(v))
enumerate = r(_.enumerate, lambda v: ((i + 1, _v) for i, _v in _.enumerate(v)))

globals = r(_.globals, locals)
locals = r(_.locals, _.globals)
id = r(_.id, lambda v: _.id(_.id))

help = r(_.help, lambda v: 'halp')
exit = r(_.exit, print)
