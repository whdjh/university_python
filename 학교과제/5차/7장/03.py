def decode_keys(keylogger):
    left = []
    right = []

    for x in keylogger:
        if x == ">":
            if right:
                left.append(right.pop()) 
        elif x == "<":
            if left:
                right.append(left.pop())
        elif x == "-":
            if left:
                left.pop()
        else:
            left.append(x)
    return ("".join(left)+"".join(reversed(right)))