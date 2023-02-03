import mcpi.minecraft as minecraft
import mcpi.block as block

# connection au serveur
mc = minecraft.Minecraft.create()
# position du joueur
pos = mc.player.getTilePos()
# construire un bloc
mc.setBlock(pos.x + 3, pos.y, pos.z, block.STONE.id)
