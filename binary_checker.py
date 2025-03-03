def is_binary(s):
    # Menghapus spasi di awal dan akhir input
    s = s.strip()

    # Memeriksa apakah input kosong
    if not s:
        return False

    # Memeriksa apakah setiap karakter dalam input adalah 0 atau 1
    for i in s:
        if i != "0" and i != "1":
            return False

    return True


if __name__ == "__main__":
    # User memasukkan angka biner
    tmp = input("Masukkan bilangan biner: ")

    # Memanggil fungsi untuk memeriksa apakah input adalah bilangan biner
    if is_binary(tmp):
        # Jika input adalah bilangan biner, maka akan menampilkan "Valid"
        print(f"Valid")
    else:
        # Jika input bukan bilangan biner, maka akan menampilkan "Tidak valid"
        print(f"Tidak valid")
