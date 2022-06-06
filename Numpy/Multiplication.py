import numpy as ny
# A= ny.array([[1,1],[0,1]])
# B=ny.array([[2,0],[3,4]])
#
# print("element wise multiplication")
# print(A*B)
#
# print(("matrix multiplcation"))
# print(A@B)
# for two dimensional arrays, we csn do sam thing for each row or column. with shape 3*5
# b=ny.arange(1,16,1).reshape(3,5)
# print(b)

from PIL import Image
from IPython.display import display

im = Image.open("demo.tiff")
display(im)

# image as array PIL IMAGE TO  numpy array

array = ny.array(im)
mask = ny.full(array.shape, 255)

modified = array-mask
modified = modified*-1
modified = modified.astype(ny.uint8)
display(Image.fromarray(modified))


reshaped=ny.reshape(modified,(100,400))
print(reshaped)
display(Image.fromarray(reshaped))