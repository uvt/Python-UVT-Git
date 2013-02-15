#!/usr/bin/env python
print """
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
"""
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
            print "Perhatikan ini bukan angka!"

    def bagi(self):
        try: 
            return iniString(self.bilangan_satu) / iniString(self.bilangan_dua)
        except ZeroDivisionError:
            print "Perhatikan bilangan kedua adalah nol!"
        except ValueError:
            print "Perhatikan ini bukan angka!"

    def tambah(self):
        try: 
            return iniString(self.bilangan_satu) + iniString(self.bilangan_dua)
        except ValueError:
            print "Perhatikan ini bukan angka!"
        
    def kurang(self):
        try:
            return iniString(self.bilangan_satu) - iniString(self.bilangan_dua)
        except ValueError:
            print "Perhatikan ini bukan angka!"

program_berjalan = True

while program_berjalan:

    x = raw_input("Masukkan bilangan pertama:")
    y = raw_input("Masukkan bilangan kedua:")

    hasil = OperasiMatematika(x,y)

    print "Pilih Simbol Berikut:"
    print "Tulis '*' untuk perkalian."
    print "Tulis '/' untuk pembagian."
    print "Tulis '+' untuk penjumlahan."
    print "Tulis '-' untuk pengurangan."
    print "Tulis 'x' untuk keluar."

    pilihan = raw_input(":")

    if pilihan == "*":
        print "Hasil %s x %s = %s" % (x,y,hasil.kali())
    elif pilihan == "/":
        print "Hasil %s : %s = %s" % (x,y,hasil.bagi())
    elif pilihan == "+":
        print "Hasil %s + %s = %s" % (x,y,hasil.tambah())
    elif pilihan == "-":
        print "Hasil %s - %s = %s" % (x,y,hasil.kurang())
    elif pilihan == "x":
        program_berjalan = False
    else:
        print "Simbol: %s tidak ada dalam pilihan." % pilihan
        print "Silakan pilih sesuai simbol yang tersedia."
        print "\n"

else:
    print "Terima kasih telah menggunakan kalkulatorku."
 
