def oldage(name, age):
    year = str((100 - age) + 2021)
    print(name + "You will be 100 years old in the year " + year)


name = input("What is your name: ")
age = int(input("How old are you: "))
oldage(name, age)
