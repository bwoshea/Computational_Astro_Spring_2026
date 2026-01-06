# Day 08 - boundary value ODEs

## Goals for today's class

* Learn about boundary value ODEs and the methods used to solve them (primarily the shooting method)

## Pre-class assignments

* Read about and implement the shooting method

## In-class activity details

**Plan for the day:** 

Announcements:

* We need to find a time to have a makeup class, since I was sick.  (If possible!)  Please fill out the Doodle poll I shared!
* Homework 1 is out - questions?  (Discuss)

### Pre-class assignment

Discussion: what problems did people have with implementing a specific version of the shooting method?

Have the students talk me through making a flowchart of what the shooting method is actually supposed to do!  (This is a little confusing.)

What problems did they have with the SciPy version?  (It's tricky to use.)

**Share my PCA solutions with them!**

Note that BVP ODEs are used to solve the [Sturm-Liouville](https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_theory) problem.  One example of this is the time-independent Schodinger equation.  Another example would be time-independent wave solutions in general - i.e., standing-wave type problems.

Other methods for BVP ODEs: there are discrete variable methods that are analogous to the methods we use to solve elliptic PDEs, which are basically relaxation methods.  There are also other methods that create approximate solutions as a set of basis functions to solve it (polynomials, splines, trig functions, etc.).  Also Galerkin methods, which are another interesting minimization method.  Look in the `supp_materials` directory for some information I found online.



### In-class assignment

Work in small groups to think through and create a general version of the shooting method.  Some considerations:

* Does it matter if it's f(x) vs. f'(x) on both sides or just one side?  (If you have two derivatives you have a floating constant, so the solution is not unique; that's not true for other combinations.  If you have just values on LHS or RHS it's not a boundary value problem, it's an IVP, and it's boring in this context.)
* Make a flowchart: where in the secant method-based solution to this do you have to make a choice based on what information is retained?

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

Fall 2018:

This went OK; I need to actually have a worked solution to the SciPy version!  I should also start by having the students work through the logic of the shooting method in the general sense, since we talked through how the secant method worked for the pre-class assignment (i.e., I lectured about it a bit) but never forced them to diagram the code.  Overall today went well but was not amazing.

Spring 2021:

Kind of a dumpster fire. I ended up giving the students the worked solution for SciPy, heavily docunented (how in the PCA directory).  Students really struggled with the in-class assignment, because they had a lot of problems with the boundary conditions.  I think I need to have them do a flowchart first - draw pictures, etc., and diagram the code!
