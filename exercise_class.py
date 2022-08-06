#200444005 Gökhan Kadir Karagöz

#QUESTION 1

class Counter:
    def __init__(self, counter, limit):
        self.counter = counter
        self.limit = limit
    def increment(self):
        if self.counter < self.limit:
            self.counter = self.counter + 1
    def decrement(self):
        if self.counter > 0:
            self.counter = self.counter - 1
    def get_counter(self):
        return self.counter

#QUESTION 2

class Player:

  def __init__(self):
    self.name = ""
    self.score = 0

  def set_name(self, new_name):
    self.name = new_name

  def set_score(self, new_score):
    self.score = new_score

  def get_name(self):
    return self.name
   
  def get_score(self):
    return self.score




