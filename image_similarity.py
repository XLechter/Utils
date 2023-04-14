import numpy as np
import os
from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp

anchor_file = '/root/autodl-tmp/data/logan_watertight_triplanes_armchair/armchair/1a6f615e8b1b5ae4dbbc9440457e303e.npy'
anchor = np.load(anchor_file)
print(anchor.shape)

target_dir = '/root/autodl-tmp/data/logan_watertight_triplanes_armchair/armlesschair'

most_similar_target = ''
min_similarity = 1000
for root,dirs,files in os.walk(target_dir):
    for f in files:
        target = np.load(os.path.join(root, f))
        sim = mse(anchor, target)
        print(sim)
        if sim < min_similarity:
            min_similarity = sim
            most_similar_target = f

print(most_similar_target, min_similarity)
