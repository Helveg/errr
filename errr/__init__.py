from .exception import DetailedException
from .tree import make_tree, exception

__version__ = "1.1.2"

def wrap(err_type, *args, **kwargs):
    return err_type.wrap(*args, **kwargs)
