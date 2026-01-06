# Day 10 - Conservative methods and flux limiting

## Goals for today's class

* Understand the point of finite volume in this context
* Understand what flux/slope limiters are good for
* Continue to work on implementation of these algorithms (building on previous code)

## Pre-class assignments

* Read Chapter 5 of Zingale
* Implement the 2nd order FV advection code in 1D (without slope limiter).  Test it with a variety of ICs and left- and right-traveling waves.

## In-class activity details

**Plan for the day:** 

Announcements:

* Today is the last day of hyperbolic PDEs.  If you are interested in learning about hydro for your semester project, let me know!
* Discuss plans for the rest of the semester - where are we at?

### Pre-class assignment

* Break into discussion groups
* Make sure your code works!
* Discussion questions:
  * Why is the finite volume approximation useful for solving the wave advection problem?
  * What is the point of a slope limiter (or flux limiter) and how do they work?  (looks for extrema in slope/flux, attempts to minimize that to control oscillations.)  Also, why are there so darned many of them?
  * Why might the method of lines be useful for solving PDEs?  (If we turn the problem into an ODE, or system of ODEs, that represents the initial PDE(s), we can use many common ODE solvers - that can be extremely helpful.)
  * Any questions about multi-dimensional advection?

### In-class assignment

* Verify 2nd order FV code works correctly for all of the problems.
* Implement slope limiter and verify it behaves as expected!


## Instructor notes (for next time)

**Leave feedback on what happened in class today!**
