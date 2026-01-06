# Day 9 - Linear advection

## Goals for today's class

* Content:
  * linear advection
  * understand stability of a scheme
  * get a first sense for numerical diffusion
* Practice: Write reusable code

## Pre-class assignments

* Read Zingale Ch. 4
* Implement FTCS and upwind method for one smooth (Gaussian pulse) and one discontinous (top hat) initial condition

**Plan for the day:** 

## Announcements

* Talk about plans for moving forward
* Overview of the hyperbolic PDE days / how this leads to hydro algorithms
* I'll get you the pre-class assignment for the next class session by tomorrow!

## In-class activity details

* Talk about plan for next couple weeks
  * Next week: more hypberbolic PDEs
  * Week after: I'm out of town.  ICER workshop (in class both days)
  * After that: parallel computing!

* Discuss pre-class assignment
  * FTCS is unconditionally unstable; upwinding works better
  * Smooth profiles are better 'maintained' than sharp profiles.  What happens with this as you change the grid resolution?  (Higher resolution should equate to better solutions, less weird behavior at corners in the top hat solution, etc.)

* Talk about numerical diffusion
  * The way that we discretize the solution (i.e., FTCS, upwinding, etc.) causes the solution to "smear out" in the manner analogous to physical diffusion, but depending entirely on the numerics.
  * People who develop fluid dynamics methods spend a lot of time thinking about how to reduce numerical diffusion in order to increase the fidelity of the simulation.
  * However, sometimes it's really useful to add it in - for example, shock waves in fluids or current sheets in plasmas are nominally infinitely thin, which is numerically a problem, so sometimes you want to add a tiny bit of it into the code to make your solution stable ("numerical viscosity" for the momentum terms, or "numerical resistivity" in the magnetic field).
  * As with everything, this is a tradeoff - you can reduce or eliminate numerical diffusivity, but your solution gets more complex and/or expensive.
* Talk about numerical stability (slides)

* In-class:
  * I want people to clean up their codes, make sure that they are readable and make sense - we're going to do some peer review
  * Make sure code can handle both positive and negative values of velocity (u < 0 and u > 0).  If you don't get the same answer for u < 0 and u > 0, something's wrong!
  * Do some tests with upwinding with various grid sizes, C, u>0, u<0?
  * Hvae a discussion about how this went!



## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021: I'm completely changing what Philipp did; he put everything in notebooks, and I'm not going with that this year.  Next time I teach this, i want to totally revisit what I do for the hyperbolic PDEs section, and possibly move it to before the parabolic/elliptic PDEs.

2023: I made a huge screwup - a bunch of materials were missing this year.  In previous years I started with elliptic PDEs and had the students read the first few chapters of Zingale's notes; however, when I moved hyperbolic PDEs to be at the beginning this year I neglected to move that material up.  I need to fix that next time, otherwise a lot of stuff won't make sense.  (For example, the students weren't clear on finite volume vs. finite difference, didn't know L2 norms, etc.)

This was removed from the elliptic PDE markdown file, as discussion about the PCA:

The point of the PCA was to get people to think about grids and solving problems on grids, since that's one primary way that we deal with PDEs.  Also I want you to experiment with solving elliptical equations on grids.

Norms: why do we have different norms?  For example, "inf norm" vs. L2 norm?  (One highlights the most extreme error, the other highlights a more global sense of error.) 

PDE types: mathematically, there are three categories.  What are the practical differences?  Hyperbolic: initial-value/time-dependent (local solutions).  Elliptic: boundary value/time-independent (requires global solutions).  Parabolic: aspects of both; time-dependent but global.

Grids:  Why grids?  Why finite difference vs. finite volume?  (sampled point in space vs. actual volume element w/average value stored).  Indices of cell centers vs. cell faces.  Finite volume is useful for conservation laws, as we'll see.  What about boundary conditions?

