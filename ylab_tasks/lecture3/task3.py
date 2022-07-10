#!/usr/bin/env python3
"""Solution of task3 from the lecture3."""
import redis
from functools import wraps
from typing import Union


def memoized(redis_client: Union[bool, redis.Redis] = False):
    if redis_client:
        memory = redis_client
    else:
        memory = {}

    def wrapper(func):
        @wraps(func)
        def inner(arg):
            memoized_result = memory.get(arg)
            if memoized_result is None:
                print("Calculate the result...")
                memoized_result = func(arg)
                if redis_client:
                    memory.set(name=arg, value=memoized_result)
                else:
                    memory[arg] = memoized_result
            else:
                memoized_result = int(memoized_result)
                print("Retrieving the result...")
            print(f"Result is {memoized_result}")

            return memoized_result

        return inner

    return wrapper


if __name__ == '__main__':
    client = redis.Redis()

    @memoized(client)
    def multiplier(number: int):
        """Multiplies by 2"""
        return number * 2

    multiplier(8)
    multiplier(8)
    multiplier(1)
    multiplier(8)
    multiplier(1)

    client.close()
