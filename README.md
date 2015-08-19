Weird python json? pandas? pickle? bug. To generate, using Python 2.7.9:

```shell
➜  bad-python-list  python TDAT2_load.py | grep ident 
one of these two lists cannot be json serialized but they are identical according to python!?!?
one of these two lists cannot be json serialized but they are identical according to python!?!?
one of these two lists cannot be json serialized but they are identical according to python!?!?
one of these two lists cannot be json serialized but they are identical according to python!?!?
one of these two lists cannot be json serialized but they are identical according to python!?!?
one of these two lists cannot be json serialized but they are identical according to python!?!?
one of these two lists cannot be json serialized but they are identical according to python!?!?
```

Basically, we convert a dict of key: lists to a pandas data frame, then convert it back.
Before trans-reversion to the dict of lists, we are able to serialize it using `json.dumps`. Afterwards, we get an error that:

```python
Traceback (most recent call last):
  File "TDAT2_load.py", line 27, in <module>
    json.dumps(after) ## failes
  File "/usr/lib/python2.7/json/__init__.py", line 243, in dumps
    return _default_encoder.encode(obj)
  File "/usr/lib/python2.7/json/encoder.py", line 207, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python2.7/json/encoder.py", line 270, in iterencode
    return _iterencode(o, 0)
  File "/usr/lib/python2.7/json/encoder.py", line 184, in default
    raise TypeError(repr(o) + " is not JSON serializable")
TypeError: False is not JSON serializable
```

But before converting the data through pandas we are able to serialize just fine.

Investigating why, we end up comparing elements in each dict that do not serialize. They are all lists of `False`, and python thinks they are equal.

Why?
