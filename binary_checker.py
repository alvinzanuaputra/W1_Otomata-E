def binary_checker(s):
    # Daftar pola valid diurutkan berdasarkan panjang menurun agar pola terpanjang diutamakan
    valid_patterns = ["01001", "010", "10", "00"]
    
    # Selama string s belum kosong
    while s:
        matched = False
        # Cek setiap pola apakah menjadi prefix dari s
        for pattern in valid_patterns:
            if s.startswith(pattern):
                # Hapus pola tersebut dari s
                s = s[len(pattern):]
                matched = True
                break  # Keluar dari loop pola jika ada kecocokan
        # Jika tidak ada pola yang cocok, maka string tidak valid
        if not matched:
            return "Tidak valid"
    
    # Jika seluruh string telah terhapus (kosong), maka valid
    return "Valid"


def main():
    # User memasukkan angka biner
    binary_input = input("Masukkan bilangan biner: ")
    # Panggil fungsi binary_checker dan tampilkan hasilnya
    result = binary_checker(binary_input)
    print(result)


if __name__ == "__main__":
    main()
