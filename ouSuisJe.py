import mcpi.minecraft as minecraft

# connection au serveur
mc = minecraft.Minecraft.create()
# variable position joueur
pos = mc.player.getTilePos()
# message de position sur le jeu
mc.postToChat("x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
if pos.x == 25 and pos.z == 34:
    mc.postToChat("bienvenue a la maison")
