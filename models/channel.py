class Channel:
    def __init__(self, name: str) -> None:
        self.name = name


class _ChannelManager:
    def __init__(self):
        self.channels = {}

    def get_or_create(self, name: str):
        if name in self.channels.keys():
            return self.channels[name]
        new_channel = Channel(name)
        self.channels[name] = new_channel
        return new_channel


ChannelManager = _ChannelManager()
