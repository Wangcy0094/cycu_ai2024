# 匯入需要的模組
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# 使用 sklearn 的 make_moons 函數生成月亮形數據集
# make_moons 函數會返回兩個值，我們只需要第一個（數據集），所以使用 _ 忽略第二個返回值（標籤）
X_moons, _ = make_moons(n_samples=1000, noise=0.1)

# 使用 plt.scatter 繪製散點圖，X_moons[:, 0] 是 x 軸的數據，X_moons[:, 1] 是 y 軸的數據
plt.scatter(X_moons[:, 0], X_moons[:, 1])

# 顯示圖表
plt.show()