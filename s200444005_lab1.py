#s200444005-Gökhan Kadir Karagöz
#question1

class Calculator:

    def add(x,y):
        return(x+y)

    def substract(a,b):
        return(a-b)
    
    def multiply(c,d):
        return(c*d)
    
    def divide(k,m):
        if m == 0:
            print("You can't divide by zero")
        
        else: 
            return(k/m)

#question2

class Football:
    
    def _init_(self,stadium_name = str()):
        self.stadium_name = stadium_name
    def _init_(self,team1 = str()):
        self.team1 = team1
    def _init_(self,team2 = str()):
        self.team2 = team2
    def _init_(self,score =dict(0)):
        self.score = score
    def set_stadium(self):
        set_stadium_name = self.stadium_name
    def set_team_1(self):
        set_team_1 = self.team1
    def set_team_2(self):
        set_team_2 = self.team2
    def set_score(self):
        set_score = self.score 
    def get_stadium(self):
        return self.stadium_name
    def get_team_1(self):
        return self.team1
