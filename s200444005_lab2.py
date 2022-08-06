#200444005 Gökhan Kadir Karagöz 
#question 1

class ContestResult(object):
    def __init__(self, winner, second_place, third_place):
        self.winner = winner
        self.second_place = second_place
        self.third_place = third_place

Stick = ContestResult("x ", "y", "z")
Stick.second_place 


#question 2 


class WeatherForecast():
    
    high = 0
    low = 0
    skies = "  "
    def set_skies(self, skies):
        self.skies = skies
    def get_skies(self):
        return self.skies
    def set_high(self, high):
        self.high = high
    def get_high(self):
        return self.high
    def set_low(self, low):
        self.low = low
    def get_low(self):
        return self.low