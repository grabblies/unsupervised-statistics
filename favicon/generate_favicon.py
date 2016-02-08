from scipy import misc
from PIL import Image 
import numpy as np
im_array = misc.imread("U.png",flatten=True)

X = []
Y = []

for i in range(im_array.shape[0]):
    for j in range(im_array.shape[1]):
        if im_array[i][j]<10:
            X.append(i)
            Y.append(j)
X.reverse()
X = np.array(X)
Y = np.array(Y)
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("white")
pal = sns.light_palette("green", as_cmap = True)
#pal = sns.dark_palette("palegreen", as_cmap=True)
with sns.axes_style(None):
    ax = sns.kdeplot(Y, X, cmap = pal, shade=True, shade_lowest=False)
    sns.despine(left=True,bottom=True,trim=True)
plt.show()
