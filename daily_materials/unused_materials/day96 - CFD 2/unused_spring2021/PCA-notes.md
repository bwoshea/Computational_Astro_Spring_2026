# Questions
- After seeing how many operations even the "simple" functions involve, I can imagine for all but the simplest of problems the run time becomes increasingly long. In general, is it best to always perform the analytic calculations for the EOS, getPrimFromCon, etc., or is pre-building a table of the values and interpolating between them sufficient, more or less creating a look-up table indexed by the primitive variables? For a more complicated EOS and a system evolving for a longer time, I would think a look-up table with interpolation for the EOS could be significantly faster

- I'm most confused on the getFlux. I have down $F = [rhou rhou**2 + rho . u*(E + p)]$ but I'm confused in the sense that I use U to find rho, E, and p and then I also use the same U again? Is this correct?

[except for the rho <-> p part yes. It's just an additional relation to close the system]

- During the Riemann solver, we advance a half timestep to find UL_bar and UR_bar. We then use those values to calculate the flux at the interface. Once the F_1/2's are calculated, do we return to our original time and compute a full step, or just advance from the half timestep we already calculated?

[analogous to, e.g., midpoint rule or RK methods, i.e., make full timestep with information gained at intermediate steps]

# General remarks
- np.max() function ( with axis, or np.mininum)
- use of indices, e.g., Id_rho
- numpy arrays:
  - e = np.zeros_like(p)
  - e = p/(rho*(gamma-1))

# Plan for ICA
- compare implementations
- discuss bugs
- pair up and partner program HLL and main time loop
- reproduce shock tube results, how does it differ with CFL and why?
