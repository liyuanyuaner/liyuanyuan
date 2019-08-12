
# coding: utf-8

# #1.1五角数

def getPentalNumber(n):   
    num=0
    for i in range(1,n+1):

        f = i * (3 * i- 1) / 2
        print('%8.2f'%f,end=' ')
        num+=1
        if num%10==0:
            print()

def Start():
    
    getPentalNumber(100)
Start()



# 1.2

def sumDigits(n):      
    #2、计算整数各个数的和
    #str 将括号中的内容强制转换为字符串
    str_ = str(n)
    int_ = 0
    for i in str_:
        int_ += int(i)    #int_ = int_ +int(i)
    print(int_)
    
    
sumDigits(345)    
   



#1.3 升序

def displaySortedNumbers(num1,num2,num3):  
    res = [num1,num2,num3]
    res.sort()
    print(res)

displaySortedNumbers(6,5,4)



#4、时间

import time                   

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)



 #5、打印字符

def printChars(ch1, ch2,numberPerLine): 
    # print(ord(ch2))
    # print(ord(ch1))
    num=ord(ch2)-ord(ch1)+1
    num_2=int(numberPerLine)
    # print(num_2)
    num_1=0
    for i in range(ord(ch1),ord(ch2)+1):
        print(chr(i),end=" ")
        num_1+=1
        if num_1%num_2==0:
            print()
def start():
    ch1, ch2,numberPerLine=map(str,input().split(','))
    printChars(ch1, ch2,numberPerLine)

start()



  # 6返回一年的天数

from datetime import date        

lastDate= date(2019,1,15)
firstDate = date(2010,5,31)

delta = lastDate - firstDate
print('There are {} days between {} and {}'.format(delta.days, firstDate, lastDate))




#7、显示角

import math                         
def distance(x1,y1,x2,y2):
    a=(x1-x2)**2
    b=(y1-y2)**2
    c=math.sqrt(a+b)
    print(c)
def start():
    x1,y1,x2,y2=map(float,input().split(','))
    distance(x1,y1,x2,y2)
start()




#8、梅森素数

def Mersenne_prime(P):     
    print('P值    梅森素数（P^2-1）')
    for i in range(1,P+1):
        Number1=2**i-1
        Number2=0
        for j in range(2,Number1):
            if Number1%j==0:
                Number2+=1
        if Number2==0:
            print('%3d %10d'%(i,Number1))
def start():
    P=int(input())
    Mersenne_prime(P)
Start()


# In[ ]:
 #9、财务程序，计算未来投资值。

def futureIn(money,rate,year):   
    for i in range(1,year*12+1):
        money=float(1+rate/100/12)*money
        if i%12==0:
            print('%9d %10.2f'%((i/12),money))

def start():
    money,rate,year=map(int,input().split(','))
    futureIn(money,rate,year)
    
start()


# In[ ]:


def Roll_dice():            #10、掷骰子
    import random
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print('Dice1:%d    Dice2:%d'%(dice1,dice2))
    sum = dice1+dice2
    return sum
def Judge():
    sum=Roll_dice()
    print('点数：%d'%sum)
    a=(2,3,12)
    b=(7,11)
    c=(4,5,6,8,9,10)
    if sum in a:
        print('你输了')
    if sum in b:
        print('你赢了')
    if sum in c:
        Judge1(sum)
def Judge1(sum):
    sum_1=sum
    while True:
        sum=Roll_dice()
        print('点数：%d'%sum)
        if sum==sum_1:
            print('你赢了')
            break
        if sum==7:
            print('你输了')
            break
def start():
    Judge()
start()


# In[ ]:


# 第二次作业第一题 矩形
class juxing(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        print('宽是：%.2f,高是：%.2f'% (width,height))
    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return 2*(self.width+self.height)
if __name__ == "__main__":
    width=float(input('请输入宽：'))
    height=float(input('请输入高：'))
    rs=juxing(width,height)
    print('面积是：%.2f'% rs.getArea())
    print('周长是：%.2f'% rs.getPerimeter())


# In[ ]:


# 第二次作业第四题
class RegularPolygon(object):
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=int(n)
        self.__side=float(side)
        self.__x=float(x)
        self.__y=float(y)
    def getPerimetetr(self):
        print('周长是:%.4f'% (self.__n*self.__side )) 
    def getArea(self):
        import math
        self.s=self.__n*(self.__side**2)/4*math.tan(math.pi/self.__n)
        print('面积%.4f'% self.s)
if __name__ == "__main__":
    n=int(input('请输入边数：'))
    side=float(input('请输入边长：'))
    x=float(input('请输入x轴坐标：'))
    y=float(input('请输入y轴坐标：'))
    r=RegularPolygon(n,side,x,y)
    r.getPerimetetr()
    r.getArea()

