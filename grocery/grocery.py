groceries = {}

while True:
    try:
        item = input()
    except EOFError:
        break
    item = item.upper()
    if item in groceries:
        groceries[item] +=1
    else:
        groceries[item] = 1


for item in sorted(groceries.keys()):
    print (groceries[item], item)

