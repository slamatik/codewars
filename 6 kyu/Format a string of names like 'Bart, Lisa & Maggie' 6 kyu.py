data = [{'name': 'Bart'},
        {'name': 'Lisa'},
        {'name': 'Maggie'},
        {'name': 'Homer'},
        {'name': 'Marge'}]


def namelist(names):
    string = ""
    if len(names) == 0:
        return string
    elif len(names) == 1:
        string += names[0]["name"]
    elif len(names) == 2:
        string += names[0]["name"] + " & " + names[1]["name"]
    else:
        for i in range(len(names) - 2):
            string += f'{names[i]["name"]}, '
        string += names[-2]["name"] + " & " + names[-1]["name"]
    return string


print(namelist(data))
