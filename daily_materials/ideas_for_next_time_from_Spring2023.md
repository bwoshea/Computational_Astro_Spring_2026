# Ideas for next time (Spring 2023 edition)

As I'm writing this (roughly March 1, 2023), the semester has completely gone to hell and I have had to remove a bunch of stuff from the class to make it work.

So, things I absolutely want to do for next time:

1. Remove all machine learning, and replace it with some HPC stuff.  (MPI, threads, numpy, CuPy, etc.) - basically, you have your HPC application, how do you think about making it work faster?  (This may also require some discussion of the actual physical structure of GPUs).
2. Re-think the semester project.  At the moment it takes up a lot of time.  Is this the right thing to do?  I had to make it less intense for this semester due to everything that went on.


Order rubber ducks before the semester starts!


Reasources for GPU/HPC in Python:

* Carpetries lessons on GPU programming in Python:
  * GitHub: https://github.com/carpentries-incubator/lesson-gpu-programming
  * Website: https://carpentries-incubator.github.io/lesson-gpu-programming/
* Python multiprocessing library: https://docs.python.org/3/library/multiprocessing.html 
* Python threading library: https://docs.python.org/3/library/threading.html  (note: different than multiprocessing!)
* Parallel programming with NumPy and scipy: https://scipy-cookbook.readthedocs.io/items/ParallelProgramming.html 
* the Parallel Python tool: https://www.parallelpython.com/ 
* Using Numpy efficiently between processes: https://medium.com/analytics-vidhya/using-numpy-efficiently-between-processes-1bee17dcb01 
* Sharing big numpy arrays across python processes: https://luis-sena.medium.com/sharing-big-numpy-arrays-across-python-processes-abf0dc2a0ab2 
* Example of high-performance Python code (but not MPI-parallel): https://murillogroupmsu.com/sarkas-a-fast-pure-python-molecular-dynamics-code/ 
* Numba: http://numba.pydata.org/ and https://numba.readthedocs.io/en/stable/ 
* Numba for CUDA GPUs: https://numba.readthedocs.io/en/stable/cuda/index.html 
* NVIDIA pagee on GPU-accel. computing with Python: https://developer.nvidia.com/how-to-cuda-python 
* CuPy (numpy/scipy-compatible array library for GPU-accelerated computing with Python):
  * https://cupy.dev/ 
  * Basics of cupy: https://docs.cupy.dev/en/stable/user_guide/basic.html 
  * routine reference: https://docs.cupy.dev/en/latest/reference/routines.html 
  * scipy routine reference: https://docs.cupy.dev/en/latest/reference/scipy.html 
* RAPIDS GPU Data Science: https://rapids.ai/ 
* Intro to GPU programming with CUDA and Python: https://www.cherryservers.com/blog/introduction-to-gpu-programming-with-cuda-and-python 
* Materials for "High Performance Computing with Python" class, organized at CSCS on June 21-23, 2022: https://github.com/eth-cscs/PythonHPC 
* Cython (an optimising static compiler for Python): https://cython.org/ 
* High Performance Python book: https://www.amazon.com/High-Performance-Python-Performant-Programming/dp/1492055026/ref=asc_df_1492055026/ and https://www.oreilly.com/library/view/high-performance-python/9781449361747/ 
* A uniform interface to parallel processing pools that switches easily between local development and a supercomputer: https://github.com/adrn/schwimmbad 
* Python JobLib (pipelining in Python): https://joblib.readthedocs.io/en/latest/index.html 
* Generic (but very good) book on the Art of HPC: https://theartofhpc.com/ 

One thing that's very clear to me is that we need to figure out a way to teach students about the physical structure of computers.  That will help them to think through the "high performance" part of HPC.

----

Some VSCode links:

* https://code.visualstudio.com/
* Getting Started with VSCode: https://code.visualstudio.com/docs/introvideos/basics 
* Running Jupyter notebooks: https://code.visualstudio.com/docs/datascience/jupyter-notebooks 
* Debugging Jupyter notebooks: https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_debug-a-jupyter-notebook
* Debugging Python in VSCode: https://code.visualstudio.com/docs/python/debugging 
* Connecting to a remote server: https://code.visualstudio.com/docs/remote/ssh
* GitHub AI Copilot: https://github.com/features/copilot 
* ChatGPT VSCode plugin: https://github.com/mpociot/chatgpt-vscode 
* Collaboration on GitHub: https://code.visualstudio.com/docs/sourcecontrol/github 

Another debugging option:  https://docs.python.org/3/library/code.html  (code.interact()); see https://twitter.com/karpathy/status/1610822271157022720 

---

Some end-of-semester notes (written 4/30/2023)

* Despite the semester getting completely messed up, I think things went OK.  I had to throw away a bunch of material, but that's probably a blessing in some ways - the course was too heavy on hyperbolic PDEs (verging into CFD) anyway, and I should probably reshuffle the materials so the statistics part is fully half of the semester.
* It was OK to get rid of most of the hyperbolic PDE stuff, and I think that I would like to keep it that way in the future - but replace the materials with some basic parallel computing material.  Maybe just do the linear and nonlinear hyperbolic PDE days (days 1 and 2), and let the students do something else?
* I do need to go back and revisit what I ask the students to do in the PDE work.  Since I shuffled the order to put PDEs first, I accidentally removed some readings (from the beginning of Zingale's lecture notes) that the students could have really benefited from in terms of making sense of the various PDEs (the section on L1/L2/inf norms, finite volume, etc.).
* I am really struggling with what to do about the semester project.  Too much work seems to get piled up at the end of the semester.  Alternately, I can make all of the homeworks available on the very first day of the semester, tell the students what is in each assignment, and strongly urge them to work on those assignments as they go - that way they can make sure they've mastered the materials.  Another possible option is to make a bunch of smaller homework assignments, because apparently the ones I gave out this semester are taking far too much time.  (Too complex? Simply too long?  I'm not sure.)
* I could probably do the FFT stuff immediately before I do the rest of the time series analysis.  That would be more logically consistent, and also move the MCMC stuff up a bit in the semester (which would be appreciated by some of the students).  It also helps me make the point that lots of things in time series analysis are a convolution - correlation functions, FFTs, Lomb-Scargle, etc.
* I should make all of the homework assignments available from day 1, with consistent messaging about how I want the students to do the assignments (coding standards, Pylint, etc.).  The goal of doing this is to encourage them to work on the homework assignment problems immediately after we do it in class.  We should also set aside time in class to talk about the homework assignments, and I should provide solutions (from previous years of the class, using the best versions of everything to demonstrate correctness).
* **Make students summarize reading in the pre-class assignments!**  List key ideas, make three bullet points, etc.
* Some students thought I could do some more lecturing, which makes some sense.

