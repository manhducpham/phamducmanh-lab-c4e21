# 9.
def get_even_list(l):
    new_l = []
    for num in l:
        if num % 2 ==0:
            new_l.append(num)
    return new_l

# 10.
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
