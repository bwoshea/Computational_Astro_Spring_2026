# Day 19 - Markov Chain MOnte Carlo

## Goals for today's class

* Learn about Markov Chain Monte Carlo as an optimization tool

## Pre-class assignments

* Read some stuff about MCMC

## In-class activity details

**Plan for the day:** 

Announcements:

* Project update #2 is next Tuesday!

### Pre-class assignment

* Make sure to mention that "The MCMC Handbook" (Brooks et al.; PDF provided, and available online) is a great reference.
* Walk through the Metropolis-Hastings algorithm - empasize it's the easiest MCMC algorithm to understand, but there are better ones now!  (emcee, for example)
* Show MCMC video from Jordan - gives them a clue what the algorithm is actually doing!
* MCMC can easily incorporate a Bayesian component, which we will get to later.
* It also parallelizes well, and scales well to many dimensions.

### In-class assignment

* Building on the pre-class assignment - go for it!
* Make sure to use the correct errors!
* At the end, give them the solution.

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2018:  For next time, make sure to remind the students to actually use the correct errors in the in-class assignment: a bunch of them guessed it!  (In contrast to the pre-class assignment where they had noisy data.)

Also, make a "low noise" version of the in-class assignment data file, and ask the students to compare this one vs. the higher noise one.

MCMC video is from Jordan Mirocha.  Make sure to use this!

2021:  Make sure to point students toward the following resources:

* MCMC methods ARAA article:  https://arxiv.org/abs/1706.01629 (and code: https://github.com/sanjibs/bmcmc/ and https://bmcmc.readthedocs.io/en/latest/)
* Hogg & Foreman-Mackey "Data Analysis recipes" paper:  https://iopscience.iop.org/article/10.3847/1538-4365/aab76e 

2023: 

* For in-class assignment, if people are seeing weird results I should suggest that they try different initial values of the parameters.  One of the problems several people saw today was when they chose bad starting values - the MCMC walkers got stuck in weird spots.
* Reference for next time: https://arxiv.org/pdf/1909.11827.pdf (basic point is that there are lots of ways to measure convergence for MCMC)
* Tell students about "particle swarms" as an alternative to MCMC: https://pyswarms.readthedocs.io/en/latest/
* 



