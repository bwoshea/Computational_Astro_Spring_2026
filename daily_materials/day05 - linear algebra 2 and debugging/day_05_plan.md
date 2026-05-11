# Day 5 - numerical linear algebra, 2 (plus debugging!)

## Goals for today's class

* Learn about gradient descent methods and their relative merits
* Learn about eigenvalues and eigenvectors and how to solve for them
* Learn about debugging, ways to do it, why it's important to think about how to write code to facilitate debugging.

## Pre-class assignments

* Some reading on numerical linear algebra and debugging
* Implement a multivariable secant method
* Do an example with a debugger (PDB or IPDB)

## In-class activity details

**Plan for the day:** 

Announcements:

* Reminder: everybody should come up with some questions!
* Talk about the assignments for next week - software development, initial value problems with ODEs

### Pre-class assignment

* Talk through their experiences - who got the NLA thing to work?  Who didn't?  What problems do we think we might have with multi-d gradient descent?
* What were their debugging experiences?  In what ways will the debugging methods be helpful?
* What additional debugging techniques have people found to be helpful?  Are there specific IDEs or text editors that have built-in debugging tools?  (Beyond Visual Studio Code and JupyterLab, which we talked about in the PCA)
* What are eigenvalues and eigenvectors, and why do we care?
  * Eigenvectors are special directions in a system that do not rotate during a linear transformation - they only stretch/shring.  They reveal the fundamental structure or "main axes" of a physical system (e.g., key directions like normal modes or rotational axes)
  * Eigenvalues are the factor by which these directions are scaled.
  * Together they reveal fundamental structures of a physical system.
  * Examples: in mechanics, eigenvectors represent normal modes of a system (vibration patterns that vibrate at a single frequency).  In rotation, eigenvectors of a moment of inertia matrix represent the principle axes around which a solid body rotates stably.  In quantum  mechanics, eigenvectors represent possible states of a system, and eigenvalues indicate the measurable values of properties in those states (e.g., energies)

### In-class assignment

Linear algebra:

* Talk about getting numerical eigenvalues and eigenvectors: the whole idea is that we're rotating our basis space around so that we can make getting the eigenvalues simple.  (Using my written notes.)
* Spend some time discussing why numerical linear algebra is computationally expensive, and why it's hard to come up with faster algorithms.  (N^3 is the naive algorithm; N^2.4 is about as good as it gets currently.)
* Talk a little bit about why GPUs are often good for this, including reduced/mixed precision arithmetic; and Google TensorFlow, etc.

Debugging:

* Give them ICA 5 and have them work through it in small groups.
* The solutions are in working\_code.py.  Give some advice about how to do it!

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2018:

* Give students experience writing unit tests, maybe?
* Come up with a more extensive example of debugging to work on in class.
* There really isn't an in-class activity - it's mostly lecturing and discussion.  There isn't coding, because I couldn't come up with an eigenvalue/eigenvector or matrix inversion problem that was both interesting and doable in a short time frame.  Can I come up with something for them to do in 

2021: 

* need to revise the pre-class assignment for next time to make it clear that they don't have to dive into Section 6.3 of Newman, because it's VERY long.
* Think about having them write some unit tests for their first homework assignment?

2026:

* Think about including the included new PDF (6-Debugging.pdf), which is from a Stanford course of some sort.  It's pretty good.  Maybe just link to the version that's on the web instead?  (In the pre-class assignment.)
* Consider including wikipedia page on eigenvalues and eigenvectors - https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors .  This comes up as a point of "I can calculate it but don't understand it"
* 
