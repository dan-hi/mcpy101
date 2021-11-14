def on_chat():
  agent.set_item (CARROTS, 64, 1)
  for index in range(3):
    for index2 in range (5):
      agent.till (FORWARD)
      agent.move (FORWARD, 1)
      agent.place (DOWN)
    agent.move(BACK, 5)
    agent.move(RIGHT, 2)
      
player.on_chat("carrot", on_chat)

def on_chat2() :
  for index3 in range (15):
  mobs.spawn (CHICKEN, pos(0, 0, 0))

player.on_chat ("chicken", on_chat2)

def on_chat3 () :
  for index4 in range (15):
    mobs.spawn (SNOWBALL_PROJECTILE_MOB, pos(0, 10, 0))

player.on_chat ("snowball", on_chat3)
def item_interacted_blaze_rod() :
  player.run_chat_command("carrot")
  player.run_chat_command("chicken")
  player.run_chat_command("snowball")

player.on_item_interacted (BLAZE_ROD, item_interacted_blaze_rod)

