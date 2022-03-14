import sys
tp = sys.argv[1]
print(tp)
import datetime
import time
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

####add function path###################
#import os
#import io
#import sys
#tp         = sys.agrv[0]
#reload(sys)
#sys.setdefaultencoding('utf-8')
sys.path.append('E:/lib/py_lib/func')
sys.path.append('E:/lib/py_lib/img_data')

#####import function###################
import date_gen

arg_lst    = ['win','plt','nowin']

if tp not in arg_lst:
    print('input arg error, PLS input either %s, %s or %s'%(arg_lst[0],arg_lst[1],arg_lst[2]))

#####date operation#####################
date_st     = '2020-10-10'
date_lst    = date_gen.create_assist_date(date_st)
datenow     = datetime.datetime.now()


#####read image#########################
img         = cv2.imread('E:/lib/py_lib/img_data/cup.jpg',flags = -1)
# flags = -1 8位深度，原通道
# flags =  0 8位深度， 1通道
# flags =  1 8位深度， 3通道
# flags =  2  原深度， 1通道
# flags =  3  原深度， 3通道
# flags =  4 8位深度， 3通道

print('Current time is %s \nThe image size is %s'%(datenow,np.shape(img)))

##########reshape image########################
img_shape              = np.shape(img)
img_chan_swap          = np.zeros((img_shape[0],img_shape[1],img_shape[2]),np.uint8)
img_chan_swap[:,:,0]   = img[:,:,2]
img_chan_swap[:,:,1]   = img[:,:,1]
img_chan_swap[:,:,2]   = img[:,:,0]
img                    = img_chan_swap

reshp_w                = int(img_shape[0]*1.2)
reshp_h                = int(img_shape[1]/img_shape[0]*reshp_w)

reshp_img   = np.zeros((reshp_w,reshp_h,img_shape[2]),np.uint8)
print('the reshape image size is %s'%(str(np.shape(reshp_img))))

reshp_img[0:img_shape[0],\
          0:img_shape[1],\
          :]\
          = img

reshp_img[  img_shape[0]:  ,\
          0:img_shape[1]   ,\
          0]\
          = 255

reshp_img[0:img_shape[0]   ,\
            img_shape[1]:  ,\
          1]\
          = 255

reshp_img[  img_shape[0]:  ,\
            img_shape[1]:  ,\
          2]\
          = 255


#######threshold##############################
th       = 127
ret, img_th1 = cv2.threshold(img,th,255,cv2.THRESH_BINARY    ) #if pix > th: gray ==0     else: gray = max     
ret, img_th2 = cv2.threshold(img,th,255,cv2.THRESH_BINARY_INV) #if pix > th: gray ==max   else: gray = 0     
ret, img_th3 = cv2.threshold(img,th,255,cv2.THRESH_TRUNC     ) #if pix > th: gray ==th    else: gray = org v     
ret, img_th4 = cv2.threshold(img,th,255,cv2.THRESH_TOZERO    ) #if pix > th: gray ==org v else: gray = 0     
ret, img_th5 = cv2.threshold(img,th,255,cv2.THRESH_TOZERO_INV) #if pix > th: gray ==0     else: gray = org v     

th_titles = ['Orig_img  ',   \
             'Binary    ',   \
             'Binary_inv',   \
             'Trunc     ',   \
             'Tozero    ',   \
             'Tozero_inv'    \
            ]

th_images = [ img        ,   \
              img_th1    ,   \
              img_th2    ,   \
              img_th3    ,   \
              img_th4    ,   \
              img_th5        \
              ]
#################filter##############################
flt_n           = 5 # filter map size
gaus_sigma      = 1 # sigma of gauss forma
sigma_colr      = 5
sigma_spce      = 5

