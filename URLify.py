def urlify(in_string):
    return "%20".join(in_string.split())

string = input("Enter a string: ")
print(urlify(string))