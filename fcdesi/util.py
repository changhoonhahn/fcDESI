'''

utility functions 

'''
import os
import sys
import numpy as np


def check_env(): 
    if os.environ.get('FCDESI_DIR') is None: 
        raise ValueError("set $FCDESI_DIR in bashrc file!") 
    return None


def dat_dir(): 
    ''' dat directory is symlinked to a local path where the data files are located
    '''
    return os.environ.get('FCDESI_DIR') 


def code_dir(): 
    ''' local github repo directory 
    '''
    return os.environ.get('FCDESI_CODEDIR')


def fig_dir(): 
    ''' directory for figures 
    '''
    return code_dir()+'figs/'


def doc_dir(): 
    ''' directory for paper related stuff 
    '''
    return code_dir()+'doc/'
