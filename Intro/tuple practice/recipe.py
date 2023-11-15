def get_tuple_list(text1, text2, text3):
    # gets a list of tuples, ending with a blank line
    # uses given 'text' parameters as prompts for input
    # ends collection when element1 ""

    a_list = []

    while True:
        element1 = input(text1)
        if element1 == "":
            break
        element2 = input(text2)
        element3 = input(text3)

        a_list.append((element1, element2, element3))
    return a_list


def scale(a_list, factor):
    # scale the float element of a given tuple list by a given factor

    return [(element1, float(element2) * factor, element3) for element1, element2, element3 in a_list]


def recipe_summary(a_list):
    # give a summary of a list in 'recipe' format

    print("New Recipe:")
    for element1, element2, element3 in a_list:
        print(f"  {element2} ({element3}) {element1}")


def main():
    print("What ingredients are in your recipe? ")
    recipe = get_tuple_list("Ingredient: ", "Quantity: ", "Unit: ")
    scaling_factor = float(input("Scaling factor: "))
    scaled_recipe = scale(recipe, scaling_factor)
    recipe_summary(scaled_recipe)


if __name__ == '__main__':
    main()
