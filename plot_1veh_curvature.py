import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import json
import os
path = os.path.abspath('data')
filename = input("输入文件名:")
filename = os.path.join(path, filename)
i = 0
write_file = open("data/road_junction_info.txt", 'w')

with open(filename, 'r') as file_to_read:
  for line in file_to_read:
    i += 1
    route = json.loads(line)
    if ("topic" in route and route["topic"] == "/mqtt_backend/route"):
      waypoints = route["message"]["params"]["waypoints"]
      vin = route["message"]["vin"]
      j = -1
      plt.figure(i)
      max_curvature = 0.0
      min_curvature = 0.0
      for point in waypoints:
        j += 1
        #plt.subplot(2,1,1)
        if (point[3] > 0.03) :
          plt.scatter(point[0], point[1], c = np.random.rand(3,1))
        # if (j % 10 == 0) :
          plt.text(point[0], point[1], str(j))
        # plt.subplot(2,1,2)
        # if (point[3] > 0.03) :
        #   plt.scatter(point[0], point[3], c = np.random.rand(3,1))
        # # if (j % 10 == 0) :
        #   plt.text(point[0], point[3], str(j))
        if (point[3] > max_curvature) :
          max_curvature = point[3]
        if (point[3] < min_curvature) :
          min_curvature = point[3]
        # if (point[5] & 1) :
        #   write_file.write(vin + 'junction start at:' + str(j) + '  ')
        # elif (point[5] & 2) :
        #   write_file.write('end at:' + str(j)+ '\n')
        #if (point[5] & 8) :
         # write_file.write(vin + 'dual at:' + str(j)+ '\n')
        #plt.pause(0.01)
      # plt.subplot(2,1,2)
      print(vin, min_curvature, max_curvature)
      # plt.ylim(min_curvature, max_curvature)
    plt.title(vin,loc='center')
    # jpgname = 'figure/' + vin + '_curvature.jpg'
    # plt.savefig(jpgname,dpi=600,format='jpg')
write_file.close
plt.show()
