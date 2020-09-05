from .day import Day
from datetime import datetime, timedelta
from .programme import Programme
from .channel import Channel
from collections import defaultdict


class TvGuide:
    def __init__(self):
        self.days = defaultdict(Day)  # datetime.date: Day

    def addProgram(self, prog: Programme) -> None:
        dateToUse = prog.start.date()
        if prog.start.hour < 6:
            dateToUse -= timedelta(days=1)
            prog.onPrevDay = True
        self.days.setdefault(dateToUse, Day(dateToUse))
        self.days[dateToUse].addProgram(prog)
