# Filter, Map, Reduce

# Filter
#ilter devuelve True or False según el valor esté dentro de los criterios buscados o no.
my_list = [1,4,5,6,9,13,19,21]

add = list(filter(lambda x:x%2 != 0, my_list))
print(add)


# Map

# Map recorre todo el array
my_list = [1,2,3,4,5]

squares = list(map(lambda x:x**2, my_list))
print(squares)


# Reduce
my_list = [2,2,2,2,2]



