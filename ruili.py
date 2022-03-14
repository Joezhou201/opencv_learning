import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

xn      = 64
sigma   = 1
x       = np.arange(0,xn);
xin1     = x/4
xin2     = x/4 -10

y1      = xin1/pow(sigma,2)*np.exp(-pow(xin1,2)/2/pow(sigma,2));
y2      = (xin2)/pow(sigma,2)*np.exp(-pow((xin2),2)/2/pow(sigma,2));
y       = y1+y2+1

fig1=plt.figure('fig1')
#plt.plot(x,y,color="blue",linewidth=1.0,linestyle="-")
##柱状图
plt.bar(x[:],y[:],color="red",linewidth=1.0,linestyle="-")
#plt.plot(x,y2,color="#808080",linewidth=3.0,linestyle="--")
#plt.xticks([]),plt.yticks([])
plt.title('Bandwidth Statistics')
plt.show()

