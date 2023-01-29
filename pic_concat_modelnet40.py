import numpy as np

from PIL import Image
count = 0

img_all = None
img = None
for i in range(40):
    file_path = '/home/users/wenxiao_zhang/temp/image_' + str(i) + '_epoch6000.png'
    img_tmp = np.array(Image.open(file_path))
    if img is None:
        img = img_tmp
    else:
        img = np.concatenate((img, img_tmp), axis=1)  # 横向拼接

    if i%8 == 7:
        if img_all is None:
            img_all = img
        else:
            img_all = np.concatenate((img_all, img), axis=0)  # 纵向拼接
        img = None

img_out = Image.fromarray(img_all)
img_out.save('modelnet40.png')
