# TIL: Python Pathlib - So much nicer than os.path

Today I finally properly dug into Python's `pathlib` module. For ages, I've just used `os.path` for all my file and directory manipulation, which works, but sometimes feels a bit clunky and string-heavy.

`pathlib` is a breath of fresh air. Instead of treating file paths as just strings, it makes them actual objects. This means you get a bunch of useful methods directly on the path object, which feels way more intuitive and cleaner.

The biggest win for me is how easy it makes joining paths. With `os.path`, you'd do `os.path.join('data', 'raw', 'input.csv')`. With `pathlib`, you just use the `/` operator, which is super clean and readable:

```python
from pathlib import Path

p = Path('data') / 'raw' / 'input.csv'
print(p)
# Output: data/raw/input.csv (or data\raw\input.csv on Windows)
```

It automatically handles the correct path separators for your operating system, which is neat. You can also easily check if a path exists (`p.exists()`), create directories (`p.mkdir()`), or grab parts like the file name (`p.name`) or its parent directory (`p.parent`). No more messy `os.path.basename` or `os.path.dirname` calls.

Honestly, it just makes working with files and folders so much more pleasant and readable. I'm definitely switching to `pathlib` for new projects.
