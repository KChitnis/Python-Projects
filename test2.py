a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("\n1) Addition\n2) Subtraction")
choice = int(input("Enter an operation => "))

def add():
    c = a + b
    return c

def sub():
    c = a - b
    return c

def check():
    if(choice == 1):
        print(add())

    else:
        print(sub())
    return 0

check()


