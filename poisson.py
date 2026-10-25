import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

for lam in [1, 3, 5, 10]:
    d = stats.poisson(lam)
    sim = np.random.poisson(lam, 5000)
    d.mean()
    sim = np.random.poisson(lam, 5000)
    sim.mean()
for lam in [1, 3, 5, 10]:
    d = stats.poisson(lam)
    sim = np.random.poisson(lam, 5000)
    print(f'Poisson(λ={lam}): Th.Mean={d.mean()}, Sim.Mean={sim.mean():.3f}')
    plt.figure(figsize=(7, 5))

x_p = np.arange(0, 20)

for lam in [1, 3, 5, 10]:
    plt.plot(x_p, stats.poisson.pmf(x_p, lam),
             marker='o', markersize=4, label=f'λ = {lam}')

plt.title('Poisson PMF — Effect of λ')
plt.xlabel('Number of Events (x)')
plt.ylabel('Probability')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()