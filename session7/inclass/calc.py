def calculate(x, y, op):
    # print("Calculating...")
    # x = 5
    # op = "+"
    # y = 3
    result = 0
    if op == "+":
        # print(x+y)
        result = x + y
    elif op == "-":
        # print(x-y)
        result = x - y
    elif op == '*':
        result = x * y
        # print(x*y)
    elif op == "/":
        result = x / y
        # print(x/y)
    # print(result)
    return result

# a = int(input('a = '))
# op = input('(+, -, *, /): ')
# b = int(input('b = '))

# calculate(a, b, op)
# print(result)
