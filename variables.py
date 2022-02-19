name = "Tony"
lastName = "Stark"
age = 51
is_genius = True


#Taking input from user

name = input("What is your name ?")
print("HEllow " + name)

old_age = input("What is yor age ?")
print(old_age)
#new_age = old_age+2  # this will give us error it will take old_age as string not integer
new_age = int(old_age)+2
print(new_age)

"""
float()
str()
bool()
int()
"""