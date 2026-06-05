import cv2
import matplotlib.pyplot as plt
#how to read an image
img=cv2.imread(r"C:\\Users\\gouri\\CV and dl\\image.jpg")#loads pixel values from memory
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)#loads pixel values from memory
plt.show()#displays the image 
#opencv uses bgr however matplot expects rgb
print(rgb_img.shape)

#(255,255,3) rows,columns,channels
#channels are the color channels in the image, in this case 3 for red, green and blue.