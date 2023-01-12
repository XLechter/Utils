import os
import numpy as np
from PIL import Image

images_dir = "/home/qimin/Projects/implicit-latent-diffusion/results/Diffusion/chair/trajectory/cbc47018135fc1b1462977c6d3c24550"
save_dir = "/home/qimin/Downloads/gif"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
all_images = sorted([i for i in os.listdir(images_dir) if i.endswith('.png')])

for im in all_images:
    image = Image.open(os.path.join(images_dir, im))
    new_image = Image.new("RGBA", image.size, "WHITE")
    new_image.paste(image, mask=image)
    new_image = np.array(new_image)
    new_image[:,:,-1] = np.ones(new_image.shape[:2]) * 255
    new_image = Image.fromarray(new_image)
    new_image.save(os.path.join(save_dir, im))
