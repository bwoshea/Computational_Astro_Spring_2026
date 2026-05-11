# Day 25 - time series analysis, 1

## Goals for today's class

* Learn about time series analysis, and think about its applications in astronomy (part 1)

## Pre-class assignments

* Chapter 11 of Feigelson
* VanderPlas "Understanding the Lomb-Scargle periodogram"
* notebook full of exercises

## In-class activity details

**Plan for the day:** 

Announcements:

* Next week is the last week of class!
* There will not be a PCA for next Tuesday; there will be a SHORT one for next Thursday (due Wednesday night, the night before the last day of class).  The goal of that PCA is to synthesize what you've done over the semester.  The wrapup assignment is VERY short, and we'll spend a bit of time on it in class.  Late submissions are not going to be accepted.
* I'm grading this weekend, starting Saturday morning.  All assignments (including the PCA and ICA for today's class) are due by the end of tomorrow (Friday, April 17th).

Key points:

* This is one of those chapters that is really important, but arguably more important as a reference than as a textbook!
* Time series analysis is widely used in astronomy
* Sometimes FFTS are not availabale to us (if the data is irregularly spaced).  Also, there are things that we want to do that can't easily reduce to FFTS!
* "(Almost) everything when we're doing time series is a convolution, and all convolutions are correlation functions". FFTs are a convolution between sin/cosines and a signal; autororrelations are a convolution between a signal and itself; cross-correlations are a convolution between a signal and another signal; the Lomb-Scargle periodogram is a convolution like a FFT as well, just done in a different way.


### Pre-class assignment

* break people up into groups

Some general questions:

* Why is time series analysis so important in astronomy?  [comes up everywhere]
* Why is it hard?
* Why do we filter data?  What are some of the main techniques?
* Autocorrelation - what is it for?  [meant for you to calculate a corellelogram (ACK(k) for many k)]
  * how does this compare to the FFT?
  * How about the structure function?

### In-class assignment

Lomb-Scargle periodogram!

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2018: Things went quite well today.  Don't make major changes.  note, however, there there were some typos in the Lomb-Scargle periodogram in my notes - need to make sure to update that stuff!

2021: Great discussion, we never actually made it to the in-class assignment.  Students seemed to like it.  For next year, make sure to have solutions to the ACF and also for the structure function.

2023: A key point to make is is "everything is a convolution, and all convolutions are correlation functions" (well, not everything, but many things).  FFTs are a convolution between sin/cosines and a signal; autororrelations are a convolution between a signal and itself; cross-correlations are a convolution between a signal and another signal; the Lomb-Scargle periodogram is a convolution as well, just done in a different way.

2026: **I need to create solutions for this class (and the next class)** - students really needed it.