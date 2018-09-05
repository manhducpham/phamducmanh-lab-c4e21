def del_space(t):
    t = t.replace("\n", "")
    t = t.replace("\r", "")
    t = t.replace("\xa0", "")
    while True:
        t = t.replace("  ", " ")
        spaces = '  '
        if spaces not in t:
            break
    return t

t = del_space('\r\n                \xa0\xa0\r\n                19. Lãi cơ bản trên cổ phiếu\r\n       ')
print(t)