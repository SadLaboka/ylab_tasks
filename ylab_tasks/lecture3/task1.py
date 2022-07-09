#!/usr/bin/env python3
"""Solution of task1 from the lecture3"""


class CyclicIterator:

    def __init__(self, value):
        if self.is_order(value):
            self.value = value
        else:
            self.value = sorted(value)

    def __iter__(self):
        self.current_index = -1
        return self

    def __next__(self):
        if self.current_index < len(self.value) - 1:
            self.current_index += 1
            return self.value[self.current_index]
        else:
            self.current_index = 0
            return self.value[self.current_index]

    @staticmethod
    def is_order(value):
        if isinstance(value, (set, dict, frozenset)):
            return False
        return True


if __name__ == '__main__':
    cyclic = CyclicIterator(range(3))
    for i in cyclic:
        print(i)
