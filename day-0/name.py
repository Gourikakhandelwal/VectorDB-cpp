import cv2
import matplotlib.pyplot as plt
#how to read an image
img=cv2.imread(r"C:\\Users\\gouri\\CV and dl\\image.jpg")#loads pixel values from memory
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#converts the image from BGR to RGB color space
plt.imshow(img_rgb)#loads pixel values from memory
print(img_rgb)
print(img_rgb[0,0])#prints the pixel value at the top left corner of the image
img_rgb[0,0]=[255,0,0]#changes the pixel value at the top left corner of the image to red
#since img bdi h toh aise nhi dikhenge pixel values we have to resize it
img_rgb=cv2.resize(img_rgb,(40,40))#resizing the image to 40x40 pixels pixel ko  bda dekhne ke lie


img_rgb[0][0]=[255,0,0]#changes the pixel value at the top left corner of the image to red
plt.imshow(img_rgb)#loads pixel values from memory
plt.show()