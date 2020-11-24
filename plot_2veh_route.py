import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import json
import os
path = os.path.abspath('data')
filename = input("输入文件名:")
filename = os.path.join(path, filename)
with open(filename, 'r') as file_to_read:
  for line in file_to_read:
    route = json.loads(line)
    if ("topic" in route and route["topic"] == "/mqtt_backend/route"):
      waypoints = route["message"]["params"]["waypoints"]
      vin = route["message"]["vin"]
      pos_x = []
      pos_y = []
      for point in waypoints:
        pos_x.append(point[0])
        pos_y.append(point[1])
    PosX = np.array(pos_x) # 将数据从list类型转换为array类型。
    PosY = np.array(pos_y)
    plt.figure(1)
    plt.scatter(PosX, PosY, label=vin, c = np.random.rand(3,1))
    plt.legend(loc='best')
    plt.figure(2)
    plt.plot(PosX, PosY, label=vin, c = np.random.rand(3, 1))
    plt.legend(loc='best')
plt.show()
