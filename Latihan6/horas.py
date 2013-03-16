#!/usr/bin/env python

# contoh horas.py

import pygtk
pygtk.require('2.0')
import gtk

class HorasBah:

    def horas(self, uvt, data=None):
        print "Horas Bah"

    def hapus(self, uvt, event, data=None):
        print "Hapus Bah"
        return False

    def keluar(self, uvt, data=None):
        print "Keluar Bah"
        gtk.main_quit()

    def __init__(self):
        self.jendela = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.jendela.connect("delete_event", self.hapus)
        self.jendela.connect("destroy", self.keluar)
        self.jendela.set_border_width(60)
        self.tombol = gtk.Button("Horas UVT!")
        self.tombol.connect("clicked", self.horas, None)
        self.tombol.connect_object("clicked", gtk.Widget.destroy, self.jendela)
        self.jendela.add(self.tombol)
        self.tombol.show()
        self.jendela.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    kabar = HorasBah()
    kabar.main()
