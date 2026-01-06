# Notes from Spring 2021 (and ideas for next time)

I taught class in Spring 2021 (1) during COVID-19 and (2) as an overload.  Several compromises had to be made:

* We had to shorten the semester by a week, so i got rid of the machine learning classes (last 2 days)
* The students were utterly burnt out, so I canceled a class during our not-really-spring-break, and ended up cutting the third day of fluid dynamics.
* I gave the students a "only do pre-class and in-class assignments, and get up to a 3.5; do everything and you can get a 4.0" deal.  Of the 8 in the class, 6 took the first option and 2 took the second option.  [This is not something I'd want to do in the future, that was only a pandemic thing.]
* I ran out of time to make updates to the class; basically nothing from last time got changed except for the removal of the machine learning materials and one section from the fluid dynamics section (which was originally Philipp Grete's, and had to be adapted to remove Toro from the schedule).

Things to do:

* If I'm going to keep using Zingale's notes (which I like!) I need to rearrange the differential equation section to do hyperbolic first, otherwise some of the later stuff doesn't make that much sense.
* Maybe turn multigrid into a homework assignment?  At the very least I need to find a better reference for it, because the tutorial materials are not great.


Make sure to point students toward useful resources for the future.  This might be an interesting way to add value - website with lots of references.

* SciPy cookbook:  https://scipy-cookbook.readthedocs.io/index.html (great example: signal smoothing: https://scipy-cookbook.readthedocs.io/items/SignalSmooth.html)
* Awesome plasma physics homework assignment idea:  https://medium.com/swlh/create-your-own-plasma-pic-simulation-with-python-39145c66578b  (and git repo at https://github.com/pmocz/pic-python, and some more ideas at https://philip-mocz.medium.com/)
* Christoph Federrath astrophysical gas dynamics class web page: https://www.mso.anu.edu.au/~chfeder/teaching/astr_4012_8002/astr_4012_8002.html 
* REBOUND n-body code: https://rebound.readthedocs.io/en/latest/ (as an example of high-order n-body codes)
* Also look at this (for n-body integrators):  https://arxiv.org/abs/2104.06413 

Look at LeVeque Riemann Problem / Jupyter notebook books:

* page on book: http://www.clawpack.org/riemann_book/
* SIAM page to order it:  https://epubs.siam.org/doi/book/10.1137/1.9781611976212
* github repo of notebooks:  https://github.com/clawpack/riemann_book/tree/FA16

Look at the students' semester wrap-ups - there were some useful suggestions in there.  In particular look at ideas about in-class assignments - a lot of them are really hard to accomplish in the time allotted.  Maybe give them more scaffolded code, and only have them implement a few lines at a time?

For day 1 - Wilson et al. have a new paper:  https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510

