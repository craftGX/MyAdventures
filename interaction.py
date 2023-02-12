# coding=utf-8
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connection au jeu
mc = minecraft.Minecraft.create()

position_diamant = mc.player.getTilePos()
position_diamant.x = position_diamant.x + 1
mc.setBlock(position_diamant.x, position_diamant.y, position_diamant.z, block.DIAMOND_BLOCK.id)


def verification_frappe():
    global position
    hits = mc.events.pollBlockHits()
    for hit in hits:
        position = position.i
        if position.x == position_diamant.x and position.y == position_diamant.y and position.z == position_diamant.z:
            mc.postToChat("touché !")


while True:
    time.sleep(1)
    verification_frappe()
