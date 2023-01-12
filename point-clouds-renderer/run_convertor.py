import os
import matlab.engine

# directory containing all the point clouds
# in .ply format that need to be converted to obj
# each point is converted into a sphere
input_dir = "/home/qimin/Projects/implicit-latent-diffusion/results/Diffusion/chair/denoise/cbc47018135fc1b1462977c6d3c24550"

sphere_size = 0.015
eng = matlab.engine.start_matlab()
eng.convertply2obj(input_dir, sphere_size, nargout=0)
