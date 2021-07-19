# MineCraft Python 101

## Lesson 1
```
player.say("Hi")
```

## Lesson 2
* Place brick block (on the ground)
    ```
    blocks.place(BRICKS, pos(0, 0, 0))
    ```
* Place redstone lamp in the ceiling
    ```
    blocks.place(REDSTONE_LAMP, pos(0, 7, 0))
    ```

## Lesson 3
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
melon = 15
berries = 20
potato = 2
# Replace the lines below with your code #
# cost of apples | Step 2
cost = apple
# add melon                           | Step 3
cost = cost + melon
# add berries                          | Step 3
cost = cost + 2 * berries
# add potatos     | Step 1
cost = cost + potato
player.say(cost)
```
