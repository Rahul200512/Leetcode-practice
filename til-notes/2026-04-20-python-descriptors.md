# TIL: Python Descriptors

Today I finally dug into Python descriptors a bit more. They're actually pretty neat! Basically, they're objects that control how attributes are accessed, set, or deleted on another object.

The core idea is simple: if an object defines any of `__get__`, `__set__`, or `__delete__` methods, it can act as a descriptor. You put an instance of this descriptor class as a class attribute on another class. Then, when you try to get, set, or delete that attribute on an instance of the owner class, Python calls the descriptor's specific method instead. It's how `property()`, static methods, and class methods are implemented under the hood. Super powerful for custom attribute behavior!

Here's a quick example I jotted down:

```python
class ValueLogger:
    def __get__(self, obj, objtype=None):
        print("Attribute was GET!")
        return f"Hello from {objtype.__name__}"

    def __set__(self, obj, value):
        print(f"Attribute was SET to: {value}!")

class MyStuff:
    item = ValueLogger()

# Check it out
m = MyStuff()
print(m.item)       # Calls __get__
m.item = "new value" # Calls __set__
```
