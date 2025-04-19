# Monte Carlo π Estimation

This project uses the Monte Carlo method to estimate the value of π by randomly generating points in a unit square and checking how many of them fall inside a quarter circle.

## How it works

- Random pair of points (x, y) are generated in the range [0, 1] × [0, 1]
- Points falling inside the quarter circle are counted (where x² + y² ≤ 1)
- π is estimated using the formula:  
  π ≈ 4 × (number of points inside / total number of points)

## Visualizations

- Scatter plots showing point distribution for different sample sizes: 100, 1000, 10000, 100000
- Convergence plot showing how the estimate stabilizes over multiple runs
- Boxplots illustrating the distribution of π estimates for different sample sizes
