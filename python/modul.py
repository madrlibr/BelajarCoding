"""
Disini kita akan membahas modul dan library

Modul adalah 1 file yang berisi kumpulan fungsi ataupun class yang bisa dipanggil dan dipakai di file lain
sedangkan library adalah kumpulan dari banyak modul

"""

#Cara import modul/library
import numpy #mengimport modul numpy
import pandas as pd #kita juga bisa memakai 'as' atau alias agar memudahkan kita memakai fungsi pandas tanpa

#Tanpa as kodenya akan seperti ini:
#pandas.read_csv("dataset.csv")

#dengan as pd:
#pd.read_csv('dataset.csv')

#kalian juga bisa mengganti as nya sesuka kalian, jika kita mengubah as nya menjadi as 'kucing' maka:
# kucing.read_csv('dataset.csv') 
#Jadi kegunaan as adalah kita seakan mengganti nama library/modulnya di program kita

"""
Di folder ini kita punya file bernama mtk.py dan didalamnya ada fungsi, nah kita bisa memakai fungsi tersebut dengan menggunakan import
"""
from mtk import cariDeterminan
#Jika ingin mengimport semua fungsi yang ada: from mtk import *
from mtk import *

print(cariDeterminan(32, 23, 1, 3))
print(luasLingkaran(3))

