from PE_4_3_24.PhotoEnhance.models.FBCNN.models.network_fbcnn import FBCNN as net
import sys
import pathlib

if str(pathlib.Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(pathlib.Path(__file__).parent))

import os.path
import logging
import numpy as np
from datetime import datetime
from collections import OrderedDict
import torch
import cv2
from PE_4_3_24.PhotoEnhance.models.FBCNN.utils import utils_image as util
import requests
from PIL import Image


# class RunFBCNN:
#     def __init__(self) -> None:
#         pass
#     def predict(self, input_images, QF_control_value = None):
#         call_dir = os.getcwd()
#         work_dir = os.path.dirname(__file__)

#         # os.chdir(work_dir)

#         n_channels = 3
#         model_name = 'fbcnn_color.pth'
#         nc = [64,128,256,512]
#         nb = 4

#         model_pool = 'model_zoo'  # fixed
#         model_path = 'PE_4_3_24/PhotoEnhance/models/FBCNN/model_zoo/fbcnn_color.pth'
        
#         print(f'loading model from {model_path}')  
        
#         device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#         model = net(in_nc=n_channels, out_nc=n_channels, nc=nc, nb=nb, act_mode='R')
#         model.load_state_dict(torch.load(model_path), strict=True)
#         model.eval()
#         for k, v in model.named_parameters():
#             v.requires_grad = False
#         model = model.to(device)

#         result_images = []
#         for img_pil in input_images:
#             img_L = np.array(img_pil)
        
#             img_L = util.uint2tensor4(img_L)
#             img_L = img_L.to(device)
            
#             if QF_control_value:
#                 qf_input = torch.tensor([[1-QF_control_value/100]]).cuda() if device == torch.device('cuda') else torch.tensor([[1-QF_control_value/100]])
#                 img_E,QF = model(img_L, qf_input)
#                 QF = 1- QF
#                 img_E = util.tensor2single(img_E)
#                 img_E = util.single2uint(img_E)
#                 img = np.squeeze(img_E)
#                 result_images.append(
#                     Image.fromarray(img)
#                 )
#             else:
#                 img_E,QF = model(img_L)
#                 QF = 1- QF
#                 img_E = util.tensor2single(img_E)
#                 img_E = util.single2uint(img_E)
#                 img = np.squeeze(img_E)
#                 result_images.append(
#                     Image.fromarray(img)
#                 )

#         os.chdir(call_dir)
        
#         return result_images
    

from PE_4_3_24.PhotoEnhance.models.FBCNN.RunFBCNN import RunFBCNN

def main():
    artifact_remover = RunFBCNN()

    pil_images = []

    # for file in os.listdir('./testsets/Real'):
    #     pil_images.append(
    #         Image.open(os.path.join('./testsets/Real/', '4.jpg')).convert('RGB')
    #     )

    # pil_images.append(
    #     Image.open('./4.jpg').convert('RGB')
    # )
    pil_images = [Image.open('./4.jpg').convert('RGB')]

    out_images = artifact_remover.predict(pil_images, QF_control_value=5)

    count = 0
    for img in out_images:
        img.save(f'./out_{count}.png')

if __name__ == '__main__':
    main()