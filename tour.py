import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
# boucle for pour construire 10 rochers
for a in range(10):
    mc.setBlock(pos.x + 3, pos.y + a, pos.z, block.STONE.id)
