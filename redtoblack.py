import numpy as np
import cv2

#read the image as numpy array
#it will be a 3D array

#"image.jpg" is the name of the image we want to modify. Use appropriate
#name or path at that place 
img = cv2.imread('image1.png')
#display thr original image
cv2.imshow("Image with red eye",img)
#image.shape returns an array having width as the first
#element, height as 2nd as number of color channels as 3rd
shape=img.shape

#loop over every pixel of the image and check if it falls
#under the category of red

#first loop for looping over every pixel row in the image
for i in range(shape[0]):
    #inner loop for looping over every pixel column
    for j in range(shape[1]):
        #now we will decide the criteria for a pixel to be red
        #in the numpy array of the image the pixel color values
        #are in the order b,g,r(blue,green,red)

        #below condition implies that if the blue content in the
        #pixel is in the range(0,220) and green in range(0,100) and
        #red in range(125,255) then we will change the color of that
        #pixel to red

        #img[i][j] will have an array with 3 values [b,g,r]
        #we have to alter these values for changing the color
        if(img[i][j][0]>=0 and img[i][j][1]>=0 and img[i][j][2]>=125
           and img[i][j][0]<=220 and img[i][j][1]<=100 and img[i][j][2]<=255):
            #change color to black
            img[i][j]=[0,0,0]
#save the edited image as new image2.jpg
cv2.imwrite("image2.jpg", img)
#display the modified image
cv2.imshow("Image without red eye",img)


