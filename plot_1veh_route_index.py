import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import json
import os
path = os.path.abspath('data')
filename = input("输入文件名:")
filename = os.path.join(path, filename)
i = 0
with open(filename, 'r') as file_to_read:
  for line in file_to_read:
    i += 1
    route = json.loads(line)
    if ("topic" in route and route["topic"] == "/mqtt_backend/route"):
      waypoints = route["message"]["params"]["waypoints"]
      vin = route["message"]["vin"]
      j = -1
      plt.figure(i)
      for point in waypoints:
        j += 1
        # if (point[5] & 1) :
        #   plt.scatter(point[0], point[1], c = np.random.rand(3,1))
        #   plt.text(point[0], point[1], str(j) + 's')
        # if (point[5] & 2) :
        #   plt.scatter(point[0], point[1], c = np.random.rand(3,1))
        #   plt.text(point[0],point[1], str(j) + 'e')
        plt.scatter(point[0], point[1], c = np.random.rand(3,1))
        if (j % 20 == 0) :
          plt.text(point[0], point[1], str(j))
        #plt.pause(0.01)
    plt.title(vin,loc='center')
    jpgname = 'figure/' + vin + '_route.jpg'
    #plt.savefig(jpgname,dpi=600,format='jpg')
plt.show()
