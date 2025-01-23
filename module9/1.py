def apply_all_func(int_list, *functions):
    my_dict = {}
    if functions:
        for function in functions:
            result = function(int_list)
            my_dict[function.__name__] = result

    return my_dict


print(apply_all_func([6, 20, 15, 9], max, min))

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
