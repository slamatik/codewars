def get_order(order):
    menu = ["burger",
            "fries",
            "chicken",
            "pizza",
            "sandwich",
            "onionrings",
            "milkshake",
            "coke"]
    quantities = [0 for i in range(len(menu))]
    while order:
        for i in range(len(order)):
            temp = order[:i + 1]
            if temp in menu:
                quantities[menu.index(temp)] += 1
                order = order[i + 1:]
    results = []
    for i in range(len(menu)):
        for j in range(quantities[i]):
            results.append(menu[i].capitalize())
    return " ".join(results)
