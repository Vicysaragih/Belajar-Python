
# If-Else
n = 5
if(n%2 != 0 or (n>=6 and n<=20)):
    print("Weird")
else:
    print("Not Weird")

print(5 != 5)

print("AC/DC" != " VICY SARAGIH")

age = 15
if (age > 18):
    print("Silahkan masuk")
else:
    print("Maaf")

# Contoh 2
nama = input(f"Masukan nama anda: \n")
if nama == "Vicy":
    print(f" Horas Bro: {nama}\n")
else:
    print(f"Hei {nama}, Anda bukan Vicy, Pergi sana !!")
print("Akhir dari program.")

# elif
Marga = input(f"Masukan marga anda: \n")
if Marga == " Saragih":
    print(f"Horas {Marga}\n")
elif Marga =="Purba":
    print(f" Sorry {Marga}, kita berbeda!\n")
elif Marga == "Damanik":
    print(f" Santabi {Marga} Tonndong nami!\n")
elif Marga == "Sinaga":
    print(f"Boru ni tulang do hape ham boru {Marga}")
else:
    print("Anda bukan Simalungun")

# Latihan Percabagan 
angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("masukan angka 2 = "))

if operator == "+":
	hasil = angka_1 + angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "-":
	hasil = angka_1 - angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
	hasil = angka_1 * angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "/":
	hasil = angka_1 / angka_2
	print(f"hasilnya adalah {hasil}")
else:
	print("masukan yang bener dong!, aku pusying")

print("Akhir dari program, terima gajih!")