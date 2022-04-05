list1 = [1, 2, 3, 4]
list2 = [8, 12, 45, 67, 89, 45]
list3 = [78, 90, 65]


def app_elements(a):
    for i in range(len(a)):
        a.append(a[i])
    print(f'Отсортированный список: {a}')


app_elements(list1)
app_elements(list2)
app_elements(list3)