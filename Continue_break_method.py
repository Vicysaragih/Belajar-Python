# Continue
for i in range (1, 10):
    if i % 2 == 0:
        continue
    print(i)

# Break
for i in range (1, 10):
    if i % 5 == 0:
        break
    print(i)

angka = 0
# Break 2
while angka < 5:
	angka += 1
	print(f"angka sekarang = {angka}")

	if angka == 3:
		print("nice!")
		break

	print("wassup!")

print("cukuuup finish!")

data_int = int(input("hitung sampai = "))

angka = 0

while True:
	angka += 1
	print(f"count = {angka}")

	if angka == data_int:
		print("nice!")
		break

	print("wassup!")

print("cukuuup finish!")
# Method
nama = []

nama.append("VICY")
print("===")
for data in nama:
    print(data)
nama.append("Saragih \n")
print("===")
for data in nama: 
    print(data)


