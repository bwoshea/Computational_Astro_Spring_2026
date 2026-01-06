

## First-order methods

Implement another first order method (Lax-Friedrichs, see eq. (5.30)) and answer the following questions (use plots to support your statement):

- Q: How does the LF generally compare to the upwind method?

LF is more diffusive.

- Q: Does this depend on the initial profile, the CFL factor, and the signal velocity?

Overall not, but disontinuous profile introduces steps.
CFL does not matter here (we'll see that it does later when solving the Euler eqn with a different method.).

- Q: Does the behavior change for a wave traveling to the left? If yes, how and why?

Upwind should not work (as with negative a the stencil is not "upwind" any more) but this depends on how people implemented it.

## Second-order methods

Now implement two second order methods: - Lax-Wendroff, see eq. (5.34) - Beam-Warming, see eq. (5.35) Again, answers the following questions and use plots to support your statements:

- Q: How do these second-order methods generally compare to your first-order results?
- Q: Does this depend on the initial profile, the CFL factor, and the signal velocity?

Less diffusive, but introduce disperive error (wrong wave speed).
Introduce oscillations to the solution for discontinuous inititial conditions.

- Q: How do LW and BW compare against each other (qualitatively)?

For LW oscillation precede the discontinuities. For BW they run after the disc.
BW can handle CFL  up to 2.

- Q: Does the behavior change for a wave traveling to the left? If yes, how and why?

BW should break as the stencil is currently only one sided (for a fixed value of a).

- Q: Finally, did you observe any other interesting behavior?

## Based on your reading, please answer the following questions:

- Q: Qualitatively describe wave steepening, shock wave and rarefaction in your own words.
  - Wave steepening: initial smooth profiles develop into shocks (characteristics converge)
  - Shocks: discontinuities (characteristics cross)
  - Rarefaction: "spread out" (this is bad terminology) (characteristics diverge)

- Q: How (at a high level) would you have to change your code above to use of conservative formulations?

Introduce fluxes rather than finite differences.

- Q: How would you have to change your code above to solve the nonlinear Burgers equation?

Introduce a spatially varying velocity. Adjust computation of dt.

- Q: What is the advantage of using the integral form of the conservation laws in the presented derivations of the LF and LW schemes?

Don't rely on using an explicit Riemann solution due to integration.

- Q: Please write down two questions pertaining to what you've read. These could be related to topics that aren't entirely clear or a point that you thought interesting/surprising.


## Collected questions/feedback from PCA
- terminology: melt -> spread/diffuse

- What is the advantage of the integrals in the LF and LW schemes?
- Could you explain rarefaction again?

## To be discussed/covered in class
- How did reading go?
- How much time did people spent on the PCA?
- Conservative <-> limiting/oscillations
- How can the conservation law solutions be implemented in a problem that does not use periodic boundary conditions?
If the BCs are not periodic, would calculating the fluxes possible cause the solution to diffuse too quickly within its domain, or how could the BCs best be set to avoid this?
- Once the higher density/values/etc with a higher speed "break" over the discontinuity into the lower density/value/etc with slower speeds, does the solution become numerically unstable and breakdown, or is there ways to continue evolving a shock after this point?
- What exactly is being conserved and what are we integrating the flux of?
- I didn't follow the motivation and derivation of the conservative formulations. Why do we make the changes we do? Is it primarily to handle discontinuities (shocks and rarefaction)? I could use a walkthrough of the concepts to better understand conservative methods generally.
- What's the difference between the stable and unstable rarefraction waves/shocks?
- The whole Godunov section is not entirely clear.
- it says to use cell-average values over finite volumes, which I thought was what we were doing already? So do we need to worry about the u_i+1/2 notation?
-  I don't think I understand this term entirely. I'm not sure if I understand the big picture of implementing the conservative form. Does this mean we would need to implement a integral solver? Equation 5.42 made it looks like we were going to use some sort of arrays and stencils again, but with a new additional stencil f (numerical flux) involved, which was made from u. 
- Is adaptive timestepping available for solving the nonlinear Burgers equation?
- What is the computational overhead to preserving conserved quantities?

## Next PCA:
What are the numerical problems with identified/observed so far:
- unstable
- wrong signal velocity
- diffusive

## Specific notes
- Ask Eric if there's a problem with the notebooks.
