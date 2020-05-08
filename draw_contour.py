from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image
import numpy as np
import os


PATH_TO_HEIGTHMAP = os.path.join("heightmap")


def showImageFromArray(imageArray, axe):
    """ Display a nice grayscale image for visual checking

    Arguments:
        imageArray {np.array} -- 2D array of pixel 
    """
    axe.imshow(imageArray, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)


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


# From a subjective view, a pixel is about 1km
# So divide the height so 255 is 3800m (france)
# and put a 10 scale to be visible on chart

# FIXME : on 3D plot the y  axis is wrong


def showWireframeFromArray(imageArray, axe, r=100, c=100):
    # Sampling
    # FIXME   
    x = np.arange(len(imageArray[0]))[::-1]
    y = np.arange(len(imageArray))
    X, Y = np.meshgrid(x, y)
    axe.plot_wireframe(X, Y, imageArray, rstride=r, cstride=c)
    axe.set_zlim3d(0, 1000)





img = fileToHeightmap("france.png")

fig = plt.figure()
ax = fig.add_subplot(221)
showImageFromArray(img, ax)

ax = fig.add_subplot(222, projection='3d')
showWireframeFromArray(img, ax)


x = np.arange(len(img[0]))[::-1]
y = np.arange(len(img))
X, Y = np.meshgrid(x, y)
ax = fig.add_subplot(223, projection='3d')
ax.set_zlim3d(0, 1000)
ax.plot_surface(X, Y, img, cmap=cm.terrain,
                linewidth=0, antialiased=False, shade=True)




ax = fig.add_subplot(224, projection='3d')
# Plot the surface
ax.contour(X, Y, img, cmap=cm.terrain,
           linewidth=0, antialiased=False, shade=True)
ax.set_zlim3d(0, 1000)

plt.show()
