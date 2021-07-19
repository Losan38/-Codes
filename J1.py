import matplotlib.pyplot as plt 
import numpy as np
import PIL

#Adresse aks
path_image = "Blank.png"
path_image2 = "RGB.png"

#baz kardan aks
pilimage = PIL.Image.open(path_image)
pilimage2 = PIL.Image.open(path_image2)

#tabdil be array/list/matirs
image = np.array(pilimage)
image2 = np.array(pilimage2)

plt.imshow(image2)
plt.show()
