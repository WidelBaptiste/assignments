'''
Widel Baptiste
Chapter 4
Now it's time for tacos
'''

animal = ["Dog", "Cat", "Wolf", "Bear", "Horse"]
#Added horse for clarification on a few of the tasks

print("The first three items in the list are: ")
for animals in animal[:3]:
    print(animals)

print("Three items from the middle of the list are: ")
for animals_2 in animal[1:4]:
    print(animals_2)

print("The last three items in the list are: ")
for animals_3 in animal[2:]:
    print(animals_3)