#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk

class Jendela():

    def __init__(self):
        self.jendela = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.jendela.set_title("Jendela")
        self.jendela.set_size_request(500, 300)        
        self.jendela.set_border_width(20)
        self.jendela.set_position(gtk.WIN_POS_CENTER)
        self.tombol()
        self.masukan()
        self.label()
        self.kotak_cek()
        self.kotak_pilihan()
        self.kotak()
        self.koneksi()
        self.jendela.show_all()

    def tombol(self):
        self.tombol_ok = gtk.Button("Oke")
        self.tombol_keluar = gtk.Button("Keluar")
        self.tombol_tutup = gtk.Button(stock=gtk.STOCK_CLOSE)
        self.tombol_tutup.set_flags(gtk.CAN_DEFAULT)

    def masukan(self):
        self.masukan_karakter = gtk.Entry()
    
    def label(self):
        self.label_nama = gtk.Label("Nama Anda:")
        self.label_tutup = gtk.Label("Tutup Aplikasi:")

    def kotak_cek(self):
        self.kerangka_cek = gtk.Frame("Centang Kotak:")
        self.kerangka_cek.set_shadow_type(gtk.SHADOW_IN)
        self.tombol_cek = gtk.CheckButton("Saya setuju!")
        self.tombol_cek.set_active(True)

    def kotak_pilihan(self):
        self.kotak_kombo = gtk.combo_box_new_text()
        self.kotak_kombo.append_text("Program Anda:")
        self.kotak_kombo.append_text("Python")
        self.kotak_kombo.append_text("Perl")
        self.kotak_kombo.append_text("Ruby")
        self.kotak_kombo.set_active(0)

    def kotak(self):
        self.kotak_vertikal = gtk.VBox(spacing = 10)
        self.kotak_horizontal_1 = gtk.HBox(spacing = 10)
        self.kotak_horizontal_1.pack_start(self.label_nama)
        self.kotak_horizontal_1.pack_start(self.masukan_karakter)
        self.kotak_horizontal_2 = gtk.HBox(spacing = 10)
        self.kotak_horizontal_2.pack_start(self.tombol_ok)
        self.kotak_horizontal_2.pack_start(self.tombol_keluar)
        self.kotak_horizontal_3 = gtk.HBox(spacing = 10)        
        self.kotak_horizontal_3.pack_start(self.label_tutup)
        self.kotak_horizontal_3.pack_start(self.tombol_tutup)  
        self.kotak_horizontal_4 = gtk.HBox(spacing = 10)
        self.kotak_horizontal_4.pack_start(self.kerangka_cek)
        self.kotak_horizontal_4.pack_start(self.tombol_cek)   
        self.kotak_horizontal_5 = gtk.HBox(spacing = 10)   
        self.kotak_horizontal_5.pack_start(self.kotak_kombo)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_1)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_2)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_3)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_4)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_5)
        self.jendela.add(self.kotak_vertikal)
     
    def koneksi(self):
        self.tombol_ok.connect("clicked", self.panggilan_ok)
        self.tombol_keluar.connect("clicked", self.panggilan_keluar)
        self.tombol_tutup.connect("clicked", self.panggilan_keluar)
        self.jendela.connect("destroy", gtk.main_quit)
        self.tombol_cek.connect("toggled", self.masukan_cek)
        self.kotak_kombo.connect("changed", self.pilihan_cek)
        
    def masukan_cek(self, x):
        tandai_masukan_cek = x.get_active()
        if tandai_masukan_cek:
            print "Kotak dicentang"
        else:
            print "Tidak dicentang"
        return

    def pilihan_cek(self, x):
        model = x.get_model()
        indeks = x.get_active()
        pilihan = True
        if indeks:
            print "Program pilihan: ", model[indeks][0]
        if pilihan == "Program Anda:":
            print "Anda belum memilih!"
        return
               
    def panggilan_ok(self, x):
        nama = self.masukan_karakter.get_text()
        print nama
     
    def panggilan_keluar(self, x):
        gtk.main_quit()

if __name__ == "__main__":
    Jendela()
    gtk.main()
