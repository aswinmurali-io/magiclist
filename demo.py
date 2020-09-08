from magic import Magic

# creating a magic list, the 'test' string is used as a identifier for sharing instance
test = Magic("test", {"45": "$5"})
test2 = Magic("test2", "demo-test")
test2.append("new", "new")

print("test", test["new"])

# check if there is anything to be loaded for magiclist (return false if it's new magic list)
print(test.loaded)

print(test.memory)

# append items in a parallel fashion
if not test.loaded:
    test.append_parallel({f'{i}': i for i in range(10)})

print("45545", test + test2)

test += test2

print(test2.get("new"))
print(test.get("new"))

# get the element with key '2'
test.get("2")

# print the in-memory cache
print(test.memory)

test.get("1")

# to clean the in-memory cache by suspending unused elements
test.purge()

test.export_cache_list()

print(test.memory)
