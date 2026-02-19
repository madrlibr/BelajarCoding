"""
Disini kita akan belajar Input dan output
Input: adalah fungsi untuk menangkap input atau nilai yang dimasukan user untuk diolah
Output: Hasil dari input itu sendiri
Contoh dalam kehidupan sehari-hari:
Kamu memasukan uang vending machine, lalu vending machine itu mengeluarkan makanan/minuman
nah disini uang adalah input dan makanan/minuman itu hasilnya
"""

#Cara-cara penulisan:
input()
input("Masukan: ") #Untuk menambahkan judul/title Input

#Kalian juga bisa menentukan inputnya bertipe data apa
float(input("Masukan angka desimal: ")) 
int(input("Masukan angka integer: "))


#Umumnya input dimasukan ditempatkan ke variabel agar bisa diolah, seperti dibawah ini
angka1 = int(input("1. Masukan angka integer: "))
angka2 = int(input("2. Masukan angka integer: "))

hasil = angka1 + angka2
print(f"{angka1} + {angka2} = {hasil}") #Ini lah yang dinamakan outputnya
"""
Jika dianalogikan, angka1 dan angka2 adalah koin, dan variabel "hasil" adalah mesin dari vending machine yang
mengolah input, lalu 20 + 11 = 31 yang muncul di terminal adalah outputnya yaitu hasil dari mesin yang mengolah input
"""
