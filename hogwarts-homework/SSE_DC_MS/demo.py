my_dict = {"1": 1, "2": 2, "3": 3, "4": 4, "abc": {"bcd": 100}}

print( max(my_dict.items(), key=lambda x: x[1]))