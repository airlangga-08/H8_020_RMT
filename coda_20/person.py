name = 'Raka'
devices = ['laptop', 'smartphone', 'tablet']


def display(nama):
  print(f'halo {nama}!')


def hitung_persegi(panjang, lebar):
  return panjang * lebar


def hitung_segitiga(alas, tinggi):
  return alas * tinggi * 0.5


def hitung_luas(jenis_bidang, angka_1, angka_2):
  if jenis_bidang == 'persegi':
    return hitung_persegi(angka_1, angka_2)

  elif jenis_bidang == 'segitiga':
    return hitung_segitiga(angka_1, angka_2)
  
  else:
    return "bidang tidak diketahui"
  

def cetak_plus(n):
  '''
  function ini digunakan untuk mencetak simbol plus (+) sesuai jumlah yang digunakan didalam argument.
  cara pakai fucntion ini
  cetak_plus(n) >> n adalah jumlah simbol plus yang ingin dibuat.

  cetak_plus(0) >> 

  cetak_plus(3) >> 
  '''
  
  if n <= 0: # Ini conditional jika dia kurang dari sama dengan 0
    print('Input salah')
  else:
    for iter in range(n):
      print('+') 