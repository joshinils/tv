from .day import Day
from datetime import datetime
from .programme import Programme
from .channel import Channel
from collections import defaultdict


class TvGuide:
    def __init__(self):
        self.days = defaultdict(Day)  # datetime.date: Day

    def addProgram(self, prog: Programme) -> None:
        self.days.setdefault(prog.start.date(), Day(prog.start.date()))
        self.days[prog.start.date()].addProgram(prog)
