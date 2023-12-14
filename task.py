import cache_module
import numpy

# Prepare an RGB image containing 3 colour channels.
ROW = 32
COL = 64
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

# 1. Load the image into the memory
index = 0
for i in range(ROW):
    for j in range(COL):
        for k in range(Channel):
            value = image[i, j, k] & 0xFF  # Assuming 64-bit signed integers
            cm.write(index, value)
            index += 1


# 2. Traverse the image array and apply the mask. Write the results into 
 # the memory through the write function. Do not fill the result array in 
 # this step.
index = 0
for i in range(1, ROW - 1):
    for j in range(1, COL - 1):
        for k in range(Channel):
           # Initialize the result value
            result_value = 0

            # Apply the mask considering values outside the image as zero
            for m in range(mask_size):
                for n in range(mask_size):
                    # Check if indices are within bounds
                    if 0 <= i - 1 + m < ROW and 0 <= j - 1 + n < COL:
                        result_value += image[i - 1 + m][j - 1 + n][k] * mask[m][n]

            # Convert the result value to 64-bit signed integer
            #result_value = result_value & 0xFF
            
            # Ensure that memory stays 8-bit unsigned
            cm.write(index, result_value)  # Retain only the least significant 8 bits
            index += 1
# 3. Load the result image from memory through the read function.
            #and do not forget to convert 64 bit signed while reading to result array 
            index = 0
            for i in range(ROW):
                for j in range(COL):
                    for k in range(Channel):
                        # Read the result from memory and convert to 64bit signed integer
                        result[i, j, k] = cm.read(index) & 0xFFFFFFFFFFFFFFFF  
                        index += 1
            


###### WRITE YOUR CODE ABOVE. ######

cm.finish()
