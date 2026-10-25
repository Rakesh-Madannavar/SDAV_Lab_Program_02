import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


p_geo = 0.3
geo = stats.geom(p_geo)
geo.mean()
geo.pmf(1)
1 - geo.cdf(5)

print(f'Geometric(p={p_geo}):')
print(f'  Mean = 1/p = {geo.mean():.4f}')
print(f'  P(X=1) = {geo.pmf(1):.4f}')
print(f'  P(X>5) = {1 - geo.cdf(5):.4f}')

# Visualization - Geometric PMF
plt.figure(figsize=(7, 5))

x_g = np.arange(1, 20)

plt.bar(x_g, geo.pmf(x_g), color='green',
        edgecolor='black', alpha=0.8)

plt.title(f'Geometric PMF (p={p_geo})')
plt.xlabel('Trial Number (x)')
plt.ylabel('Probability')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()