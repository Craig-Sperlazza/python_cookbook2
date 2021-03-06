import timeit

def timethis(method):
    def timed(*args, **kw):
        ts = timeit.default_timer()
        result = method(*args, **kw)
        te = timeit.default_timer()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r %2.15f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

@timethis
def append_one(l):
    l.append(1)

my_list = [x for x in range(int(11464873))]

for i in range (20):
    append_one(my_list)