# Day 11 in-class assignment

### Transition from PCA
- Copy your PCA over and delete the old questions at the bottom
- (tbc) Update for PCA in teams in order to get a easily extendable base (e.g., with respect to solver and boundary conditions implemenation)

### First-order methods

Implement another first order method (Lax-Friedrichs, see eq. (5.30)) and answer the following questions (use plots to support your statement).

How does the LF generally compare to the upwind method? 

Does this depend on the initial profile, the CFL factor, and the signal velocity? 

Does the behavior change for a wave traveling to the left? If yes, how and why?


### Second-order methods

Now implement two second order methods:
  - Lax-Wendroff, see eq. (5.34)
  - Beam-Warming, see eq. (5.35)

Again, answers the following questions and use plots to support your statements.

How do these second-order methods generally compare to your first-order results? 


Does this depend on the initial profile, the CFL factor, and the signal velocity? 

How do LW and BW compare against each other (qualitatively)?

Does the behavior change for a wave traveling to the left? If yes, how and why?


Finally, did you observe any other interesting behavior?
