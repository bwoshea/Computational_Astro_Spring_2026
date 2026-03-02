# Day 20 - Bayesian Stats, I

## Goals for today's class

* Talk about Bayesian statistics
* Do some examples

## Pre-class assignments

* Read several chapters of Andreon and write up questions

## In-class activity details

**Plan for the day:** 

Announcements:

* We're going to do Update #2 for the semester project!
* There IS a PCA for next time - it's short.  We'll be implementing a Bayesian MCMC in class!
* Next week is time series analysis, and the last week of class!  (One PCA for the whole week.)

### Pre-class assignment

Discuss PCA - get people to compare notes!  What are your answers to the two questions?

1.  What is the utility of the inclusion of prior and evidence probabilities?
2. Fundamentally, what is the difference between the frequentist and Bayesian approahces toward statistical inference?  How does this manifest in the way these approaches are used?

Q1 answer:  "prior" encodes what we know about the model before considering the data (useful because we almost always know omething about the data).  "evidence" or "model evidence" or "marginal likelihood" encodes our understanding of the underlying sample out of which our dataset is generated, to the extent we have it.  (This is very hard to calculate in astronomy).  Taken together, this allows us to update our beliefs based on observations, given a prior state of knowledge.

Q2 anwer:  "Frequentist" -- probability calculated in terms of a limiting case of repeated measurements (i.e., probability fundamentally related to frequency of events).  Variations are due to statistical error of measuring device, so it's meaningless to talk about "true" values - it's by definition a single, fixed value (so an extended distribution of 'truth' is undefined, but in reality ranges quantify our uncertainty of measurements).  

"Bayesian" -- probability is extended to cover degrees of certainty about statements ("reasoing with belief"), and is fundamentally related to the observer's knowledge of an event.  So, it's meaningful to say that the "true value" of a parameter or observation lies within a given range.

Bayes' theorem itself is not controversial; it's the interpretation of probability that is controversial.

### In-class assignment

Let's work out some probabilities!  Spend a bunch of time talking through Bayesian stats, priors, etc., and get them to do a couple of examples.

Suggestion: think for next time about how we might incorporate this into our MCMC code!

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2018:  Next time, find a better Bayesian stats example than galaxy redshfits - or at least change the probabilities so that not everything is 10%, as it's super-confusing.  It would also be good to start with a Bayesian example that's simpler (i.e., doesn't require new astrophysics as well as Bayesian stats to understand).  I used the medical example second this year, and should probably do it the other way around in the future!

Find a couple of extra examples and do them in class.  

Figure out how to chain together probabilities for the future.

Claire shared this - make sure to use it next time:  https://www.youtube.com/watch?v=9TDjifpGj-k

2021: went OK, didn't get to the photo-z section.  I forgot to share Claire's video - do that next time!

2023: it went great and we got through everything.  I think the students really liked it.  We used the slides from last time, which were VERY helpful.  I did notice that slide #10 has a typo - it should be p(data fit to high-z model)*p(low-z galaxies) in the second term in the denominator.  Fix that for next time!
