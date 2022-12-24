
list1 = [1, 3, 9, 7, 2, 6, 4]


for j in range(5):
    for i in range(6):
        if list1[i] > list1[i+1]:
            ch = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = ch

print(list1)

# for i in range(6):
#     for j in range(7):
#         if j+i > 6:
#             break
#         elif list1[i] > list1[j+i]:
#             ch = list1[i]
#             list1[i] = list1[j+i]
#             list1[j+i] = ch
#
# print(list1)