from re import S
from PIL import Image, ImageOps
import glob
import os

for filename in glob.glob('C:\\temp\Img\*.png'): #:)
    img=Image.open(filename)
    img_with_border = ImageOps.expand(img,border=3,fill='DarkBlue')
    picname = os.path.basename(filename)
    img_with_border.save('C:/temp/Img/bordered_pics/bordered-%s' % picname)
