'''
This file contains the  code required for one of the homework problems.
The doc strings for each of the two functions describe what they do.
'''

if "np" not in dir():
    import numpy as np

def luminosity_function(nbins=10, error_scale=1,
                        abs_mag_min=-28, abs_mag_max=-15,
                        phi=1.2e-2, mag_star=-23.0, alpha=-1.25):
    '''
    Calculates a synthetic observed galaxy luminosity function in comoving number
    density of galaxies per magnitude bin, including errors.  Recall that in magnitudes,
    the smaller (i.e., more negative) the number, the brighter the galaxy!

    Inputs:
      nbins = number of bins in the returned arrays

      error_scale = controls magnitude of errors

      abs_mag_min = minimum absolute magnitude returned (change with caution)

      abs_mag_max = maximum absolute magnitude returned (change with caution)

      phi = normalization of comoving galaxy number density

      mag_star = bolometric magnitude corresponding to L* (pivot point)

      alpha = slope of luminosity function for magnitudes > mag_star (lower luminosity galaxies)

    Outputs:
      mag_bins, number_density, error_bars

      mag_bins = center of bins in absolute bolometric magnitude

      number_density = comoving number density of galaxies in that magnitude bin

      error_bars = Standard deviation of error in number_density in that magnitude
    '''

    # calculate width of magnitude bin
    dM = (abs_mag_max-abs_mag_min)/nbins

    # calculate magnitude bins
    mag_bins = np.arange(abs_mag_min,abs_mag_max,dM)

    # calculate number density for those magnitude bins
    number_density = 0.4*np.log(10.0) * phi*((10**(0.4*(mag_star-mag_bins)))**(alpha+1)) \
                      * np.exp(-10**(0.4*(mag_star-mag_bins)))

    # calculate error bars.  Start out simply.
    error_bars = error_scale*0.1*number_density

    # The following lines are meant to modify the error estimates so that brighter galaxies
    # (i.e., those with more negative magnitudes) have larger error bars proportionally to their
    # values.  This is because there are fewer galaxies in those bins so there are large Poisson
    # errors.  Be very careful changing this!

    ######  DO NOT USE THIS IT IS BROKEN AND GARBAGE ########
    # error_bars *= np.abs(1.0+np.random.normal(loc=0.0,scale=.2))
    # error_pivot_point=mag_star+4.0
    # error_modifier = 10**(np.abs((mag_bins/error_pivot_point))**2-1)
    # error_bars *= error_modifier

    return mag_bins, number_density, error_bars

def schechter_function(magnitude_bins, phi, mag_star, alpha):
    '''
    Calculates galaxy luminosity function in comoving number
    density of galaxies per magnitude bin.  Recall that in magnitudes, the
    smaller (i.e., more negative) the number, the brighter the galaxy.

    Inputs:
      magnitude_bins = a numpy array with the centers of the magnitude bins you
                       wish to retrieve the comoving number density for.

      phi = normalization of comoving galaxy number density

      mag_star = bolometric magnitude corresponding to L* (pivot point)

      alpha = slope of luminosity function for magnitudes > mag_star (lower luminosity galaxies)

    Outputs:

      number_density = a numpy array of comoving number densities with the same size
                       as the input magnitude_bins array
    '''
    number_density = 0.4*np.log(10.0) * phi*((10**(0.4*(mag_star-magnitude_bins)))**(alpha+1)) \
                      * np.exp(-10**(0.4*(mag_star-magnitude_bins)))

    return number_density
