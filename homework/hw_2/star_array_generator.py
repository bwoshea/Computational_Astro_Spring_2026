
def make_star_array(Ngrid=103,Nstars=1,Lbox=1.0,Mstar = 1.0):
    '''
    Returns 3D, cubic numpy array containing densities in CGS units.  Function call is:

    make_star_array(Ngrid, Nstars,Lbox,Mstar)

    Arguments are:

    Ngrid = size of one dimension of the grid (integer; should be an odd number)

    Nstars = number of stars (integer)

    Lbox = Length of one side of box in parsecs

    Mstar = mass of a single star in solar masses
    
    '''
    import numpy as np
    
    # "stellar density" - Mstar / V_cell in CGS units
    rho_star = Mstar*1.989e33/(Lbox/float(Ngrid-2)*3.0857e+18)**3

    # this is the array that has a single star at the center
    single_star_array = np.zeros([Ngrid,Ngrid,Ngrid])

    # this is the array that has Nstars stars scattered randomly
    many_star_array = np.zeros([Ngrid,Ngrid,Ngrid])

    if Nstars==1:
        # get the center cell using integer division 
        cen = Ngrid // 2

        # make array with a single star
        single_star_array[cen,cen,cen] += rho_star

        return single_star_array
    else:
        # set random seed so result is reproducible
        np.random.seed(8675309)

        # loop over many_star_array and distribute stars 
        # randomly, but not too close to the edge.
        for i in range(Nstars):
            many_star_array[np.random.randint(10,Ngrid-10),
                                np.random.randint(10,Ngrid-10),
                                np.random.randint(10,Ngrid-10)] += rho_star

        return many_star_array
