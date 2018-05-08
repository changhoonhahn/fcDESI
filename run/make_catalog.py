'''
'''
import h5py 
import numpy as np 
from astropy.io import fits 

from fcdesi import util as UT 


def fits2h5py(name_fits):
    ''' given some fits file with data in a table, save to an 
    hdf5 file with minimal data organizational structure. All the 
    columns in the fits file will be saved as the highest level 
    datasets
    '''
    f_fits = fits.open(name_fits) 
    fits_header = f_fits[0].header 

    name_hdf5 = name_fits.replace('.fits', '.hdf5') 
    f_hdf5 = h5py.File(name_hdf5, 'w') 

    if fits_header is not None: 
        # save header info as meta data 
        for k in fits_header.keys(): # this needs to be checked for a 
            # fits file with a header
            f_hdf5.attrs[k] = fits_header[k]
    
    fits_data = f_fits[1].data
    for name in fits_data.names: # for all the names
        f_hdf5.create_dataset(name.lower(), data=fits_data.field(name))          

    f_hdf5.close() 
    return None 


if __name__=="__main__": 
    something
