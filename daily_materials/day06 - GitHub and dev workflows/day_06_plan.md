# Day 6 - git and open source workflows

## Goals for today's class

* Revisit git
* Learn to use GitHub to fork/branch/issue PRs/do code review
* Learn to use GitHub Actions

## Pre-class assignments

* Lots of reading about Git and GitHub

## In-class activity details

**Plan for the day:** 

Announcements:

* Nothing at the moment!

### Pre-class assignment

* Talk through their experiences - what are the key points?
  * We're going to make lists on the boards and everybody's going to talk about it.
  * break it down as "software development best practices," "version control workflows," "software testing," and "style and linting".  On the one side, put "key points".  And the other side, put "questions/discussion items". 
  * make four groups - everybody starts adding concepts/questions, then we rotate around a couple times.  Make sure to write reasonably small, as we'll need space!
* Some questions:
  * The practices we're talking about have overhead - when do we start using them?  [when the project is big enough, long-lived enough, important enough, etc...  not for some simple plotting script...]
  * What is the value of open source software in astrophysics (or science more generally)?  [make sure to talk about NSF/etc. mandates]
  * Forks vs. branches - what's the difference and why would you use one vs. the other?  (Forks = longer-lived/permanently diverged changes; branches = )
  * Linting/style: who cares?  (consistency in style helps reduce cognitive load)
  * Testing: who cares?  (Ultimately speeds up development by speeding up debugging; test-driven development is very important for lending confidence in code results.)
  * Don't forget documentation!
  * Takeaways from looking at astrophysics projects?
* By the way, Git/GitHub have VSCode plugins but I didn't use them for this assignment.  You can, though!

### In-class assignment

Goal is to actually do some of this version control stuff.

* We're not going to implement testing/linting automatically, but it is possible to do it!  (Just a little time-consuming to get it set up, so we're not going to worry about it in class today.)
* Git sometimes does weird things, but it's almost always recoverable.  Just don't panic, and don't delete anything unless you know what you're doing!  (You can always make a copy of your local repository.  `git log --graph` is your friend, too.)
* By the way, Git/GitHub have VSCode plugins but I didn't use them for this assignment.  You can, though!

Make sure to talk about it at the end!

## Instructor notes (for next time)

**Leave feedback on what happened in class today!**

2023:

I totally ignored the materials Rachel Salmon shared with me due to lack of time, and should consider incorporating them next time:

* https://docs.google.com/document/d/1xwnvPoYKbcnvtC13e7gTaRARg7O2UFKQ6DFDI1kiMco/edit
* https://escholarship.org/uc/item/6fv1s464#main

Also, **this was a really fun class, but we never even got to the in-class activity.**  We spent all of the time discussing the pre-class assignment.  That's fine, but I think I'll turn the in-class assignment into part of a homework assignment. (And maybe also have them create a unit test.)



