def pig_it(text):
    from string import punctuation
    solution = []
    text = text.split()
    for i in text:
        if i not in punctuation:
            solution.append(i[1:] + i[:1] + "ay")
        else:
            solution.append(i)
    return " ".join(solution)


print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
print(pig_it('Hello world !'))
