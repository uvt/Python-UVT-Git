#!/usr/bin/env python

from easygui import *

msgbox(msg="""
__name__ = "kalkulatorku"
__version__ = "1.0.0"
__author__ = "Raviyanto Ahmad"
__author_email__ = "raviyanto@gmail.com"
__copyright__ = "Copyright 2013, Python-UVT"
__credits__ = ["Khadis", "Arif", "Rais", "Firdaus", "Samudera", "Dayat"]
__download_url = "https://github.com/UVT/Python-UVT-Git"
__license__ = "GNU GPL"
__maintainer__ = "Raviyanto Ahmad"
__maintainer_email__ = "raviyanto@gmail.com"
__status__ = "Development"
""", title="Keterangan Program")

def iniString(str):
    try:
        nilai = int(str)
    except ValueError:
        nilai = float(str)
    return nilai

class OperasiMatematika(object):

    def __init__(self, bilangan_satu, bilangan_dua):
        self.bilangan_satu = bilangan_satu
        self.bilangan_dua = bilangan_dua

    def kali(self):
        try:
            return iniString(self.bilangan_satu) * iniString(self.bilangan_dua)
        except ValueError:
            msgbox(msg="Perhatikan ini bukan angka!", title="Kesalahan")

    def bagi(self):
        try: 
            return iniString(self.bilangan_satu) / iniString(self.bilangan_dua)
        except ZeroDivisionError:
            msgbox(msg="Perhatikan bilangan kedua adalah nol!", title="Kesalahan")
        except ValueError:
            msgbox(msg="Perhatikan ini bukan angka!", title="Kesalahan")

    def tambah(self):
        try: 
            return iniString(self.bilangan_satu) + iniString(self.bilangan_dua)
        except ValueError:
            msgbox(msg="Perhatikan ini bukan angka!")
        
    def kurang(self):
        try:
            return iniString(self.bilangan_satu) - iniString(self.bilangan_dua)
        except ValueError:
            msgbox(msg="Perhatikan ini bukan angka!", title="Kesalahan")


program_berjalan = True

while program_berjalan:

    x = enterbox(msg="Masukkan bilangan pertama:", title="Masukan")
    
    y = enterbox(msg="Masukkan bilangan kedua:", title="Masukan")
        
    hasil = OperasiMatematika(x,y)
    
    msg = "Pilih Operasi Matematika Berikut atau x untuk Keluar:"
    
    title = "Pilihan Anda"
    
    choices = ['*','/','+','-','x']
    
    choice = buttonbox(msg, title, choices)
    
      
    if choice == "*": 
        msgbox(hasil.kali(), title="Hasil")
    elif choice == "/": 
        msgbox(hasil.bagi(), title="Hasil")
    elif choice == "+": 
        msgbox(hasil.tambah(), title="Hasil")
    elif choice == "-": 
        msgbox(hasil.kurang(), title="Hasil")
    else: 
        program_berjalan = False
           
else:
    msgbox("Terima kasih telah menggunakan kalkulatorku.")
