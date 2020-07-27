data = ["NORTH", "SOUTH", "EAST", "WEST"]


def dirReduc(a):
    for i in range(len(a) - 1):
        if a[i] == "NORTH" and a[i + 1] == "SOUTH":
            a.pop(i)
            a.pop(i)
            return dirReduc(a)
        elif a[i] == "SOUTH" and a[i + 1] == "NORTH":
            a.pop(i)
            a.pop(i)
            return dirReduc(a)
        elif a[i] == "WEST" and a[i + 1] == "EAST":
            a.pop(i)
            a.pop(i)
            return dirReduc(a)
        elif a[i] == "EAST" and a[i + 1] == "WEST":
            a.pop(i)
            a.pop(i)
            return dirReduc(a)
    return a


print(dirReduc(data))
