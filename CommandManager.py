commandList = []

class Commander:
    def __init__(self):
        self.keys = []
        self.description = '' # information of key

        commandList.append(self)

    @property
    def __keys(self):
        return self.keys

    @__keys.setter
    def __keys(self, array):
        for arg in array:
            self.keys.append(arg.lower())

    def answer(self):
        pass