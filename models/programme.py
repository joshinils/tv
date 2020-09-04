from datetime import datetime
from typing import Dict

from .channel import Channel, ChannelManager


class Programme:
    def __init__(self, channel: Channel, start: datetime, stop: datetime):
        self.channel: Channel = channel
        self.start: datetime = start
        self.stop: datetime = stop
        self.data: Dict = {}
        self.is_prominent = False

    @staticmethod
    def from_dict(input_dict: Dict) -> 'Programme':
        date_format: str = "%Y%m%d%H%M%S %z"
        return Programme(
            ChannelManager.get_or_create(input_dict['channel']),
            datetime.strptime(input_dict['start'], date_format),
            datetime.strptime(input_dict['stop'], date_format)
        )

    def __repr__(self):
        return f'{self.channel.name}: {self.start} -> {self.stop}'

    def __set__(self, instance, value):
        if instance not in ['channel', 'start', 'stop']:
            self.data[instance] = value

    def __get__(self, instance, owner):
        pass
