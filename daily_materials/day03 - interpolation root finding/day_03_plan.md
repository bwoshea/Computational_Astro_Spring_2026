# Day 03 - Interpolation and root finding

## Goals for today's class

* Learn about interpolation and root-/extrema-finding, and their limitations

## Pre-class assignments

* Read Pang/Newman sections on interpolation and root/extrema finding
* Write a linear interpolation code and compare to the actual solution, compare to scipy.interpolate.
* Write code to implement Newton's method and bisection method for finding roots of functions.

## In-class activity details

**Plant for the day:** Discuss pre-class assignment regarding interpolation and root-finding, and then we're going to spend the day trying to break root-finders!

Announcements:

* We're going to be working on linear algebra and debugging next!  There are two new PCAs up.  **These may take time - get started early!**

### Pre-class assignment

* How long did it take?
* Get people to talk about their experiences with the pre-class assignment:
  * Interpolators: experiences?  Does interp1D seem like it works well?  How might this extrapolate to multiple dimensions, and how might it get more complicated?
  * How might root finding get more complicated in multiple dimensions?  Think about the types of values you might find, and how you might break an interpolator (non-monotonic, artificial extrema, not a single ideal solution, etc.)
  * How is a tool for finding minima and maxima different than a root finder?  (1st derivative of function is zero, but you also need to look for local extrema and figure out if it's a min or max)
  * Root-finding: any problems with your root-finders?  What was your experience with bisection vs. Newton's method in terms of number of iterations?  Which seems more robust, and which seems quicker?
  * How would you deal with it if you had muliple roots?  (maybe something with both 1st derivative and function, or second derivative, etc.?)

### In-class assignment

* We're going to try to understand the parameters for what breaks different root-finders.  See which ones are robust but slow, and which ones are fast but flighty.  (Are some fast and robust?)
* Everybody pick your own functions and intervals, and keep notes.  We'll experiment for a half hour or so and then convene.
* At the end: make some notes about different methods and their outcomes.
* Push your notes to the repository when you're done!

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**
