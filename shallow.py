my_list1 = [[1, 2, 3], 4, 5, 6]
my_list2 = my_list1[:]
my_list1[0] = 1

print(my_list1)
print(my_list2)


forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan']
zipped_names = zip(forenames, surnames)

print(list(zipped_names))