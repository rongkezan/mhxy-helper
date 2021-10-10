from PIL import Image
from PIL import ImageFilter

img = Image.open("dataset/raw/raw_crop/front/baf84ca6-28d9-11ec-8c55-acde48001122-4.jpg")
imgF = img.filter(ImageFilter.CONTOUR)
imgF.show()