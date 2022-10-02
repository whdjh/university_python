x = []

def flatten(x):
    list_flat = []
    i = 0
    while i < len(x):
        if isinstance(x[i], list):
            list_flat.extend(flatten(x[i]))
        else:
            list_flat.append(x[i])
        i += 1
    result = []
    for value in list_flat:
        if value not in result:
            result.append(value)
    return result

print(flatten(x))