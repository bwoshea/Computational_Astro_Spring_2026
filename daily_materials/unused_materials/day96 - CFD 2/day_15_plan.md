# Day 15 - Computational Fluid Dynamics, 2

## Goals for today's class

* Understand and be able to articulate how to write a 2D finite volume hydro code.

## Pre-class assignment

* Read Chapter 8 ("Euler Equations: Numerical Methods") from Zingale, not quite all of it.
* Read Wikipedia page on Riemann solvers.
* Install pyro2 code.
* Answer some questions.

## In-class activity details

**Plan for the day:** 

Announcements:

* Next week: we're going to leave PDEs.  Monday = FFTs, Wed = Stats.  If you have not already bought Feigelsen & Babu, now would be an extremely good time to do that.

### Pre-class assignment

Discuss pre-class activity:

1. What are the key components of a code that solves the Euler
equations for the 1D Sod Shock Tube (described in Section 8.9.1)?  How
is this similar to, or different from, the codes you've created so far
for the linear advection equation and Burgers' equation?

2. What are the benefits and drawbacks of using differnet methods
of reconstructing the states of cell interfaces?  Specifically,
compare and contrast piecewise constant, piecewise linear, and
piecewise parabolic reconstruction (as discussed in Sections 8.2.1-3)
in terms of accuracy, simplicity, and speed.

3. Why is there such a profusion of Riemann solvers for
computational fluid dynamics?  Why doesn't everybody use the best one?

Try to get this done relatively quickly.

### In-class assignment

Break it into small groups; look at code; do some experiments.  Talk it through!

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021: for next time, update the pre-class assignment to tell students to install the pyro2 code (links in the in-class assignment).  Also, note that for the in-class assignment there are some links with hashtags that break OS X preview (mitigated with bit.ly); check to see if those are fixed and/or if the bit.ly links still work.

Also, we spent the entire class talking about the pre-class assignment, and never got to the in-class assignment.  Oops!