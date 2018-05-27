import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

# from . import albums_tags
# from . import albums
# from . import images_tags
# from . import images
# from . import tags
# from . import *
# from . import modelsHelper

from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

from . import modelsHelper
modelsHelper.Base.metadata.create_all(modelsHelper.ENGINE)
