import numpy as np
import matplotlib.pyplot as plt
#image creation
img=np.zeros((20,20),dtype=np.uint8)#creates a 20x20 pixel image with all pixel values set to 0 (black)


img[2,5:15]=255
img[10,5:15]=255
img[2:10,15]=255
plt.imshow(img,cmap='gray')#displays the image in grayscale
plt.show()
print(img.shape)