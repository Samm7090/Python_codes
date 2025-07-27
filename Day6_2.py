name=input("Enter your name ")
name=name.upper()
print(name)
name=name.lower()
print(name)

#split
names=name.split(" ")
print(names[0][0]+names[1][0])          #getting initials

#1st 3init
print(names[0][0:3]+names[1][0:3])

#steping
#print(name[0:len(name):2])         #steping the name by 2nd character
print(name[::-1])                   #reverse the whole name

print(name[6::-1])                   #reverse of 1st name

print(name[len(name):6:-1])           #reverse of last name.