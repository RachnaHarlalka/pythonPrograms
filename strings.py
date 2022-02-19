name = "Rachna Harlalka"

NAME = name.upper() #it don't affect the original string

print(name)
print(NAME)
print(name.find('H')) #helps us to find the characters in our given string, if it dont find anything then it returns (-1) otherwise the index
                        # find() is case sensitive and work different for s and S

print(name.replace("Rachna" , "Ruchi ")) #it don't affect the original string

print( "Rac" in name) # in to check if a character string a part of the main string or not
print(5+2)
print(5-2)
print(5/2)  #divide but it will give decimal
print(5//2)  #divide but it will give the floor of the decimal part only
print(5*2)
print(5%2) #remainer
print(5**2) # power operator

number=5
print(2<=number)

#if statement
age = input("Please Enter your age : ")


if int(age)>=18:
    print("Major")
elif int(age)<5:
    print("You are a child")
else:
    print("Yor are in school")
print("Thank you")