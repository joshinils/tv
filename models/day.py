from .channel import Channel
from typing import List
from datetime import datetime, timedelta, timezone
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
        self.channels[prog.channelName.id].addProgram(prog)

    def getDate(self) -> str:
        return str(self.date)

    def isToday(self) -> bool:
        LOCAL_TIMEZONE = datetime.now(timezone(timedelta(0))).astimezone().tzinfo
        return self.date == datetime.now(LOCAL_TIMEZONE).date()

    def getWochentag(self) -> str:
        weekdays = {0: "Montag",
                    1: "Dienstag",
                    2: "Mittwoch",
                    3: "Donnerstag",
                    4: "Freitag",
                    5: "Samstag",
                    6: "Sonntag"}
        return weekdays[self.date.weekday()]
