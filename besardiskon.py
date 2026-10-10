import sys
import subprocess


print(
    "\nMari Kita buat Mesin pencari Besar Diskon yang dibutuhkan! ~Created by Arian Surya\n"
)
hargaawal = int(input("\nBerapa Harga Awal nya? "))
harga1 = int(input("\nBerapa Harga Akhir yang diinginkan? "))
selisih = int(hargaawal - harga1)
rumus = int(selisih / hargaawal * 100)
print("\nBerarti Besarnya Diskon untuk Produk adalah sebesar: ", rumus, "%\n")
tanya = str(
    input("\nOk Sekarang Anda ingin Apa nih?\nA.Balik ke Menu Utama\nB.Selesai\n")
)
if tanya.lower() == "a":
    print("Kita Kembali ke Menu Utama!")
    subprocess.run([sys.executable, "pilihan.py"])
elif tanya.lower() == "b":
    print("\nTerima Kasih, ini semua diciptakan oleh Arian Surya!\n\n")
