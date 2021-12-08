# import necessary libraries
import math
import random
import numpy as np
import matplotlib.pyplot as plt


# Class for up-and-out American-style Asian puts option
class MonteCarlo:
    def __init__(self, spot, time, interest, dividend, volatility, period, simulations):
        self.spot_price = spot
        self.time = time
        self.interest_rate = interest
        self.dividend_rate = dividend
        self.volatility_rate = volatility
        self.period = int(period)
        self.path = int(simulations)
        self.deltaT = time / period

    # Generate random path
    def random_path(self):

        # Randomized the path of Brownian Motions
        self.randomWalk = np.zeros((self.path, self.period + 1))

        # Initialize price
        self.randomWalk[:, 0] = self.spot_price

        # Random Walk each period. The price follow brownian motion
        for i in range(1, self.period + 1):
            self.randomWalk[:, i] = self.randomWalk[:, i - 1] * np.exp(
                (
                    self.interest_rate
                    - self.dividend_rate
                    + (self.volatility_rate ** 2) / 2
                )
                * self.deltaT
                + self.volatility_rate
                * np.sqrt(self.deltaT)
                * np.random.normal(size=self.path)
            )

    # Apply least square method on all path
    def pricing(self):

        Y = self.randomWalk[:, -1]

        # Calculate mean and variance of the stimulation
        self.mean = np.mean(Y)
        self.std = np.std(Y) / np.sqrt(self.path)

    def plot(self, bin=50, sampling=50):

        # draw histograms
        f1 = plt.figure(1)
        n, x, _ = plt.hist(self.randomWalk[:, -1], bins=bin)

        x_bar = 0.5 * (x[1:] + x[:-1])

        plt.title("Distribution")
        plt.xlabel("Stock Price")
        plt.ylabel("Occurance")

        plt.figtext(
            0.01,
            0.01,
            f"estimated price: {round(self.mean, 4)}\nstandard deviation: {round(self.std, 4)}",
            fontsize=8,
        )

        # draw the fitting curve
        plt.plot(x_bar, n)

        # draw sampled path
        f2 = plt.figure(2)

        x = np.arange(0, self.period + 1)

        for path in random.sample(range(self.path), sampling):
            plt.plot(x, self.randomWalk[path, :])

        plt.title("Sampled Path")
        plt.xlabel("Period")
        plt.ylabel("Price")

        plt.show()
