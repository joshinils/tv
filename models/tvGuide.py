from .day import Day
from datetime import datetime
from .programme import Programme
from .channel import Channel
from collections import defaultdict


class TvGuide:
    def __init__(self):
        self.days = defaultdict(list)  # datetime.date: [Channel]

    @classmethod
    def addProgram(self, prog: Programme) -> None:
        self.days.setdefault(prog.start.date(), {})
        self.days[prog.start.date()].setdefault(
            prog.channelName.id, Channel(prog.channelName.name))
        self.days[prog.start.date()][prog.channelName.id].addProgram(prog)
