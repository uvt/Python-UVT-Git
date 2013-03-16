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
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.hapus)
        self.window.connect("destroy", self.keluar)
        self.window.set_border_width(60)
        self.button = gtk.Button("Horas UVT!")
        self.button.connect("clicked", self.horas, None)
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    kabar = HorasBah()
    kabar.main()
