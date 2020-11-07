import random as rd

# TODO: Create a Database for all the Food Types and Chain Restaurants

# fast_food_types = {
#     1: "Hamburguesas",
#     2: "Pollo",
#     3: "Sushi",
#     4: "Pizza",
#     5: "Sandwiches",
#     6: "Nacional",
#     7: "Internacional",
#     8: "Masas",
#     9: "Churrasco",
#     10: "Dulces"
# }

fast_food_typesfood = {
    1: {1: "McDonalds", 2: "Burger King", 3: "Carls Jr", 4: "Honesto Mike",
    5: "Holly Molly"},
    2: "Pollo",
    3: "Sushi",
    4: "Pizza",
    5: "Sandwiches",
    6: "Nacional",
    7: "Internacional",
    8: "Masas",
    9: "Churrasco",
    10: "Dulces"
}


# def choose_foodType(num):
#     return fast_food_types.get(num, 'Otros')
#
#
# print(choose_foodType(rd.randint(1, len(fast_food_types))))


print(fast_food_typesfood[1][rd.randint(1,5)])
