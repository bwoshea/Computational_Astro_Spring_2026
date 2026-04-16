# Day 26 - time series analysis 2

## Goals for today's class

* Learn about time series analysis, and think about its applications in astronomy (part 2)
* Talk about (and do!) semester wrapup assignment

## Pre-class assignments

* Semester wrap-up assignment (due the night before)

## In-class activity details

**Plan for the day:** Semester wrap-up, then time series analysis 

Announcements:

* This is the last week of class!  All assignments are due at the end of next week, on Friday.  This is a **firm deadline** - I need time to grade everything!
* Also talk about final exam session/presentations.  What is the plan?
  * Meeting is on Friday of finals week at 7:45 a.m.
  * I have no control over the time, I'm sorry!
  * Presentations should be 7-8 minutes, plus 2 minutes for Q\&A.
  * Final code, etc. is due that evening along with everything else.



* Remind people about final exam session/presentations.  What is the plan?

### Pre-class assignment

* Semester wrap-up activity.
  * The idea is to get you to synthesize what you've learned this semester and reflect a bit about how it'll be useful to you in the future.
  * See if I can get groups to identify and agree on big themes.
  * How do sub-topics fit into the big themes?

### In-class assignment

**NOTE: This is not actually what happened in the in-class assignment!**
Talk about Lomb-Scargle periodogram: remind people that it's useful for non-uniformly sampled data!  Also ask if you can do something analogous to it for other types of functions (i.e., non-sinusoidal but repetitive functions).  The answer is YES, it's just a different basis function.

**This is the part that actually happened in the in-class assignment:**
Implement cross-correlation and self-correlation function (it's the same thing, so write it in a general way!)

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2018: The project update roundtable took about fifteen minutes, and the actual assignment took between 15 and 45 minutes, depending on the person.  This was NOT a difficult assignment - I could easily have added a couple points to it.  For next time, add something to make it more challenging!

2021: I decided to leave it easy, because it's been a heck of a semester and I felt bad for the students.  Tell students who finished early to get started on their semester wrap-up.  Next time, add signals of different wavelengths, different shapes, etc. (square waves, triangle waves, things with different periods) and ask the students to talk about the differences.

2023: This day went pretty well.  Given that we talked about correlation functions today, I think we could probably swap the previous day of time series in-class assignment (which focused on Lomb-Scargle) with this one, and be just fine.  Also, definitely add some extra signals for next time - really hit on the point that signals that have no correlation at all should have very low-amplitude correlation numbers (nothing is exactly zero, but a number of around 1 indicates a very high correlation).  Maybe come up with some signals that have very low correlation because they have very different periods, and then some signals that have very different shapes (infrequent Gaussian pulses, maybe?) so the correlation function is not particularly sinusoidal.