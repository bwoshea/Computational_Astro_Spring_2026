import numpy as np

# set up our time domain
t_start = 0
t_stop = 4.0*np.pi

# number of samples - we're going to vary this from ~100 to 10,000
N_samples = 10000

dt = (t_stop-t_start)/N_samples

# time range
t = np.linspace(0,N_samples*dt,N_samples,endpoint=False)

# function without noise
fx = 4.0*np.sin(30.0*np.pi*t) + 1.5*np.cos(60.0*np.pi*t) + 3.0*np.cos(120.0*np.pi*t)

# function with noise added
fx_noisy = fx + 2.0*np.random.rand(N_samples)


