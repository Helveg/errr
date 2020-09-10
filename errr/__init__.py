from .exception import DetailedException
from .tree import make_tree, exception

__version__ = "0.1.0"

def wrap(type, e, *details, prepend=None, append=None):
    interpolator = type("", *details)
    msg = ""
    if prepend is not None:
        msg = interpolator.interpolate(prepend)
    msg += (str(e) or "")
    if append is not None:
        msg = interpolator.interpolate(append)
    err = type(msg, *details)
    err.__traceback__ = e.__traceback__
    raise err from None
