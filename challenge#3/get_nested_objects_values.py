def nested_get_value(nested_input_dict, nested_key):
    internal_dict_value = nested_input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value

if __name__ == '__main__':

    print(nested_get_value({"a":{"b":{"c":"d"}}},["a","b","c"]))
    print(nested_get_value({"x":{"y":{"z":"a"}}},["x","y","z"]))
