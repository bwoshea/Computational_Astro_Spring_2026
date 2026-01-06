# Day 14 - Computational Fluid Dynamics, 1

## Goals for today's class

* Discuss Euler equations and make sure that people understand them, in preparation for implementation.

## Pre-class assignments

* Read Zingale Chapter 7, Wikipedia page on Rankine-Hugonio jump conditions.
* Work through the math.
* Answer a bunch of questions about the Euler equations.

## In-class activity details

**Plan for the day:** 

Announcements:

* HW 2, 3 and semester project out for everybody who is doing that.

### Pre-class assignment

* Break people up into groups of 4 (not the same groups as before)
* Specific questions:
  * Where in the derivations do you get confused?
  * Talk about answers to the questions.

Questions:

  1. Why might we want to use both the conserved form and primitive form of the Euler equations? In other words, what might each set of equations potentially tell us?
  2. How are the Euler equations similar to the linear advection equation and/or Burgers’ equation, and how are they different?
  3. What’s the point of all of the linear algebra in this chapter? In other words, what does it tell you about the Euler equations and how they propagate information?
  4. What are the types of waves that are in the Riemann problem for the Euler equations? How does your answer differ from Burgers’ equation? (And how does this relate to the previous question, about linear algebra?)

Answers:

  1. Primitive to solve Riemann problem (using characteristic equations).  Conserved to update.
  2. Similar to both in that they're hyperbolic and have wave propagation; Similar to Burger's in that they're nonlinear in that wave propagation; Different in that there are three equations instead of one, with three wave speeds instead of one (and thus it's more complex).
  3. Gives us the eigenvalues (propagation speeds of waves/characteristics) and eigenvectors (information about jumps of information across characteristics, and relation between them).
  4. Types of waves: shock, rarefaction, contact discontinuity.  Burgers' effectively has a shock but not a rarefaction, and no contact discontinuity.  This is because there's only one wave in Burger's, so all you get is one possible type of discontinuity (shock!)

### In-class assignment

There isn't a specific in-class assignment today - just answer any questions the students have, and work through whatever they want to know!

Things to emphasize (in addition to the answers to questions above):

* The wave solutions to the Riemann problem will directly lead to updates to the hydro equations.
* We use primitive variables for our characteristics because it's physically convenient, but typically update the conserved variables because they're conserved (which is desirable, and a key point to the finite volume equations).  We don't have to do it this way, but it's helpful - calculating the eigenvalues and eigenvectors of the conserved quantities is much more complex.
* There are direct analogues between Burgers' equation and the Euler equations.
* This works in a similar way for Navier-Stokes, but with viscosity you either have additional complexity due to the diffusive/viscous component or you have to operator split.

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021: class went well, I'm pretty happy with it!  Lots of good questions.