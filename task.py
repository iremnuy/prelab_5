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

# Prepare an empty result image. You will fill this empty array with your code. 
result = numpy.zeros([ROW, COL, Channel], dtype=numpy.int64)

# Configuration for the cache simulator module.
l3 = ["L3", 16384, 16, 64, "LRU"]
l2 = ["L2", 4096, 8, 64, "LRU"]
l1 = ["L1", 1024, 4, 64, "LRU"]
m = 256 * 1024 * 1024
cm = cache_module.cache_module(l1, l2, l3, m)

###### WRITE YOUR CODE BELOW. ######

#Row-major order is the default in NumPy (for Python). Row-major order is used in C/C++
#Column major: FORTRAN
#optimization: use channel-row-column order to reduce cache misses.

index = 0

 #1. Load the image into the memory
for k in range(Channel):
    for j in range(ROW):
        for i in range(COL):
            value = image[j, i, k] & 0xFF  # Corrected indices
            cm.write(index, value)
            index += 1

# Reset index for convolution operation
index = 0

# 2. Traverse the image array and apply the mask
for k in range(Channel):
    for j in range(1, ROW - 1):
        for i in range(1, COL - 1):
            result_value = 0
            for m in range(mask_size):
                for n in range(mask_size):
                    if 0 <= i - 1 + m < ROW and 0 <= j - 1 + n < COL:
                        result_value += cm.read(index + (j - 1 + m) * COL + (i - 1 + n)) * mask[m, n]
            cm.write(index + i * COL + j, result_value & 0xFF)

# 3. Load the result image from memory
index = 0
for k in range(Channel):
    for j in range(ROW):
        for i in range(COL):
            result[j, i, k] = cm.read(index) & 0xFFFFFFFFFFFFFFFF
            index += 1

# Save the result arrays to respective CSV files
#numpy.savetxt("result_red.csv", result[:, :, 0], delimiter=",")
#numpy.savetxt("result_blue.csv", result[:, :, 1], delimiter=",")
#numpy.savetxt("result_green.csv", result[:, :, 2], delimiter=",")

print(result[5,10,2])

###### WRITE YOUR CODE ABOVE. ######

cm.finish()
