# Day 20 - Regression

## Goals for today's class

* Learn about regression and how you do it
* Practice nonlinear regression in class!

## Pre-class assignments

* Read Chapter 7
* Write a bit of code to do linear regression

## In-class activity details

**Plan for the day:** 

Announcements:

* Next week is all about Monte Carlo - that's one of my favorite topics!  So incredibly useful!
* Project update #1 is due next Monday, 3/30 - need to have background reading done and start your implementation.

### Pre-class assignment

* Discuss with your neighbors, and also compare results of your codes
* What questions do you have? 

Some questions to ask:

* What is regression?
  * A way of estimating functional relationships
* Why is regression useful in astronomy?
  * Lets us examine both empirical relationships (e.g., color-magnitude) and physical models (fitting of a blackbody).  Another way of thinking about this is "apparent" vs. "causal" relationships.
* Why use weighted least squares over least squares?  When would you use one vs. the other?
  * Not all data points typically have the same errors, so this lets us take that information into account.
* How does least squares estimation differ from a maximum likelihood estimation?
  * least squares: minimizes the sum of squared differences (i.e., residuals) between dependent and independent variables (or observed/predicted, or just any two variables), often without assuming a specific distribution in the errors.  This is a geometric approach.
  * Maximum likelihood estimation: finds parameter values that maximize the probability of observed data under _an assumed distribution_ in both the probabilities (e.g., Gaussian Poisson, etc.) and in errors.  So, MLE is a probabilistic approach.
  * MLE is generally more flexibile and robust when dealing with non-normal data or generalized linear models, or with complicated errors.
  * LSE and MLE provide identical estimates when errors are normally distributed.
  * Use LSE when quick, simple, standard linear regression is needed.
  * Use MLE when data is non-normal, you know or suspect a strong selection function is at play, or when you have a complex model that requires precise interpretation.
  * Use MLE when you have a lot of information about things like errors!  (It lets you use more information, so you get a better fit.)

* How do "measurement error models" work and why are they useful?
  * Useful because it's a way of systematically thinking about and approaching all of the errors that may occur as part of a observation-based science (variability in population, issues with detector/telescope, atmosphere, etc.)
  * It also lets you treat different sources of error differently (different magnitudes of error, can assume independent variable behaves in a specific way, can assume response variable has certain properties based on your physical knowledge, etc.).  Can also include, for example, both intrinsic and measurement error for a single part of the problem. (And systematic errors in measurement - offsets, biases, etc.)
* How does nonlinear model regression work differently than linear regression?
  * Generally need a decent starting guess for the right answer and then use some sort of iterative method to get the "best fit" solution.
  * The main risk is finding a local, rather than global, "best fit"
* When you are attempting to select and validate models, what are some of the things you need to take into account?
  * always remember "best fit" is not necessarily "a good fit!"
  * Use global models of success (residuals, empirical distribution functions, etc.) and closely look at plots of models vs. data (and residuals) to see if there are important details about model/data discrepancies that may point toward improvements.
  * "Nested models" are potentially useful - start with a simple model and add epicycles (for example, when modeling a plasma start assuming a single temperature and add additional complexity such as non-equilibrium ionization states)
  * "non-nested models" are also potentially useful - start with a single temperature plasma model and add additional temperatures as necessary.
  * cross-validation (for example, k-fold cross-validation) is a very useful technique for testing models.

Some points to make:

* Use least squares and weighted least-squares whenever possible
* Bootstrap error analysis is very helpful - gives you a sense of what your model variations are!
* Anscombe's Quartet (https://en.wikipedia.org/wiki/Anscombe%27s_quartet) is a really good example of why you might want to look at your data as well as just measure residuals and adjusted residuals.
  * Always remember "best fit" is not necessarily "a good fit"!

### In-class assignment

* Nonlinear regression and model validation (7.6, 7.7 of Feigelson and Babu)


## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2021: went well!  most people got the fit to work in the ICA, but didn't do the k-fold cross-validation.
