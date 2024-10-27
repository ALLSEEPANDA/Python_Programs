def tup_to_li_with_str(tup, giv_str):
    result = []
    
    for elem in tup:
        new_elem = str(elem) + giv_str
        result.append(new_elem)    
    return result

tup = (1, 2, 3, 4)
giv_str = " Sheep"
converted_list = tup_to_li_with_str(tup, giv_str)
print(converted_list)