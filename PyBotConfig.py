import ConfigParser

class PyBotConfig():
    def __init__(self, file):
        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.read(file)

    def get(self,key):
        return self.config.get("PyBot", key)

