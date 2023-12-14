import cache_module
import numpy

# Prepare an RGB image containing 3 colour channels.
ROW = 1024
COL = 2048
Channel = 3
image = numpy.random.randint(0, 256, size=(ROW, COL, Channel), 
dtype=numpy.int64)

# Prepare a mask for the convolution operation.
mask_size = 3
up = 10
down = -10
mask = numpy.random.randint(down, up + 1, size=(mask_size, mask_size), 
dtype=numpy.int64)

# Prepare an empty result image. You will fill this empty array with your 
code.
result = numpy.zeros([ROW, COL, Channel], dtype=numpy.int64)

# Configuration for the cache simulator module.
l3 = ["L3", 16384, 16, 64, "LRU"]
l2 = ["L2", 4096, 8, 64, "LRU"]
l1 = ["L1", 1024, 4, 64, "LRU"]
m = 256 * 1024 * 1024
cm = cache_module.cache_module(l1, l2, l3, m)

###### WRITE YOUR CODE BELOW. ######

# 1. Load the image into the memory


# 2. Traverse the image array and apply the mask. Write the results into 
the memory through the write function. Do not fill the result array in 
this step.


# 3. Load the result image from memory through the read function.


###### WRITE YOUR CODE ABOVE. ######

cm.finish()
