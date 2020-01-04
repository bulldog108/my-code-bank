import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
mc.postToChat("a transporter adventure")
transporter1 = mc.player.getTilePos()
mc.setBlock(transporter1.x, transporter1.y - 1,
transporter1.z, block.DIAMOND_BLOCK)
mc.postToChat("find a second location in thirty second")
transporter2 = mc.player
