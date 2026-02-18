#while loop#

i=1

while i<=5:
    print(i * "*")

    i=i+1


i=5

while i<=0:
    print(i * "*")

    i=i-1

    # #even numbers#
    # i=2
    # while i<=10:
    #      print(i)
    # i += 2 

    # i = 10

while i >= 1:
    print(i)
    i -= 1

    
n = int(input("Enter number: "))
i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1