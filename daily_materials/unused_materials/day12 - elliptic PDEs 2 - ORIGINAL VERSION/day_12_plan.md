# Day 12 - Elliptic Equations, 2

## Goals for today's class

* Learn about multigrid!


## Pre-class assignments

* Read Ch. 9 of Zingale's Comp Hydro tutorial (Elliptic Eqtns. + Multigrid)
* Sec. 9.2 of Computational Physics
* Implement 2D Poisson using relaxation method

## In-class activity details

**Plan for the day:** 

Announcements:

* 

### Pre-class assignment

* Break off into discussion groups
* Talk about the solutions; did you get what you expected?  how does this work?
* Questions:
  * How did your test compare to the analytic results?  (What about units?)
  * Residual vs. L1/L2/Linf norms - what do these tell you?  (Residual is what you use when you don't actually know the "true" answer).  
  * Generally, how slow was your code?  (Number of iterations compared to grid size) - helps motivate multigrid!

### In-class assignment

* Multigrid is insanely useful, but too complicated to do in a single class - instead, we're going to talk through it and experiment with it.
* Zingale's example codes are fantastic and a great reference.
* Things to emphasize:
  * Multigrid speeds up convergence for the large-wavelength errors.  Relaxation is very slow there.
  * Algorithm is more complicated, but faster - it's a tradeoff!  (No free lunch in computational methods - always trading off speed, complexity, accuracy, etc.)

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021:

* The students had tons of questions about multigrid; we never actually got to the in-class assignment.  
* Zingale's lecture notes don't actually walk through the whole multigrid method - something to think about.