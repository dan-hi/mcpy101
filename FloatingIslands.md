# Floating Islands

## 1. Island 1

### A. Types
`string`:
```
say("Hello World!")
```

Fix the errors below:
```
say("Once upon a time")
say("There was a mysterious world...)
say(In which everything was made out of blocks, exactly the same size.)
say(Also in this world was a village, perched on top of some floating islands.")
say(How the island floats, no one knows...)
```

In addition to `string`, there are three other types of variables that you can also `say()` or `print()`:
```
say(23)    # integer
say(74.2)  # float
say(True)  # Boolean
say(False) # Boolean
```

### B. Variables
```
# Edit the text (String) below to add your own message
my_amazing_variable = "Test" 

# This line below outputs the contents of your variable to game chat
say(my_amazing_variable)
```

Overwriting a variable
```
my_amazing_variable = "Bad news"
# Add your code below

# The line beneath outputs the contents of the variable to game chat
say(my_amazing_variable)
```
variables can be overwritten with different types:
```
variable_name = data_being_stored
For example

name = "bob"
age = 5
```

### C. Agent Test
```
agent.move("forward")
agent.move("back")
agent.move("left")
agent.move("right")
agent.move("up")
# agent.move("down")
```

# Island 2
```

if world.weather == "rain":
    say("It's raining, quickly get inside!")
else:
    say("It's", world.weather, "outside.")
```
    
## Indentation
```
# Try changing the name below
current_weather = world.weather

if current_weather == "clear":
    say("The weather is nice and clear")
    say("No coat needed!")
else:
    say("It's raining! Get your coat quick!")
    
# outside the if- else statement, so this always runs
say("And that completes your weather information")
```
## Carrot and Wheat Checking
```
agent.move("forward")
agent.move("forward")
agent.move("forward")

# Check the seeds
block = agent.inspect("down")
say(block)
if(block == "wheat"):
    accept() 
else:
    deny()    
```
## Collecting Forest Wood
```
broadcast_position()

if (is_nest() == True):
    say("I found a nest!")
    next()
else:
    say("No Nest")
    harvest()
    next()
```

## Collecting Iron Ore
```
direction = "right"

Found = agent.inspect(direction)
say(Found)
while Found == "air":
    agent.move(direction)
    Found = agent.inspect(direction)
    say(Found)

if Found == "iron_ore":
    agent.destroy(direction)
```
## Purity Of Iron Ore
_avoid saying "iron purity"_ because iron and purity are both nouns.
```
if(purity("forward") <= 3):
    deny()
    say("Purity less than or equal to 3!")
# Add your else code below

else:
    say("Purity is acceptable!")
    accept()
```

## Lesson 3 Intro to Loops

When you know the number of times to iterate, use the `for` loop (don't forget the `:` at the end):

```
for count in range(0,8):
    say(count, "via say")
```
### Covering Hatches
```
for count in range(0,7):     
    agent.place(1, "down")
    agent.move("forward")
```
### Making a Gangplank
```
for count in range(0,11):
    agent.place(1, "down")
    agent.move("forward")
```
### Finding a Spellbook
```
for count in range(0,4):    
    if found_book("forward"):
        say("Found the book!")
        mark_book("forward")
    else:
        say("Spell book not found on this shelf")
    agent.move("up")

```
### Mining For Gold
```
for tunnel in range(0, 3):
#     # Complete the for loop above to repeat 3 times!
#     agent.move("forward")
    agent.move("forward")

    say("FORWARD")
    say("  digging...")
    for dig in range(0,3):
        agent.destroy("down")
        agent.move("down")

    say("  inspecting...")
    if(agent.inspect("down") == "gold_ore"):
        agent.destroy("down")

    say("  rising...")        
    for rise in range(0,3):
        agent.move("up")

    agent.move("forward")       
    # Add the final code to move the agent forward, below
    ```
## Using Variables
```
block = agent.inspect("down")
if(block == "wheat"):
    
    # Add an agent.destroy above and complete the agent.place below!
    agent.place(1,"down")
    say("Wheat!")
```
### Lesson 4
```
## Building A Bridge
```
while agent.inspect("forward") == "air":
    agent.move("forward")
    agent.place(1, "down")
    # Add the code above here
say("I've reached the end")
```
## Mining For Diamonds
```
found_diamond = 0
while found_diamond < 3:
    if check_ore("forward") == "diamond_ore":
        mark_diamond()
        # Complete the line above 
        found_diamond = found_diamond + 1
    else:
        mark_bin()
        # Complete the line above to dispose of other ores
```
## Picking Flowers
```
while agent.get_item_count(1) < 4:
    agent.move("forward")
    if check_flower("down") == "poppy":    # Tip, on this line, make sure there is no extra spaces within the speech marks!
        agent.destroy("down")
        # Complete the 2 lines above.
```

# Island 5
Help Building a telescope. First build two towers.  Later, insert pieces from inventory spot 1.
## Building Towers
```
def build_tower():
    for height in range(0, 15):
        agent.move("up")
        draw_square(3)
```
### Getting Data
```
def decode(info):
    if info == "a":
        return 1
    elif info == "b":
        return 2
    elif info == "c":
        return 3
    elif info == "d":
        return 4
```
### Wiring It Up
```
def on_player_travelled(location, mode, distance):
    loc = correct_location(location)
    agent.teleport(loc)
    agent.place(1, "down")
    
    # Add your code to the line above
```
## Island 6
Learning about lists.
## Learning about plants
```
block = agent.inspect("down")

hydration = get_hydration(block)
nutrition = get_nutrition(block)
strength = get_strength(block)

# Create a new list below containing your variables above
plant_info = [block, hydration, nutrition, strength] 

# This will submit the information to the scientists to compare with their results
submit(plant_info)
```
## Finding Fossils
```
coordinates = []

for row in range(0,4):
    for col in range(0,4):
        if is_fossil_below():
            coordinates.append(agent.position)
            # Add your append code above
            say("Fossil!")
        agent.move("forward")
    return_agent()
    agent.move("left")

# Submit co-ordinates for checking
submit(coordinates)
```
## Checking the Rocket
```
for kfjeija in range(0, 26):
# Complete the for loop above to run 26 times
    block = agent.inspect("forward")
    if (block in accepted_blocks):
        say("Accept")
        accept()
    else:
        say("Deny")
        deny()
    agent.move("up")
    # Add and agent.move above to move your agent up
```
## Helping a Airport
```
for row in runway_design:
    for block in row:
        agent.place(block, "down")
        agent.move("right")
        # Add code above to move the Agent to the right
    return_agent()
    agent.move("forward")
    # Add code above to move the Agent forward
```
