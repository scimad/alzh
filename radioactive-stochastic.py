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
N[0] = N0

# Simulate radioactive decay using the Probabilistic approach (Poisson distribution)
for i in range(1, len(t)):
    decay_events = np.random.poisson(l*N[i-1]*dt)
    N[i] = N[i-1] - decay_events

# Plot results
plt.plot(t, N)
plt.xlabel('Time')
plt.ylabel('Number of atoms')
plt.show()
