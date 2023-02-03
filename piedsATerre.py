# coding=utf-8
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connection au jeu
mc = minecraft.Minecraft.create()


def piedsATerre():
    # recuperer la position du joueur
    pos = mc.player.getTilePos()
    bloc = mc.getBlock(pos.x, pos.y - 1, pos.z)
    # pos.y-1 = bloc position sous le pied du joueur
    # si le joueur est sur l'eau ou dans le vide
    if bloc == block.AIR.id or bloc == block.WATER_STATIONARY.id or bloc == block.WATER_FLOWING.id:
        mc.postToChat("vous etes en danger !")
    else:
        mc.postToChat("vous etes en securite !")


while True:
    time.sleep(0.5)
    piedsATerre()
