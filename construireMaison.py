import mcpi.minecraft as minecraft
import mcpi.block as block

# connection au serveur
mc = minecraft.Minecraft.create()
# position actuelle du joueur
pos = mc.player.getTilePos()
# variables
DIMENSION = 4
x = pos.x + 2
y = pos.y
z = pos.z
midx = x + DIMENSION / 2
midy = y + DIMENSION / 2
# construction murs exterieurs
mc.setBlocks(x, y, z, x + DIMENSION, y + DIMENSION, z + DIMENSION, block.STONE_BRICK.id)


