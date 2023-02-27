# 导入必要的模块
import sympy as sp

# 定义符号变量
t = sp.symbols('t')
y = sp.Function('y')(t)

# 定义微分方程
eq = sp.Eq(y.diff(t), -2*y + sp.sin(t))

# 解微分方程
sol = sp.dsolve(eq, y)

# 打印解析表达式
print("Solution:")
print(sol.rhs)