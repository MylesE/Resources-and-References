# def test(nat, acc):
#     if nat == 0:
#         print(acc)
#     else:
#         test((nat - 1), (acc + 1))
#
# test(10, 0)


# map, filter, zip, and reduce
# test_lst = [1,2,3,4,5]
# print(list(map(lambda x: (x * 2), (test_lst)))) # need to turn into list before it is printable
#
# # or can do it like this:
# def multiply_by2(item):
#     return item * 2
# print(list(map(multiply_by2, test_lst)))
#
# print(test_lst)


# # filter
# def only_odd(number):
#     return number % 2 != 0 #will be odd if this is true
#
# print(list(filter(only_odd, test_lst)))
#
# # or using lambda:
# print(list(filter(lambda x: x % 2 != 0, test_lst)))


# # zip
# lst1 = [1,2,3,4,5]
# lst2 = ['a','b','c','d','e']
# lst3 = [7,8,9,10,11]
#
# print(list(zip(lst1, lst2)))
# print(list(zip(lst2, lst1)))
# print(list(zip(lst1, lst2, lst3)))


# # reduce
from functools import reduce
#
# my_lst = [1, 2, 3]
#
# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item
# print(reduce(accumulator, my_lst, 0))
#
# # alternatively using lambda:
# print(reduce(lambda x, y: x + y, my_lst))



# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
# print(list(map((lambda x: x.upper()), my_pets)))
#
#
# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
#
# print(list(zip(my_strings, sorted(my_numbers))))
#
#
# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
# print(list(filter(lambda x: x > 50, scores)))
#
#
# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# print(reduce(lambda x, y: x + y, (scores + my_numbers)))

# # lambda expressions
# lst_example = [5, 4, 3]
# # Square
# print(list(map(lambda x: (x ** 2), lst_example)))
#
# # List Sorting
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# a.sort(key=lambda x: x[1])
# print(a)

# # List comprehensions allow the quick creation of lists
# test_lst = [char for char in "hello"]
# test_lst2 = [num for num in range(0, 100)]
# test_lst3 = [num*2 for num in range(0, 100)]
# test_lst4 = [num**2 for num in range(0, 100) if num % 2 == 0] # keeps all evens
#
# print(test_lst)
# print(test_lst2)
# print(test_lst3)
# print(test_lst4)

# Set comprehensions are the same but with {} set notation

# # Dictionary comprehensions
# simple_dict = {
#     'a':1,
#     'b':2
# }
# test_dict = {key: value**2 for key, value in simple_dict.items() if value%2==0}
#
# print(test_dict)
#
#
# test_dict2 = {num:num*2 for num in [1,2,3]}
# print(test_dict2)


# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
#
# print(duplicates)
