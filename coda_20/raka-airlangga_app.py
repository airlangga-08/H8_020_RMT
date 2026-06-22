'''
=================================================
Graded Challenge 2

Nama  : Raka Airlangga
Batch : CODA-RMT-020

Program ini dibuat untuk mempelajari konsep function, if conditional, dan loop
=================================================
'''

'''keranjang {} ini berfungsi sebagai wadah untuk user meng input variable dan value'''
keranjang = {}

'''def menu() adalah fungsi yang menyimpan proses yang akan menampilkan pilihan menu 
dan meminta user input nomor menu yang tersedia'''
def menu():
    print('Selamat datang di Toko kami!') #\n adalah 'enter' berfungsi agar teks selanjutnya berada di bawah
    print('Menu:\n' 
    '1. Tambah Barang\n'
    '2. Hapus Barang\n'
    '3. Tampilkan Barang di Keranjang\n'
    '4. Total Belanja\n'
    '5. Keluar\n')
    input_user = input('Silahkan pilih nomor menu di atas: ') #input berfungsi agar user bisa berinteraksi dengan mengetik apa yang mereka mau
    
    return input_user #return berfungsi mengiirim hasil input dari dalam fungsi keluar, 
#sehingga hasil disimpan sebagai variable dan digunakan pada funsgi 'if' di bawah 

'''def tambah_barang() adalah proses dimana user masuk ke menu "1" dan 
melakukan interaksi dengan menulis nama dan harga barang'''
def tambah_barang():
    nama_barang = input('Masukan nama barang: ')
    harga_barang = int(input('Masukan harga barang: Rp ')) #int disini berfungsi jika user input string dia akan error

    keranjang[nama_barang] = harga_barang
    print(f'{nama_barang} berhasil dimasukan ke keranjang\n') #f'{variable}' di sini berfungsi untuk mengkombinasi string dan variable tanpa harus menggunakan tanda + sebagai penghubung
    

'''def hapus barang() berfungsi jika user ingin menghapus barang yang ada di keranjang dengan cara input nama barang'''
def hapus_barang():
    barang = input('Masukan barang yang ingin dihapus:')
    if barang in keranjang: #menggunakan 'if' statemnt sehingga jika nama barang ada di keranjang maka jalankan perintah 'del'
        del keranjang[barang]
        print(f'{barang} telah dihapus\n')
    else:
        print('Barang tidak ada') #jika user menulis barang yang tidak ada di keranjang maka outputnya ini


'''def tampilkan_barang() berisi proses yang akan menampilkan nama barang dan harga yang telah diinput sebelumnya'''
def tampilkan_barang():
    if len(keranjang) == 0: #menggunakan len == 0 berfungsi menghitung jumlah item di keranjang jadi jika saat pilih no 3 dan tidak ada barang di dalamnya
        print('keranjang kosong\n') #maka tampilkan pesan ini
    else:
        for barang, harga in keranjang.items(): #for untuk mengambil dan memproses setiap pasangan data
                                                #.items digunakan untuk mengambil isi dict sebagai pasangan key dan value
            print(f'{barang}: Rp{harga}')

'''def total_belanja() adalah fungsi untuk menampilkan total belanja yang harus dibayar'''
def total_belanja():
    print('Total belanja: Rp', sum(keranjang.values())) #menggunakan sum untuk menjumlahkan value yang ada di keranjang

'''if __name__ == '__main__' ini untuk menjalankan menu program dengan memanggil nama file
(raka-airlangga_app.py) dan bisa juga dipakai untuk import sebagai modul'''
if __name__ == '__main__':
    while True: #While + True itu berfungsi agar program dapat terus berjalan selama kondisinya benar
        input_user = menu()
        if input_user == '1':
            tambah_barang()
        elif input_user == '2':
            hapus_barang()
        elif input_user == '3':
            tampilkan_barang()
        elif input_user == '4':
            total_belanja()
        elif input_user == '5':
            print('\nTerima kasih telah berbelanja\nSemoga hari mu menyenangkan!!!\n')
            break #ini berfungsi untuk menghentikan while loop di atas
        else:
            print('Mohon ikuti sesuai instruksi yaa :)')







