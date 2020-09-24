a = [6, 5, 4, 19, 17, 11, 13, 43, 55, 66, 77, 14, 87, 26, 22, 34, 39, 88, 76, 21, 96, 33, 51, 52,
     53, 54, 81, 76]
a1 = [x if x != 22 else 55 for x in a]
print(a1)
# num = a.index(19)

# a1 = []
# for x in range(len(a)):
#     if a[x] == 22:
#         a[x] = 55
#         a1.append(a[x])
#     else:
#         a1.append(a[x])
# print(a1)

# a1 = [x for x in a  if x == 22  else 55]
# y = [22]
# a1 = [55 if x in a else x for x in y ]
# # res=["-" if x in str else x for x in lis]


# lst1 = ["Sun", "Mon", "Tue", "Wed", "Fri", "Sat"]
# lst2 = ["Sun", "Tue", "Thu", "Sat", "Tom"]
# # lst3 = [x if x not in lst2 else x for x in lst1]
# lst4 = [x for x in lst1 if x not in lst2 for x in lst2 if x not in lst1]
# print(lst4)
# lst3 = []
# for x in lst1:
#     print(x)
#     if x not in lst2:
#         lst3.append(x)
# for x in lst2:
#     if x not in lst1:
#         lst3.append(x)
# print(lst3)
