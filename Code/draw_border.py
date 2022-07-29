from PIL import Image, ImageOps
import glob
import os

# for filename in glob.glob('C:\\temp\Img\*.png'): #:)
#     img=Image.open(filename)
#     img_with_border = ImageOps.expand(img,border=3,fill='DarkBlue')
#     picname = os.path.basename(filename)
#     img_with_border.save('C:/temp/Img/bordered_pics/bordered-%s' % picname)

for filename in glob.glob(r"C:\temp\Img\*.png"):
    img = Image.open(filename)
    border = Image.new(mode="RGB",size=(1,1),color=(0, 255, 255))
    border_thickness = 5
    size = img.size
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if (x<border_thickness or x>img.size[0]-(border_thickness+1)) or (y<border_thickness or y>img.size[1]-(border_thickness+1)):
                img.paste(border,box=(x,y))
    picname = os.path.basename(filename)
    img.save(f'C:/temp/Img/bordered_pics/bordered-{picname}')


