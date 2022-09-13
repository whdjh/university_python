def unique_values(aList):
    result = []
    for value in aList:
        if value not in result:
            result.append(value)
    result.sort(reverse=True)
    return result