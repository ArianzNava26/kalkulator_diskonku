import sys
import subprocess

bahasa = str(
    input("Please Choose Your Preferred Language:\nA.Bahasa Indonesia\nB. English ")
)
if bahasa.lower() == "a":
    print("Selamat Datang!")
    subprocess.run([sys.executable, "pilihan.py"])
elif bahasa.lower() == "b":
    print("Welcome to Arian's World!")
    subprocess.run([sys.executable, "e-pilihan.py"])
else:
    print("..AI is Exiting")
