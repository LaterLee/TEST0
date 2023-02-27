# 导入必要的模块
print('Hello,World!')
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定义微分方程
def derivative(y, t):
    return -2 * y + np.sin(t)

# 定义初始条件
y0 = 1.0
t = np.linspace(0, 10, 101)

# 解微分方程
sol = odeint(derivative, y0, t)

# 绘制结果
plt.plot(t, sol)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
# 输出解
print("Solution:")
for i in range(len(t)):
    print("t = {:.2f}, y = {:.4f}".format(t[i], sol[i][0]))

