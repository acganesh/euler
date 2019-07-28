import numpy as np


fn = lambda x: x**3
vals = np.arange(0, 1, 0.0001)

fvals = fn(vals)

integral = np.trapz(fvals, vals)
print integral

