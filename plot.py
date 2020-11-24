import numpy as np
import matplotlib.pyplot as plt
from pylab import *
filename = 'route_/e100.w.car12route.txt2' # txt文件和当前脚本在同一目录下，所以不用写具体路径
filename2 = 'route_/e100.w.car14route.txt1'
pos_x = []
pos_y = []
Heading = []
with open(filename, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if not lines:
      break
      pass
    x,y,heading = [float(i) for i in lines.split(',')] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
    pos_x.append(x)  # 添加新读取的数据
    pos_y.append(y)
    Heading.append(heading)
    pass
    PosX = np.array(pos_x) # 将数据从list类型转换为array类型。
    PosY = np.array(pos_y)
    Head = np.array(Heading)
    pass
#plt.plot(PosX, PosY)
figure(1)
#plot(PosX, PosY, color="red", linewidth=1.5, linestyle="--")
scatter(PosX,PosY,linewidths=0.1,marker='*',color='b',label=filename)
#legend(loc='best')
#show()
pos_x.clear()
pos_y.clear()
Heading.clear()
with open(filename2, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if not lines:
      break
      pass
    x,y,heading = [float(i) for i in lines.split(',')] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
    pos_x.append(x)  # 添加新读取的数据
    pos_y.append(y)
    Heading.append(heading)
    pass
    PosX = np.array(pos_x) # 将数据从list类型转换为array类型。
    PosY = np.array(pos_y)
    Head = np.array(Heading)
    pass
figure(1)
#plot(PosX, PosY, color="green", linewidth=1.0, linestyle="-")
scatter(PosX,PosY,linewidths=0.1,marker='o',color='r',label=filename2)
legend(loc='best')
show()
