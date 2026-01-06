## Talk conceptually about MUSCL-Hancock

## PCA questions

- In how far are the Euler equations different from the linear advection equation and Burgers equation?
  - multiple variables, system has multiple characteristics

- In how far does the overall algorithm differ from what we've used so far for solving hyperbolic PDEs?
  - U_L, U_R, and Delta_i "I don't understand conceptually what these variables are so I don't really understand why we determine the flux in the way that we do."
  - multiple variables
  - data reconstruction
  - as before: limiting
  - as before: calc dt (but how is this different now)
  - actually solving a riemann problem (HLL has two wave configuration)
  

- Given that you have left and right hand side quantities in (Eq 14.34), why do you need (Eq 14.35) before calling the Riemann solver?
  - I don't know. I don't understand the difference between U_L and U_R and their barred counterparts so I'm not really sure what eq (14.34) is

## Student questions
- Is there any need to enfore the constraint of the EOS for every time step or is it sufficient to do this only at initialization due to the formulation of the Euler equations?
- What are the "star regions" and "star states"? Are they the regions/states in a rarefaction wave?
- Conceptually what is the difference between a two-wave model and a three wave model? What are the waves? Is this important to understand for implementing the algorithms or to know what algorithm is appropriate?
- What do the barred quantities (U_L, U_R, and Delta_i) mean and how are they different than their non-barred counterparts?
- Do U_L and U_R need updates every timestep?
- How is the getFlux function different from the Riemann solver?
- Difference detla_i and Delta_i_bar
- with respect to getting a primitive pressure from our conserved energy, I am still unsure how we will convert between total energy and specific energy used in our equation of state.


## Eqns
- EOS: (1.18)
- getFlux: (4.1)
- getslope (14.44) 
- riemann (little more involved than people think, 10.21, 10.49, 10.50, 10.51
- how to calc wave speeds?
- remember dt (incl c_s 14.4., 14.5)
- main loop 14.33, 14.34, 14.35, 14.3 (cons update)

## MUSCL-Hancock
- dt
- reconstruction (piecewise linear to interfaces, so called boundary extrapolated values)
- potentially limiting
- evol. of BEV by 0.5dt
- get fluxes by solving Riemann values with half evolved quantities
- make a full time updated with those fluxes
