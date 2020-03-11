##1. class name
##2. __init__ method
##3. objects and fields
##4. methods
##5. property decorator





class Batsman:
    def __init__(self , matches, not_out, runs):
        self.matches = matches
        self.not_out = not_out
        self.runs = runs

    @property
    def average(self):
        return (self.runs)/(self.matches - self.not_out)


kunal = Batsman(100, 20, 5000)    


































































##class User:
##    pass
##
##user1 = User()
##
### here user1 is instance of class User
### user1.name , here user1 is object and name is field
### function inside the class is called method
### __init__ method (initialization aka constructor)







