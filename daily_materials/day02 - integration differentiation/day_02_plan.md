# Day 02 - numerical integration, differentiation, floating-point precision

## Goals for today's class

* Learn about numerical integration - low and high order methods
* As above, but differentiation
* Learn that numerical precision is a thing, and how floating-point approximations must be considered when you're doing calculations.

## Pre-class assignments

* Read Newman Ch. 5 and Goldberg floating-point arithmetic paper, also Wikipedia articles on these various things.
* Write code to calculate a 3-point derivative, integrate with the trapezoidal rule, and actually calculate the error.

## In-class activity details

**Plan for the day:** 

Announcements:

* Pre-class for next week's sessions are out

### Pre-class assignment

Question: how long did it take to complete this assignment?

* Discussion in groups of 3:
  * Discuss the two readings and the actual assignments.
  * Compare questions you have about the readings: what questions remain?
  * Compare the results from the code: do you get the same answers?  What's the answer to part 3 of the PCA?
* Floating point arithmetic: what are the implications?  
  * You can only ever get answers that are so good when you're using floating point numbers...) - no answer is every completely accurate!
  * A whole lot of numerical analysis (methods) are trying to get around the limitations of floating-point numbers, or at least mitigate things like summation error
  * It's important to be aware of this - you can really shoot yourself in the foot!  (CGS and floating-point don't necessarily go well together.)

### In-class assignment

* Read through it, think about it, let's make predictions for what we'll see for the plots.
* Then do it: Brian will walk around.
* Wrapup: outcome?  What did you see?  Was it what you expected to see?

Then, for next time: we'll be doing interpolation and root-finding.  Pang is actually better than Newman for this.

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

Fall 2018: This one went pretty well - we had some issues with the function used in the pre-class assignment, but now that I've changed it to e^x sin(x), it worked fine in terms of errors.

Spring 2021: Pre-class assignment took almost an hour, including discussion in breakout rooms and as a group.  It could be because it's Zoom and we're chatty; it's hard to tell at this point.  We'll see how it goes for the next couple of weeks!

