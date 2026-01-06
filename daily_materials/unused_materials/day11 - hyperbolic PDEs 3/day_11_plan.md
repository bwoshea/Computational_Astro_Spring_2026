# Day 11 - Nonlinear problems (Burgers' equation)

## Goals for today's class

* Discuss conceptual difference between linear and nonlinear equations (formation of discontinuities/shocks)
* Understand the Riemann problem and it solution (Riemann fan)
* Experiment with the instructor code (in PCA directory)

## Pre-class assignment

* Read Chapter 6
* Extend previous finite volume code to implement Burgers' equation using 2nd order method w/limiter
* Test that code on the rarefaction, sinusoidal ICs and verify it behaves correctly.

## In-class activity details

**Plan for the day:** 

Announcements:

* Doing computational fluid dynamics next week!  Today's class will build on that.  PCAs for next week, as well as homework #2 and the semester project, are going to be made available soon.  (**verify this is true**)


### Pre-class assignment

Assignment:

* Discuss the pre-class assignment: did you get it working?
* What are the questions that you have from the reading?
* What's the idea behind this shock thing?  What about characteristic tracing?

### In-class assignment

Talk through Section 6.1, focusing on explaining the shock formation: characteristics intersect, which means you can't go backwards to find an initial state.  Opposite of this is a rarefaction, where characteristics diverge.  We can think of any solution to Burgers' equation as locally being one or the other; so, we can think of our conservative update to u(x,t) to u(x,t+dt) as using fluxes at cell faces calculated using a simple set of logic for shocks vs. not-shocks (converging vs. diverging values at a cell face).  

**Walk through this logic - equations 6.12 - 6.15**

This means that each interface is only informed by the characteristics (linear projections of wave information) that's propagated toward that interface from cell centers.  This is simple for Burgers' equation but gets more complicated when there are more waves (like in a fluid; sound wave + advection + shocks in each direction).

**Show the traffic standing wave video -- can see a compression wave that's propagating!** 

Because u(x,t) varies through the domain, this means that our timestep varies, and we have to take the smallest timestep available.

**ACTUAL ACTIVITY:** Everybody should get my code, look at it, and create a variety of initial conditions with both positive and negative velocities.  Experiment with different ICs (esp. top-hat and Gaussian) and see if you can figure out why it behaves the way it does, thinking of it in terms of what the local characteristics are doing.  Then we'll discuss!

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2018: Talk about traffic standing waves; use the movie I put in this directory to do so!

2021: we didn't really get to much of the activity, because we spent almost all of our time talking about concepts.  I gave them the PCA solutions and asked them to experiment later.