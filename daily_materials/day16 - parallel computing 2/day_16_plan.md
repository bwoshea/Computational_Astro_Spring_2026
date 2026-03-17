# Day 16 - Parallel Computing, 2

## Goals for today's class

* Understand how multiprocessing divides work among multiple processes
* Think through the process of parallelizing a problem
* Run parallel jobs on the HPCC with SLURM

## Pre-class assignment

Next lesson we'll start working with multiple CPU cores. A common way to do this is to use *threads* - multiple streams of program execution that share memory. It's this shared memory aspect that makes threads an attractive way to run a program on multiple CPUs; however, Python's design means threads aren't as helpful as they are in other languages. This design feature is called the Global Interpreter Lock (GIL), and the following pre-class resources are intended to make you more familiar with this parallel programming roadblock.

* What is an interpreter anyway? Read this overview of [compiled vs. interpreted languages](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/). The article points out that Python can be run in compiled mode (if you've ever seen a `.pyc` file, that's compiled Python code) but this is usually reserved for imported modules.
* Watch this video [introducing the GIL](https://www.youtube.com/watch?v=XVcRQ6T9RHo).
* Read this article explaining [why the GIL is necessary](https://realpython.com/python-gil/).
* **Optional:** a recent Python Enhancement Proposal (PEP) lays out a road map for removing the GIL! If you're interested, you can read more [here](https://www.infoworld.com/article/3704248/python-moves-to-remove-the-gil-and-boost-concurrency.html). This proposal is slated to be included with Python 3.13, which is currently in the "pre-release" stage.

## In-class activity details

**Plan for the day:** 

Announcements:

* Homework 3 will be released?

### Pre-class assignment notes

* If the GIL is going away, why am I still teaching multiprocessing? Answer: removable of GIL still not mainstream, lag in packages catching up, multiprocessing's more suitable API (from the historical split)

### In-class assignment nodes

* Go over the attached slides, which also has instructions for setting up the necessary jobs on the HPCC (this is the class that really requires the HPCC)
* The lesson will have students play with the data structure returned by multiprocessing's Pool.map() function, walk them through parallelizing a Monte Carlo estimation of pi, ask them to parallelize another small program while holding their hand a little less, and then walk them through writing a SLURM script for the last of these programs.


## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2026: 

* I demo'd OnDemand in class (planned), showing how create a `.condarc` file that will let students use the class environment and launch JupyterLab. Plan on this in future.
* oops, students need to setup SSH keys or personal access tokens in order to clone github repos to the HPCC. I also had to demo SSH keys in class (unplanned) via the OnDemand terminal. I'm not sure this is great as a pre-class though, since some students may be new to the HPCC. It took time away from the in class assignment but if anticipated could be streamlined
* Students should *not* use VS Code on their desktop but instead use JupyterLab on OnDemand. There isn't time to explain how to set up/best use personal VS Code.
* some students were also unfamiliar with git from the command line so I wrote out commands on the blackboard.
* some students had also not encountered dictionaries before!
* The class environment I made did not work correctly for the assignment so students had to switch to the default environment in OnDemand...