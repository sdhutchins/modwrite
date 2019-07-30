# -*- coding: utf-8 -*-
import os
import sys


class Modwrite(object):
    """Write template module files based on directory structure."""

    def __init__(self):
        pass

    def get_software_list(self, directory=None):
        """Get software list from input directory.

        Args:
            directory(str): The directory of the software. Default is None.

        Returns:
            A list of directories.
        """

        if 'linux' or 'mac' in sys.platform and not directory:
            directory = '/usr/local/apps'
        dirs = [d for d in os.listdir(directory) if
                os.path.isdir(os.path.join(directory, d))]
        return dirs

    def write_module(self, filename, language="tcl"):
        """Write the module file in the language of preference.

        Args:
            language(str): The language to write the module file in (lua or
            tcl).
            filename(str): The name of the module file.
        """
        languages = ["tcl", "lua"]
        if language not in languages:
            raise ValueError('Incorrect language chosen.')

        file_contents = ""

        with open(filename, "w") as modfile:
            modfile.write(file_contents)
            modfile.close()

    def create_module_dir(self, path):
        """Create the directory for module files.

        Args:
            path:
        """
        pass

    def make_temp_modules(self, software_path, module_path, language):
        """Make temporary module files for all software.

        Args:
            software_path:
            module_path:
            language:
        """
        pass
