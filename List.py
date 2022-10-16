
#
L = ["MJ", 10.2, 1983]
print(L[1])

# Menambah Isi List
L.extend(["Pop", 34])
print(L)

# Memasukan List baru ke dalam List
L.append(["Pop", 25])
print(L)

# Mengubah nilai dalam List
L[0] = "PJ"
print(L)

# Menghapus nilai
del(L[4])
print(L)

# Convert String to List
print("Vicy Saragih".split())

# Aliacing
L = ["MJ", 10.2, 1983]
C = L
C[0] = "LJ"
print(C)
print(L)

# Clone
L = ["MJ", 10.2, 1983]
C= L[:]
C[1] = 12
print(C)
print(L)

print(L[2:5])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)

# Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

N = int(input())
print(N)

