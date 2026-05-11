# Day 19 - nonparametric statistics and data smoothing

## Goals for today's class

* Learn about nonparametric statistics (Feigelson Ch. 5)
* Learn about data smoothing (density estimation)  (Feigelson Ch. 6)

## Pre-class assignments

* Read Feigelson Chs. 5 and 6
* Work through Jupyter notebook w/some datasets.



## In-class activity details

**Plan for the day:** 

Announcements:

* We're going to do a quick project roundtable today.
* Working on grading HW 2 this week! 
* For next Tuesday:  Ch. 7 of Feigelson, on linear and nonlinear regression
* Is anybody getting the sense that Feigelson and Babu really think astronomers are bad at statistics?  (In all fairness, statisticians think everybody who isn't a statistician is bad at statistics, and any positive outcomes they get are purely coincidental.)

### Before we do PCA

Roundtable: **What are you doing for your semester project?**

### Pre-class assignment

* Read Chs. 5 and 6 of Feigelson (nonparametric stats, density est.)
* Go through Jupyter notebook and answer some questions
* In class:
  * Discuss the chapters, come up with questions
  * Check with each other about the notebook - did you get the same answers?  What are they?
* Chapter 5 questions:
  * In general, what does "nonparametric" mean?  (Don't know or assume anything about underlying data distribution/shape)
  * Why is it often appropriate to use nonparametric statistics in astronomy?  (We often don't know underlying data distribution; robustness.)
  * Why is median value vs. mean value an issue, and similarly standard deviation vs. percentile statistic?  (median - robustness.  spread - also robustness, more appropriate capturing of asymmetric data distributions.  Standard deviation assumes Gaussianity; percentile statistics require no such assumption.)
  * When is it inappropriate or inadvisable to use nonparametric statistics or inference?  (Sometimes inefficient or slow compared to parametric models; KS statisics fall apart for multivariate datasets and don't give believable values.)
* Chapter 6 questions:
  * Why are histograms a problem, and how can we do better?  (i.e., why do histograms suck?  But why do we keep using them?)  Lots of reasons - fixed bin widths are arbitrary and problematic.  Probability distribution functions are better.
  * When we're talking about kernels in this chapter, what are they and why is their choice potetntially important?
  * How does data smoothing get harder as datasets go to higher dimensionality?

**Observation for the students:** This is another "big list of options" chapter from F&B - remind them that they should approach these things in the spirit of trying to get the key points, and then they should remember that this reference exists for the future.

### In-class assignment

Focusing on discussion of the pre-class assignment.

Remind students - there are existing libraries/tools for all of the methods/techniques we're talking about - make sure you understand what's going on, but never implement these things yourself unless there's some extremely compelling reason to do so!

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021: 