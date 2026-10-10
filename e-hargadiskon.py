import subprocess
import sys

print(
    "\nWelcome! Let's count the Discounted Price!\nYou can Use this for solving the discounted price problem!"
)

angka1 = int(input("\nHow Much the Discount in Percentage? "))
angka2 = int(input("\nHow much the Price? "))
hasil = angka1 % angka2
hasilangka = int((hasil / 100) * angka2)
hasilakhir = int((angka2 - hasilangka))
print("\nWith the Discount ", hasil, "%")
print("\nThat means the Discounted Price number is $", hasilangka)
print("\nSo the Final Price is $", hasilakhir, "\n")
tanyakan = str(
    input("Ok, Now What Should We Do Next?\nA. Back to Main Menu\nB.Done!\n")
)
if tanyakan.lower() == "a":
    subprocess.run([sys.executable, "e-pilihan.py"])
elif tanyakan.lower() == "b":
    print("\nThank You! This Simple AI created by Arian S with Love..\n")
else:
    print(
        "\n\nLu ngomong apa sih? Ditanya apa, nulis apa.\n\nUdah Minum Kopi? Ngantuk Ya?\n\nTiduuurrr kaleeee...\n"
    )
