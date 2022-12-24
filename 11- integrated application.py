import random

# prepare datas
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)
# print(offices)

for office in offices:
    print(f'办公室的人数为{len(office)},老师的名字分别是：')
    for name in office:
        print(name)

