# Magic List

Next gen list data type for today's programming. It is capable for storing
persistent data. Magiclist has the ability to release memory on a *per element basis*
rather than the object itself! This way magiclist can store a *large about of data* inside
it without running out of memory. When magiclist runs out of memory, then purge()
function can be called and all the inactive elements are suspended from the memory and
later on returned when needed. Magiclist can be used for handling BIG data, perfect
for data science! Multiple programs can used the same magiclist data shared with their own in-memory cache!

### Docker support !
```docker build -t magiclist```

### Install the deps
```python3 -m pip install -r requirements.txt```

### Generate documentation
```make html```

### Compile magiclist for better speed
```python3 setup.py buid_ext --inplace```
