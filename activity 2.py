string = input("Please enter your own String: ")
string2 =  ('')
for i in string:
    string2 = i + string2
print("\nThis is the original string = ", string)
print("This is the string you reversed = ", string2)