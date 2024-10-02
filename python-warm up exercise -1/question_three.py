#Question One 
# WITI has tasked you to automate a simple grading system
#As apython student, write a progarm using to display the grades that
#the students will be receing based on the mark scored in a subject
#The grades are:
#90% - 100% Grade is A
#80% - 89% Grade is  B
#70% - 79% Grade is C
#60% - 69% Grade is D
#50% - 59% Grade is E
# < 5O% Fail

def calculate_grades():
    
    #Capture stdent mark
    mark = int(input("entet mark  scored:\t"))

    #testing student mark
    if mark>=90 and mark<=100:
        print("Grade is A")
    elif mark>=80 and mark<=89:
        print("Grade is B")
    elif mark>=70 and mark<=79:
        print ("Grade is C")
    elif mark>=60 and mark <=69:
        print ("Grade is D")
    elif mark>=50 and mark<=59:
        print ("Grade is E")
    else:
        print("Fail")

#call the function
calculate_grades()