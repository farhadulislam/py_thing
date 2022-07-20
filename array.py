from array import array

array_integers = array('i', [0,1,2,3,4,6])
print(array_integers)
array_integers.append(9)
print(array_integers)
print(f"Buffer info", array_integers.buffer_info())

array_float = array('f', [0.1, 0.2, 0.3, 0.4, 0.5])
print(array_float)