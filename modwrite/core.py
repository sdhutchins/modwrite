# -*- coding: utf-8 -*-
import os


class Modwrite():
    """Write template module files based on directory structure."""
    
    def __init__(self):
        pass
    
    
    def get_software_list(self, directory):
        """Get software list from input directory."""
        dirs = [d for d in os.listdir(directory) if
                os.path.isdir(os.path.join(directory, d))]
        return dirs
        