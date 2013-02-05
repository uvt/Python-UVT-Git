print "\n"
print ".:PYTHON FLAT TEXT CREATOR v.01:."
print "\n"

program_berjalan = True

while program_berjalan:
    awal = ":"
    print "Apa yang ingin Anda lakukan?"
    print "'n' Buat file baru"
    print "'o' Buka file terdahulu"
    print "'c' Salin file"
    print "'q' Tutup aplikasi"

# Menu pilihan

    pilih_menu = raw_input(awal)
    if pilih_menu == 'n':
        print "Masukkan nama file yang hendak dibuat beserta ekstensinya (.doc atau .txt)."
        filename = raw_input(awal)
        target = open(filename, 'w')
        tulis = raw_input("Tulis di bawah: \n")
        target.write(tulis + "\n")
        tulis = raw_input("\n")
        target.write(tulis)
        target.close()
        print "\n"
        print "File berhasil dibuat."
        print "\n"
    elif pilih_menu == 'o':
        print "Masukkan nama file yang ingin dibuka: "
        filename = raw_input(awal)
        target = open(filename, 'r')
        print target.read()
        print "\n"
    elif pilih_menu == 'c':
        print "Masukkan nama file yang ingin disalin: "
        filename = raw_input(awal)
        target = open(filename)
        print "Masukkan nama file yang ingin dibuat: "
        filename2 = raw_input(awal)
        target2 = open(filename2, 'a')
        for line in target.readlines():
            target2.write(line)
        target2.close()
        target.close()
    elif pilih_menu == 'q':
        program_berjalan = False
    else:
        print "Silakan pilih sesuai simbol yang tersedia."
        print "\n"
        
else:
    print "Terima kasih telah menggunakan Termpad."
