## TIL: Python `__slots__`

Today I finally took a proper look at `__slots__` in Python classes. Always saw it, never bothered to really understand *why* you'd use it. Turns out, it's pretty neat for memory optimization!

Basically, when you define `__slots__` in a class, you're telling Python "these are the *only* attributes instances of this class will have." The big win here is that it prevents the creation of the `__dict__` attribute on each instance. That `__dict__` is how Python normally stores all your object's attributes, and it can take up a fair bit of memory, especially if you have thousands of small objects.

By ditching `__dict__`, you save memory and can even get slightly faster attribute access. The main catch is that you can't add any new attributes to an object that aren't listed in its `__slots__`.

Here's a quick example:

```python
class SmallPoint:
    __slots__ = ['x', 'y'] # These are the only allowed attributes

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = SmallPoint(10, 20)
# p.z = 30 # This would raise an AttributeError!
```

So, it's pretty handy if you need to optimize memory for a lot of instances of a simple class. Definitely something to keep in my toolbox!
