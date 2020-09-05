from datetime import datetime, timedelta, timezone
from typing import Dict
from .channelName import ChannelName

LOCAL_TIMEZONE = datetime.now(timezone(timedelta(0))).astimezone().tzinfo


class Programme:
    def __init__(self, channelName: ChannelName, start: datetime, stop: datetime):
        self.channelName: ChannelName = channelName
        date_format: str = "%Y%m%d%H%M%S %z"

        self.start = datetime.strptime(start, date_format).astimezone(LOCAL_TIMEZONE)
        self.stop = datetime.strptime(stop, date_format).astimezone(LOCAL_TIMEZONE)

        self.data: Dict = {}
        self.prominent = False
        if self.start.hour >= 20 and self.start.minute >= 1:
            self.prominent = True
        if self.start.hour >= 21:
            self.prominent = True
        self.onPrevDay = False
        now = datetime.now(LOCAL_TIMEZONE)
        self.nowRunning = now >= self.start and now <= self.stop

    def startTime(self) -> str:
        return self.start.strftime("%H:%M")

    def catgy(self) -> str:
        return self.data["category"]

    def __repr__(self):
        return f'{self.channel.name}: {self.start} -> {self.stop}'

    def __set__(self, instance, value):
        if instance not in ['channel', 'start', 'stop']:
            self.data[instance] = value

    def __get__(self, instance, owner):
        pass
