# Day 13 - Parabolic PDEs

## Goals for today's class

* Learning about diffusion and parabolic equations


## Pre-class assignments

* Read Ch. 10.1-10.5 of Zingale, 7.7-7.8 of Pang
* Implement 1D explicit diffusion solver, with C=0.8, C=2


## In-class activity details

**Plan for the day:** 

Announcements:

* HW 2 out - any questions?  Due the Friday **after** break.
* Next week is spring break - enjoy.
* Claire Kopenhafer will be teaching the week after break - we'll have pre-class assignments out shortly. **Also, I signed everybody up for ICER HPCC accounts -- make sure to do the asynchronous training if you have not already!**


### Pre-class assignment

* Discussion
* What happened with the different C for the explicit solver?  (C=2 should be very unstable)
* Did anybody try changing the resolution?

### In-class assignment

* Implement backward-Euler implicit discretization of 1D diffusion equation, test with varied C and N.
* Discuss this - much more stable!
* Why do we really care about this: we want to be able to model diffusive processes in a sensible way - this if often much more expensive because the explicit time steps are very short compared to other things we care about!  (talk about Spitzer conduction as an example - section 10.5 of Zingale's notes!)

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021: I'm starting to think I need to put parabolic, elliptic PDEs after hypberbolic.  Otherwise it doesn't really make sense compared to what Zingale has in his lecture notes.

2023:  Did parabolic after elliptic.  It worked out fine.