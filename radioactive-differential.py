import numpy as np
import matplotlib.pyplot as plt

# Define parameters
l = 0.1  # decay constant
N0 = 1000  # initial number of atoms
t_max = 30  # maximum simulation time
dt = 0.1  # time step size

# Initialize arrays
t = np.arange(0, t_max, dt)
N = np.zeros_like(t)

# Set initial condition

# Simulate radioactive decay using the differential eqn
for i, t_ in enumerate(t):
    N[i] = N0 * np.exp(-l*t_)

# Plot results
plt.plot(t, N)
plt.xlabel('Time')
plt.ylabel('Number of atoms')
plt.show()
