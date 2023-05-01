list = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']
list.append('!')
print(list)

del(list[4])
print(list)

list.insert(4, 'a')
print(list)

data_list = ''.join(map(str, list))
print(data_list)

list.sort(reverse=True)
print(list)