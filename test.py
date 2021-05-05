import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import tensorflow as ts


img_H = 100
img_W = 100

savedEdges = np.zeros(shape=[4,img_H,img_W])

img = cv.imread("Images/Charmander/Charmander.png", 0)
rsImg = cv.resize(img, (img_H, img_W))
edges = cv.Canny(rsImg, 75, 200)

img1 = cv.imread("Images/Charmander/Charmander1.png", 0)
rsImg = cv.resize(img1, (img_H, img_W))
edges1 = cv.Canny(rsImg, 75, 200)

img2 = cv.imread("Images/Charmander/Charmander2.png", 0)
rsImg = cv.resize(img2, (img_H, img_W))
edges2 = cv.Canny(rsImg, 75, 200)

img3 = cv.imread("Images/Charmander/Charmander3.png", 0)
rsImg = cv.resize(img3, (img_H, img_W))
edges3 = cv.Canny(rsImg, 75, 200)

savedEdges[0] = edges
savedEdges[1] = edges1
savedEdges[2] = edges2
savedEdges[3] = edges3

print(savedEdges)


plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
plt.subplot(121), plt.imshow(img1, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges1, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
plt.subplot(121), plt.imshow(img2, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges2, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
plt.subplot(121), plt.imshow(img3, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges3, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()





























#
#
# num_of_images = 4
# num_of_pixels = 3
# RGB = 3
# X = np.zeros((num_of_images, num_of_pixels, RGB))
#
# print(X)
# print("")
# print(images )
#
# print("")
# for i in range(num_of_images):
#     for j in range(num_of_pixels):
#         X[i, j] = X[i, j]+images[j]
#
# print(X)
#
#
# """
# for i in range(3):
#     X = np.append(X, [images2[i]], axis=0)
#
# print(X)
# """