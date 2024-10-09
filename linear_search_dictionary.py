my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}


def linear_search_dictionary(my_dictionary, target):
    for key, value in my_dictionary.items():
        if value == target:
            print(f"Found '{key}' with value {target}")
            return key
    print("Target is not in the dictionary")
    return -1


linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
