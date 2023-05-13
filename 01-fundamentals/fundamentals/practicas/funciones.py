"""def multiplicar(num_list, num):
    for x in num_list:      
        x *= num
        c.append(x)
#    return c
a = [2,4,10,16]
c = []
b = multiplicar(a,2)
print(b)
print(c)
"""

def multiplicar1(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
d = multiplicar1(a,5)
print(d)