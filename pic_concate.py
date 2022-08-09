import numpy as np

from PIL import Image

#methods_list = ['Input','GT','Cascaded','ECG','GRNet','GSA','PCN','NSFA']
methods_list = ['Input','PCN','Cascaded','GRNet','NSFA','GSA','GT']
#methods_list = ['Input','GSA','GT']

for i in [21]:
    img = None
    for method_name in methods_list:
        file_path = 'G:\\shapenet_final\\' + str(i) + '_' + method_name + '.png'
        img_tmp = np.array(Image.open(file_path))
        if img is None:
            img = img_tmp
        else:
            img = np.concatenate((img, img_tmp), axis=1)  # 横向拼接
        img_out = Image.fromarray(img)
        img_out.save('G:\\shapenet_final_all\\'+str(i)+'.png')
