import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
dimensions = int(raw_input("dimensions de espace a deblayer"))
mc.setBlocks(pos.x, pos.y, pos.z, pos.x + dimensions, pos.y + dimensions, pos.z + dimensions, block.AIR.id)
