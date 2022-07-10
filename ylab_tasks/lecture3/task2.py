#!/usr/bin/env python3
"""Solution of task2 from the lecture3"""
from dataclasses import dataclass
from datetime import datetime
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        one_day = 86400
        for period in self.dates:
            day = period[0].timestamp()
            stop = period[1].timestamp()
            while day <= stop:
                yield datetime.fromtimestamp(day).isoformat(sep=" ")
                day += one_day


if __name__ == '__main__':
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
