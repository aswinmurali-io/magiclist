# Magic List

Magiclist is an awesome data type ! Magiclist has the ability to release
memory on a per element basis rather than the object itself! This way magiclist
can store a large amount of data inside it without running out of memory. When
magiclist runs out of memory, then purge() function can be called and all the
inactive elements are suspended from the memory and later on returned when needed.
It is capable for storing persistent data. Magiclist can be used for handling
BIG data, perfect for data science! Multiple programs can share the same magiclist
data with their own in-memory cache!

### Install the deps

```bash
pip install -r requirements.txt
```

### Generate documentation

```bash
python setup.py build_sphinx
```

### Compile magiclist for better speed

```bash
python setup.py build_ext
```
