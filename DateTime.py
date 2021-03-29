#Date and Time module

class DateTime:
    def __init__(self, hour, minute) -> None:
        self.hour = hour
        self.minute = minute
        
    def addTime(self, hour=0, minute=0) -> None:
        self.hour += hour
        self.minute += minute
        
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
    
    def toStr(self) -> str:
        return str(f'{self.hour}:{self.minute}')