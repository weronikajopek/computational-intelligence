# Import libraries
import random
import matplotlib.pyplot as plt
import numpy as np

# Generate random points and classify them
def generate_and_classify(n):

    # Create lists for points inside circle and outside circle
    inside = []
    outside = []

    # Check whether points are inside or outside the circle
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # If a point is inside, append its coordinates to the inside list
        if x**2 + y**2 <= 1:
            inside.append((x, y))
        # If a point is outside the circle, append its coordinates to the outside list
        else:
            outside.append((x, y))
            
    # Calculate the estimated value of pi
    pi_estimate = 4 * len(inside) / n
    return inside, outside, pi_estimate

# Create the scatter plot
def plot_points(inside, outside, n, ax):
    if inside:
        x_in, y_in = zip(*inside)
        ax.scatter(x_in, y_in, color='blue', s=1, label='Inside Circle')
    if outside:
        x_out, y_out = zip(*outside)
        ax.scatter(x_out, y_out, color='red', s=1, label='Outside Circle')

    # Draw the circle
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=1)
    ax.add_artist(circle)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f'N = {n}')
    ax.legend()


# Track the convergence
def track_convergence(n_points, runs=10):
    plt.figure(figsize=(10, 6))
    for _ in range(runs):
        estimates = []
        inside = 0
        for i in range(1, n_points + 1):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if x**2 + y**2 <= 1:
                inside += 1
            estimates.append(4 * inside / i)
        plt.plot(estimates, linewidth=1)

    plt.axhline(y=np.pi, color='black', linestyle='--', label='π ≈ 3.1416')
    plt.ylim(2, 4)
    plt.xlabel('Number of points')
    plt.ylabel('Estimated π')
    plt.title(f'Convergence of π estimate for {runs} runs')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create boxplots
def boxplot_analysis(N_values, num_runs):
    all_estimates = []
    labels = []

    for N in N_values:
        estimates = []
        for _ in range(num_runs):
            inside, _, pi_est = generate_and_classify(N)
            estimates.append(pi_est)
        all_estimates.append(estimates)
        labels.append(f'N={N}')

    plt.figure(figsize=(10, 6))
    plt.boxplot(all_estimates, labels=labels, showmeans=True)
    plt.axhline(y=np.pi, color='red', linestyle='--', label='π ≈ 3.1416')
    plt.ylabel('Estimated π')
    plt.title(f'Estimation Accuracy for Different N')
    plt.legend()
    plt.grid(True)
    plt.show()


# Create the scatter plots for every number in the n_values list
n_values = [100, 1000, 10000, 100000]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for i, n in enumerate(n_values):
    inside, outside, pi_estimate = generate_and_classify(n)
    # Plot inside the right subplot
    ax = axes[i // 2, i % 2]
    plot_points(inside, outside, n, ax)
    ax.set_title(f'N = {n}')

plt.tight_layout()
plt.show()

# Track the convergence for 10 000 points and 10 runs
track_convergence(n_points=10000, runs=10)

# Create the boxplots for 100, 1000, 10000, 100000 and 10 runs
boxplot_analysis(N_values=[100, 1000, 10000, 100000], num_runs=10)