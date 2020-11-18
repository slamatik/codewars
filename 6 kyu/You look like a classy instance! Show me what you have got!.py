def show_me(instname):
    attributes = sorted(list(vars(instname).keys()))
    class_name = type(instname).__name__
    solution = f"Hi, I'm one of those {class_name}s! Have a look at my "
    if len(attributes) != 1:
        return solution + f"{', '.join([attributes[i] for i in range(len(attributes) - 1)])} and {attributes[-1]}."
    else:
        return solution + f"{attributes[0]}."
