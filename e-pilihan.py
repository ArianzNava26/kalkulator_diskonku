import sys
import subprocess


print("\nOk, Can I Help You? ")
pilihan = str(
    input(
        "\nA. Yes, Help me to know how Much the % Discount should I give to My Product?\nB. Yes,please Help me to know How Much My Discounted Price is?\n"
    )
)
if pilihan.lower() == "a":
    print("Choosing A")
    subprocess.run([sys.executable, "e-besardiskon.py"])

elif pilihan.lower() == "b":
    print("Choosing B")
    subprocess.run([sys.executable, "e-hargadiskon.py"])
else:
    print("Lu Nulis Apa sih?\n")
