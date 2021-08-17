# MineCraft Python 101
(_[Click here to go to Floating Islands](FloatingIslands.md)_)

## Lesson 1:  Syntax
```
player.say("Hi")
```

## Lesson 2: Learning about Relative Coordinates
* Place brick block (on the ground)
    ```
    blocks.place(BRICKS, pos(0, 0, 0))
    ```
* Place redstone lamp in the ceiling
    ```
    blocks.place(REDSTONE_LAMP, pos(0, 7, 0))
    ```

## Lesson 3: Variables
### Activity 1
```
a = "apple"
b = "berries"
c = "cherries"
fruit = a
player.say(fruit)
fruit = b
player.say(fruit)
```
### Activity 2
```
location1 = world(-24, 40, -18)
location2 = world(-31, 40, -11)
location3 = world(-28, 40, -16)
location4 = world(-25, 40, -13)
location5 = world(-31, 40, -17)
# Replace the lines below with your code #
# place block at location1 command
blocks.place(MELON_BLOCK, location1)
# place block at location2 command
blocks.place(MELON_BLOCK, location2)
# place block at location3 command
blocks.place(PUMPKIN, location3)
# place block at location4 command
blocks.place(PUMPKIN, location4)
# place block at location5 command
blocks.place(MELON_BLOCK, location5)
```
### Activity 3
```
apple = 10
# change to: apple = apple + 2
apple += 2
melon = 15
# change to: melon = melon - 3
melon -= 3
berries = 20
# pumpkin = berries - apple
pumpkin = 20 - 10
# Replace the lines below with your code #
# cost of apples | Step 2
cost = apple
# add melon                           | Step 3
cost = cost + melon
# add berries                          | Step 3
cost = cost + 2 * berries
# add potatos     | Step 1
cost = cost + potato
# add pumpkin
cost = cost + pumpkin
player.say(cost)
```

# Lesson 4: Lists

# Lesson 5: Loops

## Activity 1 
Program the agent to collect dirty clothes in a 7 x 2 rectangle and bring them back "to start."
```
for c in range(0, 7):
    agent.move(FORWARD, 1)
    agent.collect_all()
# end of loop 1
agent.move(RIGHT, 1)
agent.collect_all()
for m in range(0, 7):
    agent.move(BACK, 1)
    agent.collect_all()

agent.drop_all(RIGHT)
```

## Activity 2

```
for q in range(0, 4):  
# loop number 3                                 | Part 2
# loop number 1
    for e in range(0, 7):
        agent.move(FORWARD, 1)
        agent.collect_all()
# end of loop 1
    agent.move(RIGHT, 1)
    for r in range(0, 7):
        agent.move(BACK, 1)
        agent.collect_all()
    agent.drop_all(RIGHT)
```

# Lesson 6: Conditionals
The lesson seems to have a bug!


# Lesson 7: While Loops
building a wall
```
while agent.detect(AgentDetection.REDSTONE, FORWARD):
    # Make the Agent place a block to its right         |Part 2
    agent.place(RIGHT)
    # Make the Agent move up                            |Part 2
    agent.move(UP, 1)
    # Make the Agent place a block to its right         |Part 2
    agent.place(RIGHT)
    # Make the Agent move back down                     |Part 2
    agent.move(DOWN, 1)
    # Make the Agent move forward               |Part 1
    agent.move(FORWARD, 1)
    # End of while loop                                

```
