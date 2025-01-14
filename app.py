from romaji_dict import romaji_dict

def main():
    print("----------------------------------------------")
    print("Selamat datang di Number to Romaji Converter!")
    print("----------------------------------------------")
    
    lanjut = 'y'
    
    while lanjut == 'y':
        input_angka = input("Masukkan angka: ")
        if input_angka.isdigit():

            # Cek apakah angka ada di dictionary langsung
            if input_angka in romaji_dict:
                print(f"Hasil: {romaji_dict[input_angka]}")  # Tampilkan langsung dari dictionary
            else:
                angka_str = input_angka
                hasil = []

                # Menentukan unit yang sesuai untuk angka
                unit_angka = ["", "juu", "hyaku", "sen", "man", "juu", "hyaku"]
                panjang_angka = len(angka_str)
                
                # Iterasi berdasarkan panjang angka
                for i in range(panjang_angka):
                    digit = angka_str[i]  # Ambil digit per iterasi
                    if digit != "0":  # Jika digit bukan 0
                        unit = unit_angka[panjang_angka - i - 1]  # Tentukan unit (juu, hyaku, dsb.)
                        if unit != "":  # Menambahkan unit setelah angka
                            hasil.append(romaji_dict[digit])
                            hasil.append(unit)
                        else:
                            hasil.append(romaji_dict[digit])

                print(f"Hasil: {' '.join(hasil)}")

        else:
            print("Tolong masukkan angka yang valid.")
        
        lanjut = input("Apakah Anda ingin mengonversi angka lain? (y/n): ")
    print('Aborted. Terimakasih Telah Menggunakan!')

if __name__ == "__main__":
    main()