#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
# 
# kalkuluvt.py
#
# Copyright 2013 Universitas Virtual Terbuka
#
# Referensi program:
# 1. http://code.google.com/p/calculator-using-pygtk
# 2. http://code.google.com/p/calculator-python-glade
# 3. http://zetcode.com/gui/pygtk/layout
# 
# Program ini buat pembelajaran di Universitas Virtual Terbuka

try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk, sys
except:
    print("GTK Not Available")
    sys.exit(1)

license = """Kalkulator UVT is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License(GPL v3) as published by
the Free Software Foundation.

Kalkulator UVT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Kalkulator UVT; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA."""

authors = ["Raviyanto Ahmad", "Rajeswari Seetharaman", "Jan Bodnar"]

class Kalkulator:
    def __init__(self):
        self.jendela = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.jendela.set_size_request(470, 300)
        self.jendela.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#7E2217"))
        self.jendela.set_resizable(True)
        self.jendela.set_position(gtk.WIN_POS_CENTER)
        self.jendela.set_border_width(20)
        self.jendela.set_title("Kalkulator UVT")
        
        try:
            self.jendela.set_icon_from_file("python.png")
        except Exception, e:
            print e.message
                        
        self.tombol()
        self.menu()
        #self.fiks()
        self.tabel()
        self.masukan()
        self.kotak()
        self.konek()
        self.jendela.show_all()

    def tombol(self):
        #self.tombol_ihwal = gtk.Button("Ihwal")
        #self.tombol_ihwal.set_size_request(80, 30)
        
        self.tombol_clear = gtk.Button("Hapus")
        self.tombol_persen = gtk.Button("%")
        self.tombol_ce = gtk.Button("Nol")
        self.tombol_close = gtk.Button("Tutup")
        
        self.tombol_tujuh = gtk.Button("7")
        self.tombol_delapan = gtk.Button("8")
        self.tombol_sembilan = gtk.Button("9")
        self.tombol_bagi = gtk.Button(":")
        
        self.tombol_empat = gtk.Button("4")
        self.tombol_lima = gtk.Button("5")
        self.tombol_enam = gtk.Button("6")
        self.tombol_kali = gtk.Button("x")
    
        self.tombol_satu = gtk.Button("1")
        self.tombol_dua = gtk.Button("2")
        self.tombol_tiga = gtk.Button("3")
        self.tombol_kurang = gtk.Button("-")

        self.tombol_nol = gtk.Button("0")
        self.tombol_titik = gtk.Button(".")
        self.tombol_sama_dengan = gtk.Button("=")
        self.tombol_tambah = gtk.Button("+")

    def menu(self):
        self.papan_menu = gtk.MenuBar()
        self.pilihan = gtk.Menu()
        self.berkas = gtk.MenuItem("Baca Keterangan Program")
        self.berkas.set_submenu(self.pilihan)
        self.tentang = gtk.MenuItem("Tentang Program")
        self.keluar = gtk.MenuItem("Keluar Program")
        self.pilihan.append(self.tentang)
        self.pilihan.append(self.keluar)
        self.papan_menu.append(self.berkas)

    #def fiks(self):
        #self.tetap = gtk.Fixed()
        #self.tetap.put(self.tombol_ihwal, 275, 5)
        
    def masukan(self):
        self.masukan_angka = gtk.Entry()
    
    def tabel(self):
        self.tabel_kalkulator = gtk.Table(rows = 5, columns = 4, homogeneous = True)
        self.tabel_kalkulator.attach(self.tombol_clear, 0, 1, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_persen, 1, 2, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_ce, 2, 3, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_close, 3, 4, 0, 1)

        self.tabel_kalkulator.attach(self.tombol_tujuh, 0, 1, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_delapan, 1, 2, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_sembilan, 2, 3, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_bagi, 3, 4, 1, 2)

        self.tabel_kalkulator.attach(self.tombol_empat, 0, 1, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_lima, 1, 2, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_enam, 2, 3, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_kali, 3, 4, 2, 3)

        self.tabel_kalkulator.attach(self.tombol_satu, 0, 1, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_dua, 1, 2, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_tiga, 2, 3, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_kurang, 3, 4, 3, 4)

        self.tabel_kalkulator.attach(self.tombol_nol, 0, 1, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_titik, 1, 2, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_sama_dengan, 2, 3, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_tambah, 3, 4, 4, 5)

    
    def kotak(self):
        self.kotak_vertikal = gtk.VBox(spacing = 20)
        
        self.kotak_horizontal_1 = gtk.HBox(spacing = 10)
        #self.kotak_horizontal_1.pack_start(self.tetap)       
        self.kotak_horizontal_1.pack_start(self.papan_menu)
        
        self.kotak_horizontal_2 = gtk.HBox(spacing = 10)
        self.kotak_horizontal_2.pack_start(self.masukan_angka)

        self.kotak_horizontal_3 = gtk.HBox(spacing = 10)
        self.kotak_horizontal_3.pack_start(self.tabel_kalkulator)

        self.kotak_vertikal.pack_start(self.kotak_horizontal_1)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_2)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_3)

        self.jendela.add(self.kotak_vertikal)

    def konek(self):
        #self.tombol_ihwal.connect("clicked", self.ihwal)
        self.keluar.connect("activate", gtk.main_quit)
        self.tentang.connect("activate", self.ihwal)
        
        self.tombol_close.connect("clicked", self.panggilan_keluar)
        self.jendela.connect("destroy", self.panggilan_keluar)
        
        self.tombol_satu.connect("clicked", self.cetak_karakter, "1")    
        self.tombol_dua.connect("clicked", self.cetak_karakter, "2")
        self.tombol_tiga.connect("clicked", self.cetak_karakter, "3")
        self.tombol_empat.connect("clicked", self.cetak_karakter, "4")
        self.tombol_lima.connect("clicked", self.cetak_karakter, "5")

        self.tombol_enam.connect("clicked", self.cetak_karakter, "6")
        self.tombol_tujuh.connect("clicked", self.cetak_karakter, "7")
        self.tombol_delapan.connect("clicked", self.cetak_karakter, "8")
        self.tombol_sembilan.connect("clicked", self.cetak_karakter, "9")
        self.tombol_nol.connect("clicked", self.cetak_karakter, "0")
        self.tombol_titik.connect("clicked", self.cetak_karakter, ".")
        
        self.tombol_ce.connect("clicked", self.hitung, "Nol")
        self.tombol_clear.connect("clicked", self.hitung, "Hapus") 
        self.tombol_kali.connect("clicked", self.hitung, "x")
        self.tombol_bagi.connect("clicked", self.hitung, ":")
        self.tombol_tambah.connect("clicked", self.hitung, "+")
        self.tombol_kurang.connect("clicked", self.hitung, "-")
        self.tombol_persen.connect("clicked", self.hitung, "%")
        self.tombol_sama_dengan.connect("clicked", self.hitung, "=")

    def ihwal(self, a):
        self.tentang = gtk.AboutDialog()
        self.tentang.set_program_name("Kalkulator UVT")
        self.tentang.set_version("0.1")
        self.tentang.set_license(license)
        self.tentang.set_copyright("(c) 2013 UVT")
        self.tentang.set_authors(authors)
        self.tentang.set_comments("Kalkulator Sederhana")
        self.tentang.set_website("http://universitas-virtual-terbuka.blogspot.com")
        self.tentang.set_logo(gtk.gdk.pixbuf_new_from_file("python.png"))
        self.tentang.run()
        self.tentang.destroy()
    
    def cetak_karakter(self, a, b):
        self.masukan_angka.insert_text(b, position = 20)

    def hitung(self, a, b):
        if b == "Hapus":
            self.masukan_angka.set_text("")
	elif b == "Nol":
	    self.masukan_angka.set_text("0")		
	elif b == "+":
	    self.tanda = 1
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == "-":
	    self.tanda = 2
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == "x":
	    self.tanda = 3
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == ":":
	    self.tanda = 4
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == "%":
	    self.tanda = 5
	    self.angka_pertama = self.masukan_angka.get_text()
	    self.masukan_angka.set_text("")
	elif b == "=":
	    self.angka_kedua = self.masukan_angka.get_text()
	    jumlah1 = float(self.angka_pertama)
	    jumlah2 = float(self.angka_kedua)
	    if self.tanda == 1:
	        hasil = jumlah1 + jumlah2
	    elif self.tanda == 2:
	        hasil = jumlah1 - jumlah2
	    elif self.tanda == 3:
	        hasil = jumlah1 * jumlah2
	    elif self.tanda == 4:
	    	if jumlah2 == 0.0:
                    try:
		        hasil = jumlah1 / jumlah2
		    except:						
			hasil = "Maaf, Saudara, angka kedua 0. Jadi, kalkulator ini bingung!"
		else:
	            hasil = jumlah1 / jumlah2
	    elif self.tanda == 5:
	        jumlah1 = int(jumlah1)
		jumlah2 = int(jumlah2)	
		hasil = jumlah1 % jumlah2
	    self.masukan_angka.set_text(str(hasil))
        
    def panggilan_keluar(self, a):
        gtk.main_quit()

if __name__ == "__main__":
    Kalkulator()
    gtk.main()

    
        


       
