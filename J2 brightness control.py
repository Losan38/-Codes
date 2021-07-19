import matplotlib.pyplot as plt
import numpy as np
import PIL

def checker(X):
    if X >= 255:
        X = 255
    elif X <= 0:
        X = 0
    return X

path_image = "RGB.png" #Address aks
pilimage = PIL.Image.open(path_image) #Baz kardan aks ba pillow
image = np.array(pilimage) #tabdil be np.array

#image[0][0] pixel aval

for i in range(len(image)):
    for j in range(len(image[0])):
        for c in range(len(image[i][j])):
            image[i][j][c] = checker(image[i][j][c] + 80)


plt.imsave('Brightness.png', image) #Save aks
plt.imshow(image)
plt.show()

