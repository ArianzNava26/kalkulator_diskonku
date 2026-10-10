import sys
import subprocess


print("\nLet's Count The Price! Shall We? :) ~Created by Arian Surya\n")
hargaawal = int(input("\nHow Much the Asking Price? "))
harga1 = int(input("\nHow Much is Your desired price? "))
selisih = int(hargaawal - harga1)
rumus = int(selisih / hargaawal * 100)
print("\nThe Discount is: ", rumus, "%\n")
tanya = str(input("\nOk, What Should We do Next?\nA.Go Back into Main Menu\nB.Quit\n"))
if tanya.lower() == "a":
    print("Let's Go Back to Main Menu! Shall We?")
    subprocess.run([sys.executable, "e-pilihan.py"])
elif tanya.lower() == "b":
    print("\nThank You, This Simple Ai Project created by Arian S!\n\n")
