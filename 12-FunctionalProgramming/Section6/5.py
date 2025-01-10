array = list(range(1,21))
div2a3 = lambda value: value %2 == 0 and value %3 == 0
print(list(filter(div2a3, array)))