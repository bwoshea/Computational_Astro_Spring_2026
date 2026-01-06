# Day 07 - initial value ODEs

## Goals for today's class

* Learn about initial value ODEs and the methods that are used to solve them
* Understand the merits of different integraters (i.e., symplectic integrators) and why one might choose one over another based on the properties of the system that one wishes to maintain (i.e., conservation of energy vs. absolute numerical accuracy, etc.)
* Learn about adaptive stepping in ODE integraters and how this can save a tremendous amount of computational time

## Pre-class assignments

* Read the initial value ODE sections of Newman, including adaptive stepping.  Read wikipedia pages on Euler-Cromer and midpoint methods.
* Implement a couple of different methods for ODE integration and compare their properties regarding spring position and energy conservation.

## In-class activity details

**Plan for the day:** 

Announcements:

* Explain the plan for the next few weeks: this week is ODEs, and then we'll move on to various PDEs followed by computational fluid dynamics.
* The first homework will come out in a week or so!

### Pre-class assignment

* Get students to talk in small groups about their experiences with the pre-class assignment, and solicit questions about things that are unclear from the readings.  Ask the students to compare their plots, and try to understand why they behave the way that they do.
* Some discussion questions to ask the students:
  * Approximately how long did the pre-class assignment take?
  * Based on the reading, why do you think there is such a profusion of methods for solving initial-value ODEs?  [solving different problems and with different levels of precision; attempting to conserve different quantities/minimize different types of error; etc.]
  * What's the point of adaptive time-stepping (or, really, adaptive step sizes) in ODE integraters?  [Save computational cost/take fewer time steps]
  * Get the students to discuss their plots: hopefully they come up with the conclusion that Euler is terrible compared to leapfrog, and that accuracy gets better as step size gets smaller.  (What should happen as step sizes get smaller and smaller?  In principle, at some point floating-point precision becomes an issue and everything should get really ugly, as we saw in an earlier class with numerical differentiation.  However, it's somewhat irrelevant because when one is taking exceedingly small time steps you'll never get the ODE (or set of ODEs) to evolve to where you want them to be!  (This is an argument for higher-order methods, so you can take longer steps.) )  Also, how did the students choose to display their plots?  The instructions were somewhat vague; ask people to share what they came up with.  What makes the most sense?

### In-class assignment

Goal is to get the students to show how energy conservation behaves as a function of step size for the various methods, on a single plot - while facilitating, encourage the students to make a log-log plot of error vs. step size (i.e., in the way that we usually do it).

Floating point operation calculation: get people to think about what a single step could cost in terms of arithmetic operations. This may require a bit of discussion: what is a floating-point operation?  How do you count them in an algorithm?  And then, how many steps do you have to take?  (So how do you get the total number of operations?)

For a given level of accuracy, which method is most computationally efficient to solve the problem?

For the "maintain energy to a give level of accuracy," we're going for adaptive time steps.  Give a highly elliptical orbit as an example, which is similar in some ways to the pre-class spring example, but has a much wider variety of accelerations and velocities.  How might you develop a method that can adaptively decrease AND increase the time step?  When you have a situation like that, how much efficiency might be gained by an adaptive time step?  (There is a section of the reading that talks about this - it's worth emphasizing the algorithm presented!)

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

**2018 notes** 

### Pre-class assignment
- overall went well and was well received
- on average 2-3 hours workload (reading + coding)
- about 10-15 minutes for a discussion in small groups (2-3 students)
- afterwards about 5-10 minutes discussion of results in class
- one results that came up (not mentioned in the plan yet as a point for discussion) is that some students had "step functions" in their error vs. dt plots. [their N\*dt didn't exactly end up at tend so that there was an additional error by not comparing the exact same times]

### In-class assignment
- overall, no student was able to address all points in the in-class assignment
- approx. 50% finished all implementations correctly, but just barely finished to plot all the results together
- my impression is that a lot of time was spent on identifying small 'bug' in their algorithm logic [I was kind of suprised given that RK4 for two eqns is explicitly written out as python code in the parts they read previous to class] - Need to be confirmed -> I asked students to report their issue with handing in the answers to the ICA
- instructions for use 'midpoint' wasn't clear, as there's an explicit and implicit midpoint rule on Wikipedia, and a midpoint (RK2) and modified midpoint in the Newman book
- students observed small phase shifts in their solutions [didn't take care to have matching time and pos/velocity arrays]
- some student notebooks were enormous (wrt lines of code, also for the PCA). [in future, we should emphasize more reusing code and discourage copy and pasting as I tried in class]
- finished class with 
  - discussing a log-log error plot, and how fitting/plotting expected straight lines illustratd the order of the algorithm in practice
  - conceptually how counting flops works and how the total computational cost an different algorithms relates to order 
- Another comment after giving this more thought: Given the 'bugs' in the students' implementations, one could either reduce the number of algorithms to implement or provide a more guided structure. Philipp is in favor of providing a e.g. a notebook that has an overall skeleton in order to let the students focus on implementing the algorthms  (with fewer lines of code). Alternatively (or in addition),  the PCA could be rephrased so that reusable/extensible code has to be turned in (and they write their skeleton themselves) e.g., 'Make sure to write extensible code, i.e., to implement Euler-Cromer you should not add more than 10 lines of code (incl. plotting) total'

**2021 notes**

Seems to have gone better.  The in-class assignment is still too long; need to think about how to do that.  I think maybe we want to go with a notebook for next time, or reduce the number of codes...

**2023 notes** 

I didnt' make any changes from 2021 due to lack of time, and we did not finish the in-class assignment, though we were pretty close.  Next time I should scaffold it a bit more - maybe give them some skeleton code to work with that takes care of the plotting?
