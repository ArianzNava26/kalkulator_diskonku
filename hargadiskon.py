import subprocess
import sys

print(
    "\nSelamat Datang di AI Penghitung Besar Diskon!\nPakai ini untuk Menghitung Besar Diskon!"
)

angka1 = int(input("\nBerapa Persen Diskon nya? "))
angka2 = int(input("\nBerapa harga nya? "))
hasil = angka1 % angka2
hasilangka = int((hasil / 100) * angka2)
hasilakhir = int((angka2 - hasilangka))
print("\nMaka dengan Besar Diskon sebesar ", hasil, "%")
print("\nMaka besar POTONGAN HARGA nya adalah Rp", hasilangka)
print("\nMaka besar HARGA SETELAH DISKON nya adalah Rp", hasilakhir, "\n")
tanyakan = str(
    input(
        "Ok, Sekarang apa yang ingin Anda lakukan Berikutnya?\nA. Kembali ke Menu Utama\nB.Selesai\n"
    )
)
if tanyakan.lower() == "a":
    subprocess.run([sys.executable, "pilihan.py"])
elif tanyakan.lower() == "b":
    print("\nTerima Kasih, AI ini diciptakan oleh Arian Surya.\n")
else:
    while tanyakan != True:
        print(
            "\n\nLu ngomong apa sih? Ditanya apa, nulis apa.\n\nUdah Minum Kopi? Ngantuk Ya?\n\nTiduuurrr kaleeee...\n"
        )
