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
