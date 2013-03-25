#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class HorasBah:

    def __init__(self):
        self.jendela = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.jendela.set_title("Horas")
        self.jendela.set_size_request(300, 150)
        self.jendela.set_position(gtk.WIN_POS_CENTER)
        self.jendela.set_border_width(60)
        self.tombol()
        self.konek()
        self.jendela.show_all()

    def tombol(self):
        self.tombol_horas = gtk.Button("Horas UVT")
        self.jendela.add(self.tombol_horas)

    def konek(self):
        self.tombol_horas.connect("clicked", self.horas)
        self.tombol_horas.connect_object("clicked", gtk.Widget.destroy, self.jendela)        
        self.jendela.connect("delete_event", self.hapus)
        self.jendela.connect("destroy", self.keluar)
              
    def horas(self, x):
        print "Horas Bah"
        
    def hapus(self, x, y):
        print "Hapus Bah"
        return False

    def keluar(self, x):
        print "Keluar Bah"
        gtk.main_quit()
   
if __name__ == "__main__":
    HorasBah()
    gtk.main()
