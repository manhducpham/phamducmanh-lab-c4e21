#1: tao 1 lít gom cac số nguyên
#2 cho người dùng nhập vào 1 số
#3 in ra:
#   có tìm thấy số vừa nhập không?
#   nếu có vị trí là ở đâu?

num_list = [4, 5, 7 ,8, -10, -5, -21, 3, 19, 100, 1000, 1000]

#1 code
while True:
    num_enter = input("Enter your number: ")
    if num_enter == "e":
        break
    else:
        num_search = int(num_enter)
        if num_search in num_list:
            print("Found your number in no.", num_list.index(num_search))
        else:
            print('Not found')
#2 function
# a = num_list.__getattribute__(num_search)
# print(a)
found = False # can use mark, flag
for index, item in enumerate(num_list):
    if num_search == item:
        print("Found it")
        print(index)
        found = True
        break # if require find one
if found == False: # = if not found:
    print("Not false")

#3 python lam ho: neu k break thi t se else
for index, item in enumerate(num_list):
    if num_search == item:
        print("Found it")
        print(index)
        break # if require find one
else:
    print("Not false")

