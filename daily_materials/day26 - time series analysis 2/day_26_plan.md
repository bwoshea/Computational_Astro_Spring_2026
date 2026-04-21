# Day 26 - time series analysis 2

## Goals for today's class

* Learn about time series analysis, and think about its applications in astronomy (part 2)

## Pre-class assignments

* None!

## In-class activity details

**Plan for the day:** Time series analysis 

Announcements:

* We're doing a semester wrap-up activity on the last day of class!  Please take a bit of time (no more than an hour!) to go back through the materials from the semester and think about what you've learned.
* This is the last week of class!  All assignments are due at the end of next week, on Friday.  This is a **firm deadline** - I need time to grade everything!
* Also talk about final exam session/presentations.  What is the plan?
  * Meeting is on Friday of finals week at 7:45 a.m.
  * I have no control over the time, I'm sorry!
  * Presentations should be 7-8 minutes, plus 2 minutes for Q\&A.
  * Final code, etc. is due that evening along with everything else.


### Pre-class assignment

None!

### In-class assignment

Implement cross-correlation and self-correlation function (it's the same thing, so write it in a general way!)

Try this on a bunch of different signals (I generated a bunch).  Things to emphasize:

* Scipy's "correlate" does indexing in a way that is backwards from what we're doing, so if you want to compare the correlations between the two you have to reverse the order of one of the arrays.
* Signals with different periods have complicated correlation relationships.  You can see things like beat frequencies.
* Signals with different shapes have non-sinusoidal correlation function shapes (typically much "peakier").  Ask about delta functions and what that would look like for a correlation function compared to, say, a sine wave.

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2018: The project update roundtable took about fifteen minutes, and the actual assignment took between 15 and 45 minutes, depending on the person.  This was NOT a difficult assignment - I could easily have added a couple points to it.  For next time, add something to make it more challenging!

2021: I decided to leave it easy, because it's been a heck of a semester and I felt bad for the students.  Tell students who finished early to get started on their semester wrap-up.  Next time, add signals of different wavelengths, different shapes, etc. (square waves, triangle waves, things with different periods) and ask the students to talk about the differences.

2023: This day went pretty well.  Given that we talked about correlation functions today, I think we could probably swap the previous day of time series in-class assignment (which focused on Lomb-Scargle) with this one, and be just fine.  Also, definitely add some extra signals for next time - really hit on the point that signals that have no correlation at all should have very low-amplitude correlation numbers (nothing is exactly zero, but a number of around 1 indicates a very high correlation).  Maybe come up with some signals that have very low correlation because they have very different periods, and then some signals that have very different shapes (infrequent Gaussian pulses, maybe?) so the correlation function is not particularly sinusoidal.

2026: split the semester wrap-up off to another day.  Implemented a bunch of new signals.  Some things for next time:

* Scipy's "correlate" does indexing in a way that is backwards from what we're doing, so if you want to compare the correlations between the two you have to reverse the order of one of the arrays.  Make a note about this in the notebook!
* Add a very delta function-y pulse to the set of signals, which should result in something interesting in terms of the shape of the correlation function (comparing it to the top hat, for example).
* 