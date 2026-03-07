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

    # create magnitude bins
    mag_bins = np.arange(abs_mag_min,abs_mag_max,dM)

    # calculate number density for those magnitude bins
    number_density = 0.4*np.log(10.0) * phi*((10**(0.4*(mag_star-mag_bins)))**(alpha+1)) \
                      * np.exp(-10**(0.4*(mag_star-mag_bins)))


    '''
    Create error estimate.  We're using a very simple error estimate
    to start out, which assumes that the error is linearly
    proportional to the number density of galaxies in a given bin.
    This is completely indefensible for a real galaxy survey!
    '''
    error_bars = error_scale*0.1*number_density


    '''
    Create your own error estimates here. Galaxy surveys are typically
    limited by some combination of the volume surveyed and by the
    apparent magnitude of galaxies. More massive galaxies are both
    much brighter (and thus easier to find) and also have lower number
    density (and are thus rarer) than their low-mass counterparts,
    which are dim but numerous.

    This means that a deep (in magnitude) but volume-limited galaxy
    survey will be relatively "complete" at the low-mass end (meaning
    the low-luminosity galaxies have all been found and counted, so
    the error bars are small for those bins) but covers a small
    volume, meaning the number of high mass galaxies are small and
    thus the number density estimates are statistically limited (and
    thus the error bars are large).  A shallow but large-volume galaxy
    survey will have exactly the opposite problem - the counting of
    bright galaxies will be robust (i.e., the corresponding bins will
    have small error bars) due to the wide area of coverage, but many
    low-luminosity galaxies will be missed, meaning the corresponding
    bins will have large error bars. Astronomical surveys are
    inevitably limited in the amount of telescope time available for
    the survey, which means that tradeoffs in survey design must be
    made in order to accommodate these challenges!

    So, when choosing your own estimates for error bars, try setting
    up errors that approximate both deep, volume-limited and shallow,
    wide-field surveys.  Try also approximating a "snapshot" survey
    that is both volume- and magnituded-limited, meaning the error
    bars at both the high ahd low-luminosity ends are bad.  How do
    these choices impact the degree to which different parameters in
    the model are constrained?

    '''
    # error_bars = UNCOMMENT AND ADD YOUR CODE HERE

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
