import os
import typing
import progressbar
import ctypes 
from time import sleep
from progressbar.progressbar import ProgressBar
import random

class Pakt_Init: # putting it in class because oop autism
    # white space because clean code
    @staticmethod # static method because this shouldn't be in a class, but read above lines
    def pakt_init(name: typing.Optional[str], boot: bool = True) -> None: # setting parameters and return types
        if not isinstance(name, str): # checking if the name provided is a string or not, type hinting doesn't raise errors iirc
            raise TypeError("`Name` has to be a string.") # raising error if they messed up
        # white space because clean code
        if not isinstance(boot, bool): # checking if boot is a boolean or not
            raise TypeError("`Boot` has to be a boolean.") # raising error
        # white space because clean code
        os.system("clear") # clearing screen
        # more white space because clean code
        print("Initializing system")
        # more white space because clean code
        pakt_init_progress_bar = ProgressBar(maxval=100) # creating instance of `ProgressBar`
        pakt_init_progress_bar.start() # starting instance of `ProgressBar`
        # more white space because clean code 
        for i in range(0, 100): # creating loop to iterate over i
            if not isinstance(i, int): # type checking
                raise TypeError("Iterator variable `i` must be an integer in this context.") # raising error if type check fails
            # more white space because clean code
            pakt_init_progress_bar.update(i+1) # updating progress bar
            sleep(0.025)
            if random.randint(0, 100) < 75: # generate random number
                sleep(2) # do important init shit here
        pakt_init_progress_bar.finish() # finish progress bar (same with ur mother)
        # more white space because clean code 
        print("Pakt Init is done initializing the system.") # we are done
        ctypes.string_at(0) # segfault python because FUCK YOU
# more white space because clean code 
# more white space because clean code         
pakt_init_object = Pakt_Init() # create pakt init object with name explicitly denoting it's status as such
# more white space because clean code 
pakt_init_object.pakt_init("penis", True) # run pakt init with parameters which absolutely are important