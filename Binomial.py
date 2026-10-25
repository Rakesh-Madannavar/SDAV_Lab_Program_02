import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n, p = 20, 0.35
binom = stats.binom(n, p)
x = np.arange(0, n+1)
print(f' Mean = {binom.mean():.4f} (Theory: np={n*p})')
binom.var()
binom.moment(2)
binom.stats("s")
binom.cdf(10)
binom.pmf(7)
plt.figure(figsize=(7, 5))
plt.bar(x, binom.pmf(x), color='steelblue',
        edgecolor='black', alpha=0.8)

plt.axvline(binom.mean(), color='red', linestyle='--',
            label=f'Mean = {binom.mean():.1f}')

plt.title(f'Binomial PMF (n={n}, p={p})')
plt.xlabel('Number of Successes (x)')
plt.ylabel('Probability')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
