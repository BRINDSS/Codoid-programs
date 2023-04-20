def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [5,4,10,20,4,6,10,39,4,39]
print(Remove(duplicate))
