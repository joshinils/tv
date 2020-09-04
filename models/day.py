from .channel import Channel
from typing import List
from datetime import datetime


class Day:
    def __init__(self, day: datetime, channels: List[Channel]):
        self.day = day
        self.channels = Channel
