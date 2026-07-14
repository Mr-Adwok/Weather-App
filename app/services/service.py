import time
import functools


class APIService():
    async def get_city_route_by_name(self,city:str):
        return city



def measure_execution_time(func):
    """A decorator to measure and print the execution time of a function."""

    @functools.wraps(func)
    async def wrapper(*args,**kwargs):
        # start_time
        start_time =  time.perf_counter()
        result = await func(*args,**kwargs)
        end_time = time.perf_counter()
        execution_time_ms = (end_time- start_time) * 1000
        print(f"'{func.__name__}' executed in {execution_time_ms:.4f} ms")
        return result
    return wrapper




