#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import SimpleITK as sitk
import os

input_dir = '/input/'
path_img = os.path.join(input_dir,'{}_T2.nii.gz')
path_pred = '/output/{}.nii.gz'

list_case = [k.split('_T2')[0] for k in os.listdir(input_dir)]

for case in list_case:
    t2_img = sitk.ReadImage(path_img.format(case))

    ##
    # your logic here. Below we do binary thresholding as a demo
    ##

    # using SimpleITK to do binary thresholding between 100 - 10000
    intrameatal_pred = sitk.BinaryThreshold(t2_img, lowerThreshold=400, upperThreshold=500)
    extrameatal_pred = sitk.BinaryThreshold(t2_img, lowerThreshold=600, upperThreshold=700)
    cochlea_pred = sitk.BinaryThreshold(t2_img, lowerThreshold=900, upperThreshold=1100)

    result = extrameatal_pred + 2*intrameatal_pred + 3*cochlea_pred

    # save the segmentation mask
    sitk.WriteImage(result, path_pred.format(case))



