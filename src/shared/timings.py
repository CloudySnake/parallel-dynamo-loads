import time


def timeit(f):
    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print("%s took: %2.2fs" % (f.__name__, (te - ts)))  # noqa: T001
        return result

    return timed
