# https://terrain.party/

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image,ImageFilter
import numpy as np
import os


PATH_TO_HEIGTHMAP = os.path.join("heightmap")




def visualisation(img):
    plt.clf()
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
    ax.contour(X, Y, img, colors="k", linewidths=0.02,
               antialiased=False, shade=True)
    ax.set_zlim3d(0, 1000)
    plt.show()





from matplotlib.pyplot import figure
figure(num=None, figsize=(11, 11), dpi=120, facecolor='w', edgecolor='k')


file="paris_large"
path = os.path.join(PATH_TO_HEIGTHMAP,"{}.png".format(file))

# Pillow does not support 16 bit png
img = Image.open(path)
img_float = Image.fromarray(np.divide(np.array(img), 2**8-1))
original_image = img_float.convert('L')


B=20
blurred_image = original_image.filter(ImageFilter.GaussianBlur(B)).filter(ImageFilter.SHARPEN)




img = np.array(blurred_image)
visualisation(img)
x = np.arange(len(img[0]))
y = np.arange(len(img))[::-1]
X, Y = np.meshgrid(x, y)
N=15
levels = np.linspace(img.min(),img.max(), N)
cmap = plt.cm.get_cmap('jet')    

plt.clf()
fig= plt.figure(num=None, figsize=(11, 11), dpi=80, facecolor='w', edgecolor='k')
plt.contour(X, Y, img,levels)
plt.legend()
plt.savefig("{}_{}_{}.png".format(file,N, B), bbox_inches='tight')


plt.clf()
for h in levels :
    fig= plt.figure(num=None, figsize=(11, 11), dpi=120, facecolor='w', edgecolor='k')
    plt.contour(X, Y, img,[h],linewidths=0.6, colors="k", origin="lower")
    plt.axis("off")
    plt.savefig("{}_{:04.2f}.png".format(file,h), bbox_inches='tight')


