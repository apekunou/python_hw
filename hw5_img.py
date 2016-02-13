import os
path = 'D:\Python_projects\home_pictures'
r_xsize = 0
r_ysize = 0
for dir, subDirs, fileList in os.walk(path):
    for name in fileList:
        full_path = os.path.join(dir, name)
        print(full_path)
        from PIL import Image
        img = Image.open(full_path)
        resized_name = 'resized_' + name
        resized_path = os.path.join(dir, resized_name)
        xsize, ysize = img.size
        i_xsize = int(xsize)
        i_ysize = int(ysize)
        r_xsize = i_xsize/ 2
        r_ysize = i_ysize/2
        r_img = img.resize((r_xsize,r_ysize))
        print(resized_path)
        r_img.save(resized_path)
