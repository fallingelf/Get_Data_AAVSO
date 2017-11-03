#coding(utf-8)
import re
import time
import string
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from scipy.optimize import curve_fit
import math


# 从文件中读取数据
def getdata():
    datafile=open('AMHer_Vis.txt','r')
    AMHer_Vis=datafile.readlines()
    datafile.close()
    i=0
    HJD=[]
    Vis=[]
    hjd=re.findall(re.compile(r'[AM HER|AM her],\s([\S]*),'),str(AMHer_Vis))          #数据匹配进行目标选择
    vis=re.findall(re.compile(r'(\S+), Vis.'),str(AMHer_Vis))
    if len(hjd)==len(vis):
        for elem in hjd:
            HJD.append(float(hjd[i]))
            Vis.append(float(vis[i]))
            i+=1
    else:
        while 1:
            print('Error!')
            time.sleep(10)
    HJD.reverse()
    Vis.reverse()
    return(HJD,Vis)

#定义y轴倒序显示函数
def invplot(x,y,linename,patter):
    plt.plot(x,y,patter)
    plt.gca().invert_yaxis()                    #y轴倒序
    plt.plot(x,y,label=str(linename))
    plt.legend()
    return

#定义平滑方式
def soomth_data(x,y,scale,order):
    x=np.array(x)
    y=np.array(y)
    xnew = np.linspace(x.min(),x.max(),len(x)*scale)
    f = interpolate.interp1d(x,y,kind=order)                            #插值函数
    #f = interpolate.pchip(x,y)
    #f = interpolate.UnivariateSpline(x,y,s=methods)
    ynew = f(xnew)
    return(xnew,ynew)

def Low_pass(data,thrud):
   #data=data*

    return


if __name__ == '__main__':
    [HJD,Vis]=getdata()
    HJD=np.array(HJD)-np.array(HJD).min()     #设为0起点
    order=1
    scale=5
    [HJD_smooth, Vis_smooth]=soomth_data(HJD,Vis,scale,order)     #生成等间隔数据
    plt.figure(1)
    plt.subplot(211)
    invplot(HJD,Vis,'Vis_obs','b*')
    invplot(HJD_smooth,Vis_smooth,'Vis_smooth','r-')
    frq=1/len(HJD_smooth)
    spectro=np.fft.fft(Vis_smooth-Vis_smooth.mean())
    plt.subplot(212)
    power=abs(spectro)
    plt.plot(power)
    plt.show()