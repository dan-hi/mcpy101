"""\
03_Variables.py

Exploring the use of string & numeric variables
"""

apple = 10
apple += 2
melon = 15
melon -= 3
berries = 20
pumpkin = 20 - 10
cost = apple 
cost = cost + melon 
cost = cost + 2 * berries
cost += pumpkin
print ("Total Cost:", cost, sep=' $') 

# print(f"Total Cost: ${cost}")
