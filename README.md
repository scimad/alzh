## Modelling a radioactive process:

## Using a differential equation

The solution to the differential equation is:

$N(t) = N(0) * e^{-\lambda t}$

```python
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

```
![Differential](https://github.com/scimad/alzh/blob/main/differential.png)

## Using a stotchastic model (every decay event is a poisson process(?))
```python
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
```

![Stochastic](https://github.com/scimad/alzh/blob/main/stochastic.png)
