# fungsi pemilihan bioskop
print("Dimanakah kamu ingin menonton?")
print("XXI Empire")
print("XXI Amplaz")
print("XXI JCM")
pilihan=int(input("masukkan pilihanmu: "))
if pilihan == 1 :
    print("XXI Empire")
elif pilihan == 2 :
    print("XXi Amplaz")
elif pilihan == 3 :
    print("XXI JCM")
else :
    print("pilihan salah")

# fungsi pemilihan film
print("Mau nonton film apa nih? Ada film:")
print("Frozen")
print("Keramat")
print("KKN di Desa Penari")
pilihan=int(input("Pilih nomor film: "))
if pilihan == 1 :
    jumlah = 1
    print("Frozen")
elif pilihan == 2 :
    print("Keramat")
elif pilihan == 3 :
    print("KKN di Desa Penari")
else :
    print("pilihan salah")

# fungsi pemilihan tipe layar
print("Mau nonton layar bioskop apa: ")
print("Reguler")
print("Dolby Atmos")
print("Premiere")
pilihan=int(input("Pilih nomor tipe layar: "))
if pilihan == 1 :
    jumlah = 1
    print("Reguler")
elif pilihan == 2 :
    print("Dolby Atmos")
elif pilihan == 3 :
    print("Premiere")
else :
    print("pilihan salah")

# berapa banyak tiket 
pilihan=int(input("Berapa banyak tiket? "))

# fungsi waktu nonton
print("Mau nonton jam berapa: ")
print("12.35")
print("14.45")
print("16.55")
print("19.05")
pilihan=int(input("Masukkan angka pilihan anda: "))
print("Oke berhasil, silahkan dinikmati di jam 12.35")
if pilihan == 1 :
    jumlah = 1
    print("12.35")
elif pilihan == 2 :
    print("14.45")
elif pilihan == 3 :
    print("16.55")
elif pilihan == 4 :
    print("19.05")
else :
    print("pilihan salah")
