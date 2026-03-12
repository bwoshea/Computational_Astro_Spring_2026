# Day 15 - Parallel Computing, 1

## Goals for today's class

* Understand how the von Neumann architecture handles instructions and data
* Follow the movement of data through the memory hierarchy
* Understand how cache lines and the memory hierarchy enable vectorization
* See how to leverage NumPy's API to take advantage of vectorization

## Pre-class assignment

* Read **all pages** of this overview on the [basics of the CPU](https://www.bbc.co.uk/bitesize/guides/zws8d2p/revision/1).
* Watch [this video](https://thecrashcourse.com/courses/data-structures-crash-course-computer-science-14/) on data structures. This video is not specific to Python. The first roughly 6 minutes are the most relevant for our next class, but you may find all of it interesting and informative.
* Read the accompanying PDF on Lists and Tuples to understand how these data structures function under the hood.
* **If you've never used NumPy,** I suggest reading the [beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html).

## In-class activity details

**Plan for the day:** 

Announcements:

* These lessons are adapted from Claire's High Performance Computing for Python class (CMSE890-601), a 2 credit class she teaches every fall.
* Claire's classes start with a lecture (usually brief except for today's) and then students work on in-class assignments (Jupyter notebooks). Her pre-class assignments are light; instead, in-class assignments should be finished outside of class if necessary.

### Pre-class assignment notes

* Nothing specific; the pre-class materials are intended to prime students for the lecture.

### In-class assignment nodes

* The lecture slides are in this directory. Give this first.
* The in-class assignment cover memory hierarchy data movement for lists vs arrays and NumPy vectorization. I've also tacked on part of the following assignment where students convert a list-based 1D diffusion solver to one that uses NumPy. Removed from the original lessons are list comprehensions.

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2026: 
* Need to introduce `%%timeit` in the instructions for the Vectorization section of the in-class assignment
* I cut the section on list comprehensions but a few of the astro students are so used to using numpy arrays they don't know how to create a list full of items or do math on them
* Students got through the bulk of the workbook in class, save the Diffusion refactor
* I didn't quite set up that the creation of a NumPy array comes with some amount of overhead; the first refactor of the Diffusion section is intentionally slow both because of this reason and the quirk that iterating over a NumPy array is slower than a list. The latter is discovered by students through the course of the workbook but the former is not.