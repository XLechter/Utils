from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import torch
import numpy as np
import os
import sys
sys.path.append(os.path.abspath('..'))
import tqdm
#from utils.io import read_txt_xyz
from PIL import Image

import open3d as o3d
import glob

def draw_any_set(pcd_list, output_dir, layout=None,apply_ax_limit=False,ax_limit=0.5,size=1,colors=None,axis_off=True,format='.png',figuresize=None,wspace=None,hspace=None,set_title=True,show=False):
    """
    flexibly draw a list of point clouds 
    """
    # if not os.path.isdir(output_dir):
    #     os.mkdir(output_dir)
    
    ax_min = 0
    ax_max = 0
    pcd_np_list = []
    for pcd in pcd_list:
        # if isinstance(pcd,np.ndarray):
        #     pcd = torch.from_numpy(pcd)
        # if pcd.shape[0] == 1:
        #     pcd.squeeze_(0)
        # pcd = pcd.detach().cpu().numpy()
        pcd_np_list.append(pcd)
        ax_min = min(ax_min, np.min(pcd))
        ax_max = max(ax_max, np.max(pcd))
    # in case the generated points has a larger range
    # ax_limit = min(max(abs(ax_min),ax_max) * 1.05, 0.5)  

    if layout == None:
        row = 1
        col = len(pcd_np_list)
        fig = plt.figure(figsize=(len(pcd_list)*4, 4))
    else:
        row, col = layout
    if figuresize is None:
        fig = plt.figure(figsize=(col*4, row*4))
    else:
        fig = plt.figure(figsize=figuresize)

    for i in range(len(pcd_np_list)):
        pcd = pcd_np_list[i]
        ax = fig.add_subplot(row,col,i+1,projection='3d')
        if colors is None:
            ax.scatter(pcd[:,0],pcd[:,2],pcd[:,1],s=size)
        else:
            ax.scatter(pcd[:,0],pcd[:,2],pcd[:,1],s=size,color=colors)
        if apply_ax_limit:
            ax.set_xlim([-ax_limit,ax_limit])
            ax.set_ylim([-ax_limit,ax_limit])
            ax.set_zlim([-ax_limit,ax_limit ])
        # if set_title:
            #ax.set_title(flag_list[i])
        if axis_off:
            plt.axis('off')
        
    if wspace is not None or hspace is not None:
        plt.subplots_adjust(wspace=wspace,hspace=hspace)

    if show:
        plt.show()
    else:
        plt.show()
        output_f = output_dir
        plt.savefig(output_f)
        plt.clf()
        plt.cla()
        plt.close(fig)

def rotate_point_cloud(points, transformation_mat):

    new_points = np.dot(transformation_mat, points.T).T

    return new_points

def rotate_point_cloud_by_axis_angle(points, axis, angle_deg):

    """ angle = math.radians(angle_deg)
    rot_m = pymesh.Quaternion.fromAxisAngle(axis, angle)
    rot_m = rot_m.to_matrix() """
    rot_m = np.asarray([[0,0,1],[0,1,0],[-1,0,0]])

    new_points = rotate_point_cloud(points, rot_m)

    rot_m = np.asarray([[-1,0,0],[0,1,0],[0,0,1]])

    new_points = rotate_point_cloud(new_points, rot_m)

    return new_points

if __name__ == '__main__':

    outdir = '/root/autodl-tmp/overview_vis'
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    path = '/root/autodl-tmp/PVD/output/overview/2023-03-06-22-26-19/syn'


    f_lidar = glob.glob(os.path.join(path, '*.ply'))

    # path_mpc = '/root/Multimodal-Shape-Completion/proj_log/mpc-3depn-table/gan/results_crn/ckpt-500-n150-z10'
    # all_shape_dir_mpc = [os.path.join(path_mpc, str(i)) for i in range(len(shape_names))]

    #for i in tqdm(range(len(shape_names)), total=len(shape_names), desc='Ploting.'):
    pcd_list = []
    for i in range(len(f_lidar)):
        #pc_path = os.path.join(cur_path, "fake-z{}.ply".format(k))
        pc = np.array(o3d.io.read_point_cloud(f_lidar[i]).points)
        pcd_list.append(pc)

    draw_any_set(pcd_list, 'vis_pink.png', colors='#F08080') ##FFC0CB

