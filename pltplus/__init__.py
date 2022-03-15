from matplotlib.pyplot import *

def set_size(size):
    """Set the current default figure size."""
    rcParams["figure.figsize"] = size
    
    
def publish(filename, fig=None):
    all_artists.append(fig.get_children())