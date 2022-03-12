#!/usr/bin/env python

from skimage import data, draw, io, color
from scipy.ndimage import filters
import numpy as np
from matplotlib import pyplot as plt
import cv2
import scipy.stats as st
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros
import math
import copy


def normalizeRows(M):
    row_sums = M.sum(axis=1)
    return M / row_sums

def gen_gaussian_kernel(k_size, sigma=1):
    sigma=k_size/6
    center = k_size // 2
    g=np.ones((k_size,k_size))/(k_size*k_size)
    x, y = mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    ex_comp=(x*x + y*y)/(2*sigma*sigma)
    g =exp(-ex_comp)/ (2 *pi*sigma*sigma)
#     print(g.sum())
    return g
    

width, height = 500, 500
img = np.round(np.random.rand(height, width) * 255).astype(np.uint8)

def convolve(img):
    r=img.shape[0]
    kernel=gen_gaussian_kernel(r)
#     if (kernel*img).sum()>255:
#         return 255
#     else:
    return (kernel*img).sum()

def pythag(dx,dy):
    r=math.sqrt(dx*dx+dy*dy)
    return r

output=img.copy()
new_image_width,new_image_height=img.shape[0]+40,img.shape[1]+40
result = np.full((new_image_width,new_image_height),(1), dtype=np.uint8)
output=result.copy()
# # # compute center offset
x_center = (new_image_width - img.shape[0]) // 2
y_center = (new_image_height - img.shape[1]) // 2
result[y_center:y_center+img.shape[0],x_center:x_center+img.shape[1]] = img  

midx=result.shape[0]//2
midy=result.shape[1]//2
# cv2.circle(result,(midx,midy),10,(255,0,0),3)
# cv2.circle(result,(20,20),10,(255,0,0),3)
# cv2.circle(result,(result.shape[0]-20,result.shape[1]-20),10,(255,0,0),3)

for x in range(40,result.shape[0]-40):
    for y in range(40,img.shape[1]-40):
         R = pythag(x-midx,y-midy)
         r=int(R//10) 
         if 0<=r<=5:
               r=5 
         patch=result[x-r//2:x+r//2,y-r//2:y+r//2]
         output[x,y]=convolve(patch)
            

new=output[40:450,40:500]
min_pixel = new.min() 
max_pixel = new.max()
new_min = 0
new_max = 255
new_image = (new-min_pixel)*(new_max-new_min)/(max_pixel-min_pixel)+new_min
plt.imshow(new_image)
plt.savefig('const_new')
plt.colorbar()
plt.show()






