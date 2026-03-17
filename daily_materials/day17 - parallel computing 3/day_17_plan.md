# Day 17 - Parallel Computing, 3

## Goals for today's class

* Understand what "just in time" compilation is
* Anticipate data structures that Numba will struggle or fail to compile
* Identify the situations where different Numba tools are useful

## Pre-class assignment

* Watch this [video explaining JIT compilers](https://www.youtube.com/watch?v=d7KHAVaX_Rs) (content is optional after about 8 minutes)
* Read this brief [introduction to Numba](https://numba.readthedocs.io/en/stable/user/5minguide.html). Note that "broadcasting" here refers to [NumPy functionality](https://numpy.org/doc/stable/user/basics.broadcasting.html); e.g. multiplying an array by a scalar is "broadcasting" that scalar to the whole array.

## In-class activity details

**Plan for the day:** 

Announcements:

* TBD

### Pre-class assignment notes

* What should the students do for this?  (Specific discussion questions?)
* What do we want to make sure to talk about / ask about?

### In-class assignment nodes

* The lecture slides are very short. One important thing to highlight are Numba's dependence on C types (and not Python built-ins) and its use of thread vs processes (since running compiled code is not subject to the GIL).
* Students will learn about the `@jit` decorator (and it's limitations), use Numba's built in thread parallelism, and the `@vectorize` decorator which allows for the creation of custom NumPy-like functions for use on arrays. This is a really short lesson!


## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2026: 
* Notebook references using `time.perf_counter` but could use a little clearer instruction since students in this class aren't used to using it