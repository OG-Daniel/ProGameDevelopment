#def hello():
    #print("How are you? \n My name is Daniel \n How old are you?")
    #name = input()

#hello()

class Student():
    #properties/attributes
    name = "1212"
    age = 12
    grade = 8
    house = "blue"
    teacher = "Miss Withers"

    #constructor
    def __init__(self):
        print("Making a new student")

    #another function
    def change_details(self): 
        print("Please enter your age:\n")
        self.age = int(input())
        print("Please enter your name:\n")
        self.name = int(input())

    def show_details(self):
        print("The details of students are:\n")
        print (self.name)
        print (self.age)
        print (self.grade)
        print (self.house)
        print (self.teacher)

    

Arthur =  Student()
Gabriel = Student()

Arthur.change_details()
Arthur.show_details()
