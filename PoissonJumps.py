from __future__ import annotations
from typing import List, Dict, Union, Tuple

import numpy as np

from matplotlib import pyplot as plt

class PoissonJumps(object):
    """
        Define a PoissonJump Model
        The Simulate method will generate prices and returns, accessible respectively in the fields mReturns and mPrices
    """
    def __init__(self, Drift: float = 0.0, Volatility: float = 1.0, JumpFrequency: int = 3, MinJumpSize: float = 0.05, MaxJumpSize: float = 0.15):
        self.mDrift = Drift
        self.mVolatility = Volatility
        self.mJumpFrequency = JumpFrequency
        self.mMinJumpSize = MinJumpSize
        self.mMaxJumpSize = MaxJumpSize
        self.mPrices = []
        self.mReturns = []

    def Simulate(self, NbPeriods: float = 1.0, NbStepsPerPeriod: int = 252):
        nbSamples = int(NbStepsPerPeriod * NbPeriods)
        # draw returns from GeometricBrownianMotion
        X = np.random.normal(self.mDrift * 1/NbStepsPerPeriod, self.mVolatility * np.sqrt(1/NbStepsPerPeriod), (nbSamples))

        # draw jump flags
        jumpThreshold = self.mJumpFrequency / NbStepsPerPeriod
        jumpFlags = np.random.random((nbSamples)) < jumpThreshold
        print("Nb Jumps: {}".format(sum(jumpFlags)))

        # draw jump values
        jumpVals = np.random.uniform(self.mMinJumpSize, self.mMaxJumpSize, (nbSamples))
        upDownFlags = (np.random.random((nbSamples)) > 0.5) * 2 - 1
        jumpVals = jumpVals * upDownFlags

        # compute returns and prices
        self.mReturns = X + jumpVals * jumpFlags
        X = np.cumsum(X)
        self.mPrices = 100 * np.exp(X)
        
    def Plot(self):
        plt.plot(self.mPrices)
        plt.show()


"""
g = PoissonJumps(0.0, 0.15, 3, 0.15, 0.3)
g.Simulate(10.0, 252)
g.Plot()
"""
