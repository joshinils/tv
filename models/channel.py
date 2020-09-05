from typing import List
from .programme import Programme
from .channelName import ChannelName


class Channel:
    def __init__(self, name: ChannelName) -> None:
        self.name = name
        self.programs = []

    def addPrograms(self, programs: List[Programme]):
        for prog in programs:
            self.addProgram(prog)

    def addProgram(self, prog: Programme):
        if prog.channelName.id == self.name.id:
            self.programs.append(prog)
