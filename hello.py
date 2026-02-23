#Ask the user for their name
name  = input ("What's your name? ")

#Remove whitespace from the str 'name'
name = name.strip()

#Capitalize the users name
name = name.capitalize()

#Say hello to the user
print (f"hello, {name}")
print ("hello, "+ name)


name  = input ("What's your second name? ").strip().capitalize()
print ("hello, "+ name)