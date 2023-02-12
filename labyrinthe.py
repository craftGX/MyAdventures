# coding=utf-8
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connection au jeu
mc = minecraft.Minecraft.create()

BLOC_VIDE = block.AIR.id
MUR = block.GOLD_BLOCK.id
SOL = block.GRASS.id
# ouverture du fichier contenant les données du labyrinthe
NOM_DU_FICHIER = "labyrinthe.csv"
fichier = open(NOM_DU_FICHIER, "r")
# localiser notre joueur
position_joueur = mc.player.getTilePos()
ORIGINE_X = position_joueur.x + 1
ORIGINE_Y = position_joueur.y
ORIGINE_Z = position_joueur.z + 1
# point de départ du labyrinthe
z = ORIGINE_Z
# lire chaque ligne du fichier
for line in fichier.readlines():
    data = line.split(",")
    x = ORIGINE_X  # ré-initialise x à chaque nouvelle rangée du labyrinthe
    for cell in data:
        if cell == "0":
            b = BLOC_VIDE
        else:
            b = MUR
        mc.setBlock(x, ORIGINE_Y, z, b)
        mc.setBlock(x, ORIGINE_Y+1, z, b)
        mc.setBlock(x, ORIGINE_Y-1, z, SOL)
        x = x + 1 # mise à jour des coordonnées de x
    z = z + 1
