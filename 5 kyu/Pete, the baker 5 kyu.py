recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}


def cakes(recipe, available):
    try:
        return min([available[i] // recipe[i] for i in recipe])
    except KeyError:
        return 0


print(cakes(recipe, available))
