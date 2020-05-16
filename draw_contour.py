# https://terrain.party/

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image,ImageFilter
import numpy as np
import os


PATH_TO_HEIGTHMAP = os.path.join("heightmap")




file="idf"
path = os.path.join(PATH_TO_HEIGTHMAP,"{}.png".format(file))

# Pillow does not support 16 bit png
img = Image.open(path)
img_float = Image.fromarray(np.divide(np.array(img), 2**8-1))
original_image = img_float.convert('L')


B=20
blurred_image = original_image.filter(ImageFilter.GaussianBlur(B)).filter(ImageFilter.SHARPEN)




img = np.array(blurred_image)

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

os.mkdir(file)

plt.clf()
for h in levels :
    fig= plt.figure(num=None, figsize=(11, 11), dpi=120, facecolor='w', edgecolor='k')
    plt.contour(X, Y, img,[h],linewidths=0.6, colors="k", origin="lower")
    plt.axis("off")
    p = os.path.join(file,"{}_{:04.2f}.png".format(file,h) )
    plt.savefig(p, bbox_inches='tight')


