
class TimeSystem:

    def __init__(self):
        self.delta = 1
        self.counter = 0
        self.hour_divisor = 1000 # divide the counter by THIS to get your in-game hours 
        self.hours_passed = 0 
        self.days_passed = 0 
        self.months_passed = 0 
        self.years_passed = 0



    def nextInstant(self) -> None:
        self.counter = self.counter + self.delta

    def changeDelta(self, new_delta) -> None:
        self.delta = new_delta

    def resetCounter(self) -> None:
        self.counter = 0

    def clockHours(self) -> None:
        if self.counter / self.hour_divisor >= 1:
            self.hours_passed = self.hours_passed + 1
            self.resetCounter() 
            return 
        else:
            return 

    def clockDays(self) -> None:
        if self.hours_passed / 24 >= 1:
            self.days_passed = self.days_passed + 1
            self.hours_passed = 0 
            return 
        else: 
            return 

    def clockMonths(self) -> None:
        if self.days_passed / 30 >= 1:
            self.months_passed = self.months_passed + 1
            self.days_passed = 0 
            return 
        else:
            return 

    def clockYears(self) -> None:
        if self.months_passed / 12 >= 1:
            self.years_passed = self.years_passed + 1
            self.months_passed = 0 
            return 
        else: 
            return 

    def getHours(self) -> int:
        return self.hours_passed
    
    def getDays(self) -> int:
        return self.days_passed
    
    def getMonths(self) -> int:
        return self.months_passed
    
    def getYears(self) -> int:
        return self.years_passed
    
    def getCounter(self) -> int:
        return self.counter 
    
    def TickTickTick(self):
        self.clockHours()
        self.clockDays()
        self.clockMonths()
        self.clockYears()
        return 
    



