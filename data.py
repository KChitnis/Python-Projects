total = int(input("Enter total number of students: "))

def display():
    print("")
    print("Name: " + name)
    print("Age: " + age)
    print("Marks: " + marks)
    return 0

i = 0
while i < total:
    print("")
    name = input("Enter name: ")
    age = input("Enter age:")
    marks = input("Enter marks: ")
    i += 1

d = input("\nShow Data? (y/n): ")
if(d == 'y' or d == 'Y'):
    i = 0
    while i < total:
        print("--DATA--")
        display()
        i += 1
else:
    exit(1)

