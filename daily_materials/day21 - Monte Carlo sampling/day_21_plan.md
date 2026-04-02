# Day 21 - Monte Carlo sampling

## Goals for today's class

* Understand Monte Carlo as a sampling technique
* Experiment with Monte Carlo integration and Monte Carlo sampling

## Pre-class assignments

* Read Owen chapters 1 and 2
* Jupyter notebook on Monte Carlo integration

## In-class activity details

**Plan for the day:** 

Announcements:

* First update for semester project (background + code) was due last night!  You should be thinking about the direction your project is going - if you're doing a "choose your own adventure" project, are things looking promising?

### Pre-class assignment

First, get everybody to compare their codes!

Questions/discussion:

* Monte Carlo as a sampling technique
  * How do we use it?  (optimization, numerical integration, generating draws from a probability distribution)
  * Why do we use it at all?  (Gives approximate answers, but often in situations where it's difficult or impossible for other [typically deterministic] methods.)
* How did the Monte Carlo integration go?
* How do computers generate (pseudo)random numbers?  Are they actually random?  What does that mean?  (Give a brief presentation: https://en.wikipedia.org/wiki/Pseudorandom_number_generator)  In practice, this is not an issue any more but if you use Linux or Unix the system random number generator should be viewed with suspicion. The Mersenne Twister algorithm (https://en.wikipedia.org/wiki/Mersenne_Twister) is the PRNG used in Python and R (and Excel, Matlab, etc.) and is more than sufficient for almost all needs unless you're doing cryptography.

### In-class assignment

Monte Carlo and the stellar IMF - we're going to make some distributions, and experiment with using Monte Carlo modeling to estimate uncertainties due to things we don't understand.

Let's spend ten or fifteen minutes running through the code that's in the ICA, and go from there.  (Walk students through it and explain what it does.)

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

Spring 2021: Make sure to have the students look at the wikipedia page on pseudo-random number generators as part of their pre-class assignment next year:  https://en.wikipedia.org/wiki/Pseudorandom_number_generator .  (Note: I already updated the pre-class assignment.)  Also, this went pretty well!
