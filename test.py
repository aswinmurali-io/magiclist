from magic import Magic


test: Magic = Magic("test")

print(test.loaded)
if not test.loaded:
    test.append_parallel({f'{i}': i for i in range(10)})

test.get("2")
print(test.memory)
test.get("1")
test.purge()

print(test.memory)
