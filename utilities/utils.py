import time
import os


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r  %.8f seconds' % (method.__name__, (te - ts)))
        return result

    return timed


def file_exists(file_name: str) -> bool:
    return os.path.exists(file_name)


def delete_file(file_name: str):
    if os.path.exists(file_name):
        os.remove(file_name)



