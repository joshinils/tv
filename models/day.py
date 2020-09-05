from .channel import Channel
from typing import List
from datetime import datetime
from .programme import Programme


class Day:
    def __init__(self, date: datetime):
        self.date = date
        self.channels = {}  # Channel.ChannelName.id : Channel

    def addPrograms(self, programs: List[Programme]):
        for prog in programs:
            self.addProgram(prog)

    def addProgram(self, prog: Programme):
        self.channels.setdefault(prog.channelName.id, Channel(prog.channelName))
        self.channels[prog.channelName.id].addProgramm(prog)
