#import datetime
#import time
#import cv2
#import numpy as np
#import math
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#
####add function path###################
#import os
#import io
import sys
tp         = sys.agrv[0]
#reload(sys)
#sys.setdefaultencoding('utf-8')
sys.path.append('E:/lib/py_lib/func')
sys.path.append('E:/lib/py_lib/img_data')

#####import function###################
import date_gen

arg_lst    = ['win','plt','nowin']

if tp not in arg_lst:
    print('input arg error, PLS input either %S, %s or %s'%(arg_lst[0],arg_lst[1],arg_lst[2]))

#####date operation
date_st     = '2020-10-10'
date_lst    = date_gen.create_assit_date(date_st)
