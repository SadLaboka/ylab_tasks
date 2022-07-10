#!/usr/bin/env python3
"""Solution of task4 from the lecture3."""
from functools import wraps
from time import sleep


def reuse(
        call_count: int,
        start_sleep_time: int,
        factor: int,
        border_sleep_time: int):

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            pause_time = start_sleep_time
            print(f"Количество запусков = {call_count}\nНачало работы.")
            for i in range(1, call_count + 1):
                sleep(pause_time)
                func_result = func(*args, **kwargs)
                print(f"Запуск номер {i}. Ожидание: {pause_time}с . "
                      f"Результат декорируемой функций = {func_result}.")
                pause_time *= 2 ** factor
                if pause_time >= border_sleep_time:
                    pause_time = border_sleep_time

            return

        return inner

    return wrapper


if __name__ == "__main__":
    @reuse(call_count=3, start_sleep_time=1, factor=2, border_sleep_time=8)
    def multiplier(number: int):
        """Multiplies by 2"""
        return number * 2

    multiplier(5)
