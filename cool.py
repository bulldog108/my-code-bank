import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

mc.setBlocks(0, 0, 0, 100, 100, 100, block.CACTUS)
