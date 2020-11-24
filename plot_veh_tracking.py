import numpy as np
import matplotlib.pyplot as plt
import json
import os
file_name = input("please input file name:")
path = os.path.abspath('data')
file_name = os.path.join(path, file_name)
begin_time, end_time = input("please input begin and end timestamp, space split:").split()
vehicle_name = input("please input vehicle name:")
broker_id = input("please_input broler id:")
topic = broker_id + '/tracking'
print("find topic:%s, vehicle:%s, in %s~%s." %(topic, vehicle_name, begin_time, end_time))
with open(file_name, 'r') as f :
    for line in f :
        data = json.loads(line)
        if (data["timestamp"] >= begin_time and data["timestamp"] < end_time
            and data["topic"] == topic) :
            print("***")
            message = data["message"]
            if (message["vin"] == vehicle_name) :
                print("...")
                loc = message["params"]["loc"]
                plt.scatter(loc["lon"], loc["lat"])
                plt.pause(0.01)
        if (data["timestamp"] > end_time) :
            break
print("plot finished")
plt.show()