import sys
import subprocess


print("\nMana yang ingin Anda Pilih? ")
pilihan = str(
    input(
        "\nA. Menghitung Besar Diskon yang Dibutuhkan\nB. Menghitung Harga Setelah Diskon\n"
    )
)
if pilihan.lower() == "a":
    print("Memilih A")
    subprocess.run([sys.executable, "besardiskon.py"])

elif pilihan.lower() == "b":
    print("Memilih B")
    subprocess.run([sys.executable, "hargadiskon.py"])
else:
    print("Lu Nulis Apa sih?\n")
