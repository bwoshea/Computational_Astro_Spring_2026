# Day 12 - Elliptic Equations, 2

**NOTE:** This is totally different than previous years!  I may wish to reexamine this in the future!

## Goals for today's class

* Learn a little bit about multigrid!


## Pre-class assignments

* Nothing!

## In-class activity details

**Plan for the day:** 

Announcements:

* Homework #1 - I didn't grade it, people don't seem to have completed it (and certainly didn't follow the instructions)
* I need people to decide what they're going to do regarding the homework/project situation by no later than Thursday, please.

### Pre-class assignment

* Break off into discussion groups
* Talk about last class's pre-class assignment, and the in-class assignment from last time.
  * How should this work? 
  * Let's try it.
  * What is the point of L1/L2/inf norm?  (Give a sense of errors.)
  * How slow is your code?  (Number of iterations compared to grid size - helps to motivate multigrid.)

### In-class assignment

* Multigrid is insanely useful, but too complicated to do in a single class - instead, we're going to talk through it and experiment with it.
* Zingale's example codes are fantastic and a great reference.
* Things to emphasize:
  * Multigrid speeds up convergence for the large-wavelength errors.  Relaxation is very slow there.  Think about why the large-wavelength results are slow - iteration only couples neighboring cells, so it's going to take longer!
  * Algorithm is more complicated, but faster - it's a tradeoff!  (No free lunch in computational methods - always trading off speed, complexity, accuracy, etc.)

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021:

* The students had tons of questions about multigrid; we never actually got to the in-class assignment.  
* Zingale's lecture notes don't actually walk through the whole multigrid method - something to think about.

2023:  This is a totally different day of class than previous years.  I basically threw out any multigrid experimentation, and am just having the students go through some  materials from the previous class and then freestyling about multigrid methods.