img_blur        = cv2.blur(img,(flt_n,flt_n))
img_boxfilter   = cv2.boxFilter(img,-1,(flt_n,flt_n),normalize=False)
img_gauss       = cv2.GaussianBlur(img,(flt_n,flt_n),gaus_sigma)
img_medianblur  = cv2.medianBlur(img,flt_n)
img_bilateralF  = cv2.bilateralFilter(img,flt_n,sigma_colr,sigma_spce)

ft_titles       = ['Orig_img'       , \
                   'blur       '    , \
                   'boxfilter  '    , \
                   'gauss      '    , \
                   'medianblur '    , \
                   'bilateralF '      \
                   ]

ft_images       = [img              , \
                   img_blur         , \
                   img_boxfilter    , \
                   img_gauss        , \
                   img_medianblur   , \
                   img_bilateralF     \
                   ]

##########erode and dilation##################################
ftr_map3x3  = np.ones((3,3),np.uint8)
ftr_map5x5  = np.ones((5,5),np.uint8)
er_img3x3   = cv2.erode(img,ftr_map3x3,iterations=1)
er_img5x5   = cv2.erode(img,ftr_map5x5,iterations=1)
dl_img3x3   = cv2.dilate(img,ftr_map3x3,iterations=1)
dl_img5x5   = cv2.dilate(img,ftr_map5x5,iterations=1)
ed_img3x3   = cv2.dilate(er_img3x3,ftr_map3x3,iterations=1)
ed_img5x5   = cv2.dilate(er_img5x5,ftr_map5x5,iterations=1)

ed_titles   = [ 'er_img3x3',     \
                'er_img5x5',     \
                'dl_img3x3',     \
                'dl_img5x5',     \
                'ed_img3x3',     \
                'ed_img5x5'      \
                ]

ed_images   = [ er_img3x3,     \
                er_img5x5,     \
                dl_img3x3,     \
                dl_img5x5,     \
                ed_img3x3,     \
                ed_img5x5      \
                ]


##########erode and dilation##################################
ftr_map3x3  = np.ones((3,3),np.uint8)
ftr_map5x5  = np.ones((5,5),np.uint8)
cny_img5x10 = cv2.Canny(img, 50,100)
cny_img10x15= cv2.Canny(img,100,150)
cny_img15x20= cv2.Canny(img,150,200)
cny_img5x15 = cv2.Canny(img, 50,150)
cny_img5x20 = cv2.Canny(img, 50,200)

cny_titles   = ['img'         ,  \
                'cny_img5x10 ',  \
                'cny_img10x15',  \
                'cny_img15x20',  \
                'cny_img5x15 ',  \
                'cny_img5x20 '   \
                ]

cny_images   = [ img,     \
                 cny_img5x10 , \
                 cny_img10x15, \
                 cny_img15x20, \
                 cny_img5x15 , \
                 cny_img5x20   \
                ]


#########output image##########################
winName  = 'img_cup'
win_img  = img
win_reshp_img = reshp_img
if tp == arg_lst[0]:
    #open.window
    cv2.namedWindow(winName,cv2.WINDOW_NORMAL)
    cv2.imshow(winName,win_img)
    cv2.imshow(winName,win_reshp_img)

    k    = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k ==ord('s'):
        cv2.imwrite('E:/lib/py_lib/img_data/saved/cup.jpg')
elif tp == arg_lst[1]:
    fig1 = plt.figure('cv_threshold')
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(th_images[i],'gray')
        plt.title(th_titles[i])
        plt.xticks([]),plt.yticks([])

    fig2 = plt.figure('cv_filter   ')
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(ft_images[i],'gray')
        plt.title(ft_titles[i])
        plt.xticks([]),plt.yticks([])

    fig3 = plt.figure('cv_erode_dilation   ')
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(ed_images[i],'gray')
        plt.title(ed_titles[i])
        plt.xticks([]),plt.yticks([])

    fig4 = plt.figure('cv_Canny   ')
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(cny_images[i],'gray')
        plt.title(cny_titles[i])
        plt.xticks([]),plt.yticks([])


plt.show()



