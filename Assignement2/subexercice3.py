# Assignement 2 - Subexercice 3

import numpy as np
import matplotlib.pyplot as plt

def N_(x,mu,sigma):
  return 1/(np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*((x-mu)/sigma)**2)

def p(x):
  return 0.3 * N_(x, 2.0, 1.0) + 0.4 * N_(x, 5.0, 2.0) + 0.3 * N_(x, 9.0, 1.0)

def SIR(k, Q):
  # Sampling
  if Q == 1:
    xi = np.random.uniform(0,15, size=k) # q(x) being a uniform distribution on the interval [0 : 15].
  else:
    xi = np.random.normal(4,5, size=k) # q(x) being a normal distribution with mean equal to 5 and variance equal to 4.

  # Importance
  p_xi = p(xi)
  if Q == 1:
    q_xi = 1/15
  else:
    q_xi = N_(xi,5,4)
  w = p_xi / q_xi

  # Normalisation
  w = w/np.sum(w)

  # Remove particles with weight w[i] = 0
  xi = xi[np.nonzero(w)]
  w = w[np.nonzero(w)]

  # Cumulative Distribution
  N = w.shape[0]
  H = np.cumsum(w)

  # Resampling
  x = np.zeros(N)
  for i in range(N):
    z = np.random.uniform(0,1)
    for j in range(N):
      if z < H[j]:
        x[i] = xi[j]
        break
  return x

def resample_and_plot(Q):
  x20 = SIR(20, Q)
  x100 = SIR(100, Q)
  x1000 = SIR(1000, Q)
  print(x20)

  # Histogram as density
  plt.hist(x20, density=True, alpha=0.4, label=f"SIR k={20}")
  plt.hist(x100, density=True, alpha=0.4, label=f"SIR k={100}")
  plt.hist(x1000, density=True, alpha=0.4, label=f"SIR k={1000}")

  # Plot target distribution
  X = np.linspace(0, 15, 500)
  plt.plot(X, p(X), "r-", label="Target p(x)")

  plt.title(f"Sampling Importance Resampling")
  plt.xlabel("x")
  plt.ylabel("Probability density")
  plt.legend()
  plt.show()

def main():
  # Question 1

  resample_and_plot(1)

  # As expected, the larger k is, the more the histogram of samples fits with p(x).
  # However, even for k=20, we can see the shape of the wanted pose distribution, with a bit of noise.

  # The only issue I can see is that with not much samples, many of them won't be useful (with low weights), and we tend to have a lot of identical samples around peaks after resampling.
  # Therefore there are some high density areas with not any samples, and we need a lot of samples (1000 here) to compensate for this issue.


  # Question 2

  # As before, the larger k is, the more the histogram of samples fits with p(x).
  # However, unlike with the uniform distribution, the histogram of samples fits well even with fewer samples in most cases.
  # Indeed, it seems there are less cases where most of the new samples are generated around one peak.

  resample_and_plot(2)

  return

if __name__ == '__main__':
    main()
