from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image
import numpy as np
import os


PATH_TO_HEIGTHMAP = os.path.join("heightmap")


def fileToHeightmap(image_name):
    """Generate a 2D numpy array of pixel intensity (heightmap) from a file

    Arguments:
        image_name {String} -- name of the image

    Returns:
        np.array -- A 2D numpy array
    """
    path = os.path.join(PATH_TO_HEIGTHMAP, image_name)
    # to greyscale
    imageGrayAlpha = Image.open(path).convert('LA')
    imageNumpyArray = np.array(imageGrayAlpha)
    # do not forget the type otherwise its an uint8
    heigthMap = imageNumpyArray[:, :, 0].astype(int)
    return heigthMap



img = fileToHeightmap("france.png")

x = np.arange(len(img[0]))[::-1]
y = np.arange(len(img))
X, Y = np.meshgrid(x, y)


fig = plt.figure()


# 2D Flat image
ax = fig.add_subplot(221)
ax.imshow(img, cmap=plt.get_cmap('terrain'), vmin=0, vmax=255)

# 3D mapp
ax = fig.add_subplot(222, projection='3d')
ax.plot_surface(X, Y, img, cmap=cm.terrain,
                linewidth=0, antialiased=False, shade=True)
ax.set_zlim3d(0, 1000)

# Wireframe
ax = fig.add_subplot(223, projection='3d')
ax.plot_wireframe(X, Y, img, rstride=50, cstride=50)
ax.set_zlim3d(0, 380)

# contour map
ax = fig.add_subplot(224, projection='3d')
ax.contour(X, Y, img, cmap=cm.terrain, linewidth=0,
           antialiased=False, shade=True)
ax.set_zlim3d(0, 1000)

plt.show()
