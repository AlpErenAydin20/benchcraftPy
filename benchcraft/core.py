import time
from functools import wraps

def BenchCraft(unit = "s"):

    def benchcraft(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            t_start = time.perf_counter()

            try:
                result = func(*args, **kwargs)
                return result
            finally:
                t_end = time.perf_counter()
                elapsed_time = t_end - t_start

                display_time = elapsed_time *1000 if unit =="ms" else elapsed_time
                unit_label = "ms" if unit =="ms" else "s"
            
                print(f"[{func.__name__}] Run Time: {display_time:.6f} {unit_label}")

        return wrapper
    return benchcraft



