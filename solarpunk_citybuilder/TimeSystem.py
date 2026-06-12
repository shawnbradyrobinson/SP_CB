
class TimeSystem:

    def __init__(self):
        self.delta = 1
        self.counter = 0

    def nextInstant(self) -> None:
        self.counter = self.counter + self.delta

    def changeDelta(self, new_delta) -> None:
        self.delta = new_delta

    def resetCounter(self) -> None:
        self.counter = 0

    



