import mcpi.minecraft as minecraft
import time

# connection serveur
mc = minecraft.Minecraft.create()
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat("x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
    if pos.x == 25 and pos.z == 34:
        mc.postToChat("bienvenue a la maison")
