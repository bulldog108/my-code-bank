import mcpi.minecraft as minecraft
import time 

mc = minecraft.Minecraft.create()

time.sleep(1)
pos = mc.player.getPos()

mc.postToChat("You are located x=" +str(pos.x) + ", Y=" +str(pos.y) +", Z=" +str(pos.z))
