"""
Operator logika ada and, or, not, yaitu untuk membuat sebuah kondisi dan sama dengan perbandingan, dia akan menghasilkan
nilai boolean, yaitu True ataupun false
"""


#Contoh operator logika AND
x = 9 == 9 and 13 == 13
print("x: ", x)
"""
Disini ada dua perbandingan (10 == 10)kiri dan (13 == 13)kanan, "and" disini bisa berarti
kalau kedua perbandingan yaitu perbandingan kiri dan kanan hasilnya True, maka hasilkan nilai True, kalau salah
satunya berisi False, maka hasilkan nilai False, seperti bertanya "Apakah kedua perbandingan memiliki nilai True"
maka kalau salah satunya saja False, maka nilai False yang akan dihasilkan
"""

#Contoh operator logika AND
y = 9 != 1 or 11 == 21
print("y: ", y)
""" 
Ini mirip dengan and, hanya saja operator "or" tidak meminta kedua perbandingan untuk dia menghasilkan nilai True, tapi
kalau salah satunya saja True, maka operator or akan mau menghasilkan nilai True. Disini y akan menghasilkan nilai True
karena meskipun 11 == 21 itu salah/False tapi 9 != 1 itu benar/True
"""

#Contoh operator logika NOT
z = not 9 == 9
print("z: ", z)
"""
sesimpel, operator not membalikan nilai boolean, kita tau bahwa 9 == 9 bernilai True, dengan not, kita membalik nilainya menjadi False
dan sebaliknya, jika nilanya false maka akan dengan menggunakan not, nilainya menjadi True
"""


