from tkinter import Tk, Label, Entry, Button, StringVar
from romaji_dict import romaji_dict

# Fungsi untuk mengonversi angka ke romaji
def convert_to_romaji(angka):
    if angka in romaji_dict:  # Jika angka ada di dictionary
        return romaji_dict[angka]
    
    hasil = []
    unit_angka = ["", "juu", "hyaku", "sen", "man"]
    panjang_angka = len(angka)
    
    for i in range(panjang_angka):
        digit = angka[i]  # Ambil digit satu per satu
        if digit != "0":  # Lewati jika digit adalah 0
            unit = unit_angka[panjang_angka - i - 1]
            
            # Tangani kasus khusus
            if unit == "sen" and digit == "3":
                hasil.append("sanzen")
            elif unit == "sen" and digit == "8":
                hasil.append("hassen")
            elif unit == "hyaku" and digit in {"3", "6", "8"}:
                hasil.append({"3": "sanbyaku", "6": "roppyaku", "8": "happyaku"}[digit])
            elif unit == "man" and digit == "1":
                hasil.append("ichiman")
            else:
                hasil.append(romaji_dict[digit])
                if unit:
                    hasil.append(unit)
    return " ".join(hasil)

# Fungsi untuk menangani event klik tombol
def handle_convert():
    angka = input_var.get()
    if angka.isdigit() and 0 <= int(angka) <= 99999:  # Validasi input
        hasil.set(f"Hasil: {convert_to_romaji(angka)}")
    else:
        hasil.set("Masukkan angka valid (0-99.999).")

# Membuat GUI menggunakan Tkinter
root = Tk()
root.title("Number to Romaji Converter")
root.geometry("400x200")

# Input dan output
input_var = StringVar()
hasil = StringVar()

Label(root, text="Masukkan angka (maksimal 99.999):").pack(pady=10)
Entry(root, textvariable=input_var, width=20).pack()
Button(root, text="Konversi", command=handle_convert).pack(pady=10)
Label(root, textvariable=hasil, wraplength=300, justify="center").pack(pady=20)

root.mainloop()
