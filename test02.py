import matplotlib.pyplot as plt
import numpy as np
# 保证图片在浏览器内正常显示
#matplotlib inline

# 10个点
N = 10
x1 = np.random.rand(N)
y1 = np.random.rand(N)
x2 = np.random.rand(N)
y2 = np.random.rand(N)
plt.scatter(x1, y1, marker='o', label="circle")
plt.scatter(x2, y2, marker='^', label="triangle")
plt.legend(loc='best')
plt.show()
