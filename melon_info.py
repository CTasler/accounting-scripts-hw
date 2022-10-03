"""Print out all the melons in our inventory."""


# from melons import melon_names, melon_prices, melon_seedlessness 


# def print_melon(name, price, seedless):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])

from melons import melons

def print_melon_data(melons):
    for melon in melons: 
        print(melon)
        for key, value in melons.items():
            if key == melon:
                for k1, v1 in value.items():
                    print(f"{k1}: {v1}")
                    
def add_new_melon(melon_name, melon_price, seedlessness, flesh_color, 
                  rind_color, average_weight):
    melons[melon_name] = {"price": melon_price,"seedlessness": seedlessness, 
                          "flesh_color": flesh_color, "rind_color": rind_color, 
                          "average_weight": average_weight}
    return melons
print_melon_data(melons)
response = input("Would you like to add a new melon to the list? Type"
                 f"'Y' or 'N'").title()
if response == "Y":
    melon_name = input("What is the name of the new melon?").title()
    melon_price = float(input("What is the price?"))
    seedlessness = input("Is the melon seedeless? Type 'True' or" 
                         f"'False'.").title()
    flesh_color = input("What is the melon's flesh color?").title()
    rind_color = input("What is the melon's rind color?").title()
    average_weight = int(input("What is the melon's average weight?"))
    add_new_melon(melon_name, melon_price, seedlessness, flesh_color, 
                  rind_color, average_weight)
    print_melon_data(melons)

    

