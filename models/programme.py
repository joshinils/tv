from datetime import datetime
from typing import Dict

from .channel import Channel, ChannelManager


class Programme:
    def __init__(self, channel: Channel, start: datetime, stop: datetime):
        self.channel: Channel = channel
        self.start: datetime = start
        self.stop: datetime = stop

    @classmethod
    def from_dict(cls, input_dict: Dict) -> 'Programme':
        date_format = "%Y%m%d%H%M%S %z"
        return cls(
            ChannelManager.get_or_create(input_dict['channel']),
            datetime.strptime(input_dict['start'], date_format),
            datetime.strptime(input_dict['stop'], date_format)
        )
