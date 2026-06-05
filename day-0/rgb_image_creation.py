import numpy as np
import matplotlib.pyplot as plt
#creating a blank image
img=np.zeroes((3,3,3),dtype=np.uint8)#creates a 3x3 pixel image with 3 color channels (RGB) and all pixel values set to 0 (black)
plt.title("RGB Image")#sets the title of the plot
plt.imshow(img)#displays the image
plt.show()#displays the plot
img[0,0]=[255,0,0]#sets the pixel value at the top left corner of the image to red
img[0,1]=[0,255,0]#sets the pixel value at
#the top middle of the image to green
plt.show()