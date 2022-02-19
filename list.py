friends = ["Sruti","Seema","ankita","poonam","joyshree","priyanka"]
print(friends[-1])
# print(friends[2])
# print(friends[0])
# print(friends[4])

for i in friends:
    print(i)
print(friends[0:3])
print(friends)

friends.append("uttara") #to append new data at the end
print(friends)

friends.insert(0,"syan") #to insert new data in some index
print(friends)

print(len(friends)) #gives the length of the list

print("seema" in friends)  #checks if seema exist in the list

i=0
while i < len(friends):
    print(friends[i])
    i=i+1

friends.clear() #clears the
print(friends)
