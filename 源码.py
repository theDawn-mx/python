from turtle import *
from math import *
import time
def setup():                 #定义初始化数据函数
    title("抽象几何图像")     #作品名称
    bgcolor("white")         #背景颜色
    ht()                     #隐藏海龟图标
    speed(0)                 #设置速度
    penup()                  
    setx(-130)               #设置海龟初始横坐标
    sety(-100)               #设置海龟初始纵坐标
    pendown()                
def draw_first(n):           #定义绘制第一个个图形的函数
    for i in range(0, n):    #n边形循环n次
        fd(Len)              #绘制长为Len的边
        left(360/n)          #绘制n边形的内角
def draw(len,n, len1):       #定义循环函数
    penup()                  
    x=[]                     #定义一个空列表，用于保存下一个多边形顶点的位置
    for i in range (0,n-1):  #在已绘制的多边形上寻找下一个多边形的顶点坐标，重复n-1次
        fd(len1)             #向前走len1的长度，到达下一个多边形顶点的位置
        x.append(position()) #保存这个顶点位置的坐标
        fd(len - len1)       #继续向前走剩下的长度
        left(360/n)          #旋转一个内角
    fd(len1)                 #向前走len1的距离，到达该多边形最后一个顶点的位置
    x.append(position())     #保存这个顶点的位置坐标
    pendown()              
    for i in range(0,n):     #开始绘制下一个多边形
        goto(x[i])           #将获取到的位置坐标依次相连
if __name__ == '__main__':
    tracer(False)            #关闭追踪器
    for i in range(1,14):    #绘制动画，以间隔0.1秒的速度播放13个不同的静态图形
        clear()              #清除屏幕上的图形
        setheading(0)        #将海龟设置为初始方向
        setup()              #初始化数据
        n=3                  #多边形的边数，可以修改不同的边数
        Len=900/n            #多边形的边长，让边长和边数的乘积是一个定值，确保屏幕能画下
        Len1=i               #当前多边形的顶点到下一个多边形对应顶点的距离，随i逐渐变大，以达到动画的效果
        draw_first(n)        #绘制第一个多边形
        for i in range(0,14):#绘制剩下的多边形，重复14次
            if i%2==0:       #填充黑白相间的颜色
                color("black")
            else:
                color("white")
            begin_fill()     #开始填充颜色
            draw(Len,n, Len1)#绘制静态图形
            end_fill()       #结束填充颜色
            Len = sqrt(pow(Len-Len1, 2) - 2 * (Len-Len1) * Len1*cos(radians((n-2)*180/n)) + pow(Len1, 2)) #更新多边形的边长
            angle = degrees(asin(sin(radians((n-2)*180/n)) * Len1 / Len))       #绘制完一次后需要调整角度，以绘制下一个多边形
            #Len1 = Len1 - 2   #更新下一个多边形的顶点距这个多边形的顶点之间的距离
            left(angle)        #调整角度
        update()               #更新画好的静态图
        time.sleep(0.1)        #每0.1s呈现一张静态图
    exitonclick()              #点击后才退出



