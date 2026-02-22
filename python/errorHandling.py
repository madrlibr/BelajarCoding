"""
Disini kita akan membahas untuk cara menangani error agar program tidak crash.

Ada dua komponen utama yaitu try dan except
"""

#Contoh:

#=========BLOK TRY===========#
try: #Coba blok kode dibawah:

    #KALKULATOR SEDERHANA
    inputUser1 = int(input("1.Masukan angka Integer: "))
    inputUser2 = int(input("2.Masukan angka Integer: "))
    operator = str(input("Pilih operator [+][-][*][/]: "))

    if operator == "+":
        hasil = inputUser1 + inputUser2
        print(hasil)
    elif operator == "-":
        hasil = inputUser1 - inputUser2
        print(hasil)
    elif operator == "*":
        hasil = inputUser1 * inputUser2
        print(hasil)
    elif operator == "/":
        hasil = inputUser1 / inputUser2
        print(hasil)
    else:
        print("!Anda harus memilih operator")
#=============================#

#=========BLOK EXCEPT=========#
except: #Jika crash/error maka jalankan kode dibawah ini
    print("Terjadi kesalahan!")
#==============================

"""
Cara kerja:
program terlebih dahulu akan mencoba blok try, jika terjadi error, program tidak akan crash
tapi akan menjalankan blok except
"""




