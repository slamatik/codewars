def tickets(people):
    notes = {25: 0, 50: 0, 100:0}
    for i in people:
        if i == 25:
            notes[i] += 1
        if i == 50:
            if notes[25] == 0:
                return "NO"
            else:
                notes[25] -= 1
                notes[i] += 1
        if i == 100:
            if notes[25] >= 1 and notes[50] >= 1:
                notes[25] -= 1
                notes[50] -= 1
            elif notes[25] >= 3:
                notes[25] -= 3

            else:
                return "NO"
    return "YES"




print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 25, 25, 50, 100, 50]))
