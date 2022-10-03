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

print_melon_data(melons)