from __future__ import annotations
from typing import List, Dict, Union, Tuple

import numpy as np

from matplotlib import pyplot as plt

class GeometricBrownianMotion(object):
    """
        Define a GeometricBrownianMotion Model by specifying a drift and a volatility parameters
        The Simulate method will generate prices and returns, accessible respectively in the fields mReturns and mPrices
    """
    def __init__(self, Drift: float = 0.0, Volatility: float = 1.0):
        self.mDrift = Drift
        self.mVolatility = Volatility
        self.mPrices = []
        self.mReturns = []

    def Simulate(self, NbPeriods: float = 1.0, NbStepsPerPeriod: int = 252):
        X = np.random.normal(self.mDrift * 1/NbStepsPerPeriod, self.mVolatility * np.sqrt(1/NbStepsPerPeriod), (int(NbStepsPerPeriod * NbPeriods)))
        self.mReturns = X
        X = np.cumsum(X)
        self.mPrices = 100 * np.exp(X)

    def Plot(self):
        plt.plot(self.mPrices)
        plt.show()


"""
g = GeometricBrownianMotion(0.0, 0.15)
g.Simulate(3.0, 252)
g.Plot()

sims = []
g = GeometricBrownianMotion(0.0, 0.15)
for _ in range(50):
  g.Simulate(3.0, 252)
  sims.append(g.mPrices)


indices = np.arange(len(sims[0]))
for sim in sims:
  plt.plot(indices, sim)

plt.title("Geometric Brownian Motion")  
plt.savefig("img/GeometricBrownianMotion.png")
plt.show()
"""
