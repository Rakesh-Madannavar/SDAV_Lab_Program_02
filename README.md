# SDAV Lab Program 02: Discrete Probability Distributions in Python

This is my second lab program for SDAV. It uses Python to work with three common discrete probability distributions: Binomial, Poisson and Geometric. Each one has its own script. Each script calculates some values and draws a graph.

## What's in this repo

- `Binomial.py`: Binomial distribution
- `poisson.py`: Poisson distribution
- `Geometric.py`: Geometric distribution

## What each file does

**Binomial.py**
Uses 20 trials with a 0.35 chance of success each time. It works out the mean, variance, second moment, skewness, the chance of exactly 7 successes, and the chance of at most 10 successes. Then it draws a bar chart with a red dashed line at the mean.

**poisson.py**
Tries four values of λ (1, 3, 5 and 10). For each one, it generates 5,000 random numbers and compares the average of those numbers with the theoretical mean. Then it draws one line graph showing how the shape changes as λ changes.

**Geometric.py**
Uses a success chance of 0.3. It works out the mean, the chance that the first success comes on trial 1, and the chance that it takes more than 5 trials. Then it draws a bar chart of the probabilities.

## What you need

- Python 3
- matplotlib
- numpy
- scipy

## How to run

1. Clone this repo:
   ```
   Download this Repo
   ```
2. Run any script you like:
   ```
   python Binomial.py
   python poisson.py
   python Geometric.py
   ```

A graph window will open when each script finishes.

## Author

Rakesh Madannavar
GitHub: [@Rakesh-Madannavar](https://github.com/Rakesh-Madannavar)
