import matplotlib.pyplot as plt
import numpy as np
import PIL

path_image = "Hello.jpg" #Address aks
pilimage = PIL.Image.open(path_image) #Baz kardan aks ba pillow
image = np.array(pilimage) #tabdil be np.array

#image[0][0] pixel aval

pixels_list = []

for i in range(len(image)):
    for j in range(len(image[0])):
            pixels_list.append(image[i][j])

average_pixels = np.average(pixels_list,axis=0)
print(average_pixels)

for i in range(len(image)):
    for j in range(len(image[0])):
        if image[i][j][0] > 200 and image[i][j][1] > 200 and image[i][j][2] > 200:
            image[i][j] = np.array([255,255,255])
        else:
            image[i][j] = np.array([0,0,0])

#plt.imsave('test.png', image) #Save aks
plt.imshow(image)
plt.show()

