# Day 24 - Bayesian stats, 2

## Goals for today's class

* Multi-parameter Bayesian models and why to use Bayesian stats?
* Make a Bayesian MCMC code!

## Pre-class assignments

* Read Andreon Ch. 6.1-6.2, 10 and write down some questions

## In-class activity details

**Plan for the day:** 

Announcements:

* Homework #3 is due on Friday 4/10!
* No class next Tuesday 4/14 - I will be out of town.  Start time series analysis next Thursday (4/16).  One PCA for both days of time series analysis!
* Next semester project update next Wednesday 4/15 - code should be close to completion!

### Pre-class assignment

Questions:

* How do you do a multi-parameter estimation?
* Ch. 10: what are the advantages and shortcomings of Bayesian methods against non-Bayesian alternatives?  (Note that the authors are clearly Bayesian partisans, but they make reasonable points.)

### In-class assignment

We're going to modify some code from last time to include Bayesian priors, and then experiment with it.  Spend some time looking through the code, and then think about how to deal with the prior.  We want to address some questions:

* What happens when you use a flat prior?
* What happens when you make the prior strongly exclude the values that the linear regression returns?  (best-fit values and 2D histogram)
* If you use fewer data points, what happens to your best-fit values and 2D histogram?  In other words, how important is the prior as you change the amount of data you have?

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021: today went well, the students liked the in-class assignment!

2026:
 
* I really need to update the dataset!  It's very old.  Maybe Megan can give me a new version?  Add link to the ACCEPT 2 paper (https://ui.adsabs.harvard.edu/abs/2026ApJS..282...61D/abstract) 
* Also, I'm really starting to dislike the Andreon book - the focus on the weird programming language is annoying and distracting.  Can I go back to Feigelson & Babu chapter on Bayesian stats and see if there's a good supplement?