# Day 21 - Bayesian stats, 2

## Goals for today's class

* Multi-parameter Bayesian models and why to use Bayesian stats?
* Make a Bayesian MCMC code!

## Pre-class assignments

* Read Andreon Ch. 6.1-6.2, 10 and write down some questions

## In-class activity details

**Plan for the day:** 

Announcements:

* Will have just a single pre-class assignment for next week (due Sunday night), which is on time series analysis (from Feigelson)
* Next week is the last week of class!

### Pre-class assignment

Questions:

* How do you do a multi-parameter estimation?
* Ch. 10: what are the advantages and shortcomings of Bayesian methods against non-Bayesian alternatives?

### In-class assignment

We're going to modify some code from last time to include Bayesian priors, and then experiment with it.  Spend some time looking through the code, and then think about how to deal with the prior.  We want to address some questions:

* What happens when you use a flat prior?
* What happens when you make the prior strongly exclude the values that the linear regression returns?  (best-fit values and 2D histogram)
* If you use fewer data points, what happens to your best-fit values and 2D histogram?  In other words, how important is the prior as you change the amount of data you have?

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021: today went well, the students liked the in-class assignment!