# mi_tuple = (1,2,(10,20),4)
# print(type(mi_tuple))
# print(mi_tuple[0])
# print(mi_tuple[-1])
# mi_tuple[0] = 5 - Error inmutable
# print(mi_tuple[2])
# print(mi_tuple[2][0])
# mi_tuple = list(mi_tuple)
# mi_tuple = tuple(mi_tuple)
# print(type(mi_tuple))

t = (1,2,3,1)
# x,y,z = t
# x,y,z,a = t -not enough values to unpack
# x,y = t -too many values to unpack
# print(x,y,z)
# print(t.count(1))
print(t.index(2))
