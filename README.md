# errr
Elegantly create detailed exceptions in Python.


```python
>>> import errr
>>> class MyException(errr.DetailedException, list_detailts=True, details=["cause", "type"]):
...  pass
...
>>> raise MyException("The backend server crashed", "backend", "crash")
__main__.MyException: The backend server crashed

Details:
 ˪cause: backend
 ˪type: crash
```

You can also create a large semantic tree of exceptions using the `make_tree` function,
listing exceptions as keyword arguments using the `errr.exception` factory method. The
`make_tree` method executes these recursive factories to produce your exceptions. Nesting
these factory methods will make the resultant exceptions inherit from eachother. All of
the produced exceptions are then flat injected into the given module dictionary
(typically) this should be `globals()` but you can inject into other modules using
`sys.modules["name"].__dict__`.

```python
from errr import make_tree, exception as _e

make_tree(
  # Pass the module dictionary as first argument
  globals(),
  # List your nested exceptions
  RootException=_e(
    ChildException=_e(),
    Child2Exception=_e()
  ),
  SecondRootException=_e(
    # List details as positional arguments
    "detail1", "detail2",
    # And continue with child exceptions as keyword arguments
    AnotherChildException=_e()
  )
)

print(RootException)
# <class '__main__.RootException'>
print(ChildException)
# <class '__main__.ChildException'>
print(ChildException.__bases__)
# (<class '__main__.RootException'>,)
```
