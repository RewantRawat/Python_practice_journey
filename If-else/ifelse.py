age = 2

if age >= 18:
    print("you are an adult")
    print("you can vote")
elif age<18 and age>3:
    print("You are in school")
else:
    print("You are a child")

    #Positve/negative etc

    num = int(input("Enter Number :"))

    if num>0:
        print("Positive")
    elif num>0:
        print("Negative")
    else:
      print("zero")

#Leap year logic#    

year=int(input("Enter number:"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not leap year")
