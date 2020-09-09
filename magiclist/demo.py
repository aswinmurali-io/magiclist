from magiclist.magic import Magic

# creating a magic list, the 'test' string is used as a identifier for sharing instance
test = Magic("test")
test2 = Magic("test2", "demo")

test2.insert("new", "new")

print("test", test["new"])

# check if there is anything to be loaded for magiclist (return false if it's new magic list)
print(test.loaded)

print(test.memory)

# insert items in a parallel fashion
if not test.loaded:
    test.insert_parallel({f'{i}': i for i in range(10)})

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

test.save_cache()

print(test.memory)

print(">>>>", test.random())

print(test.get("0"))

test -= test2

test.lock = True
test.insert("lock_test", "0")
print(test.memory)

test.lock = False
test2.insert("unloc4", "4545454")
print(test2.memory)

print(test2.get('unloc4'))
