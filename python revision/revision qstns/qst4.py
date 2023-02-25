"""dictionary comprehension"""
"""create a new dictionary .covert all price from dollar to rupee"""
def dollar_to_rupee():
    price = {"laptop":10,"mobile":5,"watch":3,"keybord":1}
    convert_to_rupee = 81.38
    new_dict = {i:j*convert_to_rupee for(i,j) in price.items()}
    return new_dict
rc = dollar_to_rupee()
print("the new dict is:",rc)